
import torch.nn as nn
#TODO: Find a new method to improve this
class VilBert_Stage2_ActionHead(nn.Module):
    """
    Outputs a 4-D action, where
    """
    def __init__(self, h2=128):
        super(VilBert_Stage2_ActionHead, self).__init__()
        self.linear = nn.Linear(h2, 16)

    def init_weights(self):
        pass

    def forward(self, features):
        x = self.linear(features)
        return x