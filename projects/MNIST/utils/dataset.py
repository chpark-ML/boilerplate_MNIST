from torch.utils.data import Dataset
from torchvision.datasets import MNIST

# dataset
class MNIST_Dataset(Dataset):
    def __init__(self, mode="train"):
        self.x_data = MNIST(download_root, transform=mnist_transform, train=True, download=True)
        self.y_data = None

    def __getitem__(self, index): 
        return self.x_data[index], self.y_data[index]
        
    def __len__(self): 
        return self.x_data.shape[0]