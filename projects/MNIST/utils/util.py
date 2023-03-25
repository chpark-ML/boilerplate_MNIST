import numpy as np
import torch

import GPUtil
# util function

def set_seed(seed=1234):
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)

def get_device():
    # Select GPUs
    use_cuda = torch.cuda.is_available()
    if use_cuda:
        deviceIDs = GPUtil.getAvailable(order = 'memory', limit = 1, maxLoad = 0.5, maxMemory = 0.5, 
                                        includeNan=False, excludeID=[], excludeUUID=[])
        device = torch.device(f"cuda:{deviceIDs[0]}")
    else:
        device = torch.device("cpu")

    return device
