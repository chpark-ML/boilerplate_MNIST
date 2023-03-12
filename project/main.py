"""
Pytorch model training of MNIST dataset
script example : 
``
"""
import hydra
from omegaconf import DictConfig


@hydra.main(config_path="configs/", config_name="config.yaml")
def main(config: DictConfig):

    return train(config)

if __name__ == "__main__":
    main()
