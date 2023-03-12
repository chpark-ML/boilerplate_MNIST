"""
Pytorch model training of MNIST dataset
script example : 
`HYDRA_FULL_ERROR=1 python3 project/main.py`
"""
import hydra
from omegaconf import DictConfig

from project.train import train


@hydra.main(version_base="1.3.2", config_path="configs", config_name="train.yaml")
def main(config: DictConfig):
    return train(config)

if __name__ == "__main__":
    main()
