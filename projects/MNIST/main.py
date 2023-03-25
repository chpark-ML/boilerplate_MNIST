"""
Pytorch model training of MNIST dataset
script example : 
`HYDRA_FULL_ERROR=1 python3 project/main.py`
"""
import hydra
import numpy as np
import torch
from omegaconf import DictConfig

from projects.train import train


@hydra.main(version_base="1.3.2", config_path="configs", config_name="train.yaml")
def main(config: DictConfig):
    return train(config)

if __name__ == "__main__":
    main()
