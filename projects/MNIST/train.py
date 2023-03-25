import hydra
import numpy as np
import torch
from omegaconf import DictConfig

seed = 1234
torch.manual_seed(seed)
torch.cuda.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
np.random.seed(seed)

# Select GPUs
use_cuda = not args.no_cuda and torch.cuda.is_available()
gpu_list = [int(i) for i in args.gpu.strip().split(",")]
device = torch.device(f"cuda:{gpu_list[0]}" if use_cuda else "cpu")

class trainer():
    def __init__(self, cfg):
        self.model = hydra.utils.instantiate(cfg.model)
        params = filter(lambda p: p.requires_grad, self.model.parameters())
        self.optimier = hydra.utils.instantiate(cfg.optimizer)
        self.scheduler = hydra.utils.instantiate(cfg.scheduler)
        

def train(config: DictConfig):
    _trainer = trainer(config)
    pass
