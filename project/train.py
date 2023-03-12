import hydra
from omegaconf import DictConfig


class trainer():
    def __init__(self, cfg):
        self.model = hydra.utils.instantiate(cfg.model)
        params = filter(lambda p: p.requires_grad, self.model.parameters())
        # self.optimier = hydra.utils.instantiate(cfg.optimizer)
        # self.scheduler = hydra.utils.instantiate(cfg.scheduler)
        

def train(config: DictConfig):
    _trainer = trainer(config)
    pass
