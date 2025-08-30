import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda, Compose
import matplotlib.pyplot as plt

# Check if all imports are working
try:
    # Check if torch is working
    if torch.backends.mps.is_available():
        print("Torch is working, and MPS (Metal Performance Shaders) is available. MPS is optimized for Apple Macbook Pros.")
    elif torch.cuda.is_available():
        print("Torch is working, and CUDA is available.")
    else:
        print("Torch is working, but neither MPS nor CUDA is available.")
    
    _ = nn.Linear(10, 5)  # Test torch.nn
    _ = DataLoader([])  # Test torch.utils.data
    _ = datasets.FakeData(transform=ToTensor())  # Test torchvision.datasets and transforms
    _ = Compose([ToTensor(), Lambda(lambda x: x)])  # Test torchvision.transforms.Compose and Lambda
    plt.plot([0, 1], [0, 1])  # Test matplotlib.pyplot
    print("All imports are working correctly.")
except Exception as e:
    print(f"An import or usage error occurred: {e}")