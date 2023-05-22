import hydra
import numpy as np
import torch
from omegaconf import DictConfig


class trainer():
    def __init__(self, cfg):
        self.model = hydra.utils.instantiate(cfg.model)
        params = filter(lambda p: p.requires_grad, self.model.parameters())
        self.optimier = hydra.utils.instantiate(cfg.optimizer, params)
        self.scheduler = hydra.utils.instantiate(cfg.scheduler)
    
    def fit():
        None


def run_epoch():
    pass


def train_epoch():
    pass


@torch.no_grad()
def val_epoch():
    pass


@torch.no_grad()
def test_epoch():
    pass


def train(config: DictConfig):
    _trainer = trainer(config)
    pass