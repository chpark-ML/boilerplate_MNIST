import torch
import torch.nn as nn


class MLP(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(MLP, self).__init__()
        self.inplanes = input_dim
        self.output_dim = output_dim
        self.mlp = nn.Sequential(
            nn.Linear(self.inplanes, self.inplanes * 2),
            nn.GELU(),
            nn.Dropout(p=0.05),
            nn.Linear(self.inplanes * 2, self.inplanes // 2),
            nn.GELU(),
            nn.Dropout(p=0.01),
            nn.Linear(self.inplanes // 2, self.output_dim))

        for m in self.modules():
            if isinstance(m, nn.Linear):
                torch.nn.init.xavier_uniform_(m.weight)
                m.bias.data.fill_(0.01)

    def forward(self, x):
        return self.mlp(x)
