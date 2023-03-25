import io
import logging
import os
from typing import Union

import GPUtil
import hydra
import omegaconf
import torch
import torch.nn as nn
from cryptography.fernet import Fernet
from torch import Tensor

_ENCRYPTION_KEY = None

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@torch.no_grad()
def get_inference_result(fn: Union[nn.Module, torch.jit._script.RecursiveScriptModule], sample: Tensor,
                         device: torch.device) -> torch.Tensor:
    if isinstance(fn, nn.Module):
        fn.to(device).eval()
    result = fn(sample.to(device))  # torch.Size([1, 1, 48, 72, 72]) > torch.Size([1, 1, 48, 72, 72])
    return result


def load_checkpoint(model: nn.Module, model_path: str) -> torch.nn.Module:
    """Loads checkpoint from directory"""
    assert os.path.exists(model_path)
    checkpoint = torch.load(model_path, map_location='cpu')

    if isinstance(checkpoint, nn.Module):
        model = checkpoint
        logger.info(f"Model loaded from {model_path}")

    elif isinstance(checkpoint, dict):
        # keys of checkpoint, (epoch, model, optimizer, scaler)
        model.load_state_dict(checkpoint["model"], strict=True)
        logger.info(f"Model loaded from {model_path}")

    return model


def save_encrypted_checkpoint(
        trace: torch.jit._script.RecursiveScriptModule,
        key: bytes,
        path_to_save: str = '',
        file_name: str = 'project.pt.enc',
) -> None:
    # CPU trace
    buff = io.BytesIO()
    torch.jit.save(trace, buff)
    buff.seek(0)
    enc = Fernet(key).encrypt(buff.read())

    # save encrypted trace_fn
    file_path = os.path.join(path_to_save, file_name)
    torch.save(enc, file_path)
    logger.info(f'Saved model to {file_path}.')


def get_decrypted_model(
        key: bytes,
        path_to_load: str = '',
        file_name: str = '',
) -> torch.jit._script.RecursiveScriptModule:
    # Decryption using the model key.
    file_path = os.path.join(path_to_load, file_name)
    buff = io.BytesIO(Fernet(key).decrypt(torch.load(file_path)))
    trace = torch.jit.load(buff)
    logger.info(f'Loaded model from {file_path}.')

    return trace


def main() -> None:
    logger.info("Encrypt weight file.")

    # load config
    cfg = omegaconf.OmegaConf.load("/opt/lct/projects/nodule_segmentation/configs/model/unet_3d.yaml")

    # Materials
    if _ENCRYPTION_KEY:
        encryption_key = Fernet.generate_key()
    else:
        encryption_key = _ENCRYPTION_KEY
    prefix = '/opt/lct/projects/nodule_segmentation/outputs/buffer_8_smoothing_0.01/2023-03-17_12-27-36'
    path_to_load_weight = prefix + '/model.pth'
    path_to_save_encrypted = prefix
    file_name = 'ml.pt.enc'

    sample = torch.rand((1, 1, 48, 72, 72), dtype=torch.float32)

    # load checkpoint
    model = hydra.utils.instantiate(cfg, _recursive_=False)
    model = load_checkpoint(model, path_to_load_weight)

    # device
    device_ids: list = GPUtil.getAvailable(order='memory', limit=1, maxLoad=0.5, maxMemory=0.5, includeNan=False)
    assert len(device_ids) > 0, "There is no available GPU."
    dict_device = {
        'cpu': torch.device(f'cpu'),
        'gpu': torch.device(f'cuda:{int(device_ids[0])}')
    }

    # encryption for cpu and gpu version
    for device_type, device in dict_device.items():
        if device is not None:
            file_name_with_prefix = 'cpu_' + file_name if device.type == 'cpu' else 'gpu_' + file_name
            r_c_torch = get_inference_result(model, sample, device)

            # Encryption
            model.to(device).eval()
            trace = torch.jit.trace(
                func=model,
                example_inputs=sample.to(device),
                check_tolerance=1e-6
            )
            trace = torch.jit.freeze(trace)  # Freeze model.

            r_c_torchscript = get_inference_result(trace, sample, device)
            save_encrypted_checkpoint(
                trace,
                key=encryption_key,
                path_to_save=path_to_save_encrypted,
                file_name=file_name_with_prefix
            )

            # Decryption
            trace = get_decrypted_model(
                key=encryption_key,
                path_to_load=path_to_save_encrypted,
                file_name=file_name_with_prefix
            )
            r_c_torchscript_decrypted = get_inference_result(trace, sample, device)

            assert torch.all(torch.isclose(r_c_torch, r_c_torchscript, atol=1e-06, rtol=0.0)) and \
                   torch.all(torch.isclose(r_c_torchscript, r_c_torchscript_decrypted, atol=1e-06, rtol=0.0)), \
                f'Inference results from {device_type} models are not identical.'


if __name__ == "__main__":
    main()

