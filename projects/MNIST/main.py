"""
Pytorch model training of MNIST dataset
script example : 
`HYDRA_FULL_ERROR=1 python3 project/main.py`
"""
import hydra
import torch
from omegaconf import DictConfig

from project.train import train


random_seed = 1
torch.backends.cudnn.enabled = False
torch.manual_seed(random_seed)


@hydra.main(version_base="1.3.2", config_path="configs", config_name="train.yaml")
def main(config: DictConfig):
    return train(config)

if __name__ == "__main__":
    main()
