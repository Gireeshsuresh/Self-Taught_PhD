from numpy.core.shape_base import block
import torch
import torchvision
from torch import mode, nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda, Compose
import matplotlib
import matplotlib.pyplot as plt
from drawnow import drawnow


import numpy as np

# Check Version
t_ver = torch.__version__
tv_ver = torchvision.__version__
mp_ver = matplotlib.__version__

# Print Version
print(F"-------------------- Version Info --------------------")
print(F"Torch  \t\t= {t_ver}")
print(F"TorchVision  \t= {tv_ver}")
print(F"MatplotLib  \t= {mp_ver}")
print(F"------------------------------------------------------")


# Download training data from open datasets.
training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
)

# Download test data from open datasets.
test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor(),
)

batch_size = 64

# Create data loaders.
train_dataloader = DataLoader(training_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)

for data, target in test_dataloader:
    print(f"Shape of Data [N, C, H, W] : {data.shape} \nDType : {data.dtype}")
    print(f"\nShape of target : {target.shape} \nDType : {target.dtype}  ")
    break
print(F"------------------------------------------------------")

# Get cpu or gpu device for training.
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"\nUsing {device} device\n")


# Define model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
            nn.ReLU()
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

# Early Stopping Class


class EarlyStopping:
    """Early stops the training if validation loss doesn't improve after a given patience."""

    def __init__(self, patience=7, verbose=False, delta=0, path='checkpoint.pt', trace_func=print):
        """
        Args:
            patience (int): How long to wait after last time validation loss improved.
                            Default: 7
            verbose (bool): If True, prints a message for each validation loss improvement.
                            Default: False
            delta (float): Minimum change in the monitored quantity to qualify as an improvement.
                            Default: 0
            path (str): Path for the checkpoint to be saved to.
                            Default: 'checkpoint.pt'
            trace_func (function): trace print function.
                            Default: print
        """
        self.patience = patience
        self.verbose = verbose
        self.counter = 0
        self.best_score = None
        self.early_stop = False
        self.val_loss_min = np.Inf
        self.delta = delta
        self.path = path
        self.trace_func = trace_func

    def __call__(self, val_loss, model):

        score = -val_loss

        if self.best_score is None:
            self.best_score = score
            self.save_checkpoint(val_loss, model)
        elif score <= self.best_score + self.delta:
            self.counter += 1
            self.trace_func(
                f'EarlyStopping counter: {self.counter} out of {self.patience}')
            if self.counter >= self.patience:
                self.early_stop = True
        else:
            self.best_score = score
            self.save_checkpoint(val_loss, model)
            self.counter = 0

    def save_checkpoint(self, val_loss, model):
        '''Saves model when validation loss decrease.'''
        if self.verbose:
            self.trace_func(
                f'Validation loss decreased ({self.val_loss_min:.6f} --> {val_loss:.6f}).  Saving model ...')
        torch.save(model.state_dict(), self.path)
        self.val_loss_min = val_loss


model = NeuralNetwork().to(device)
print(model)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-1)


def train(dataloader, model, loss_fn, optimizer, patience, train_losses, avg_train_losses):
    size = len(dataloader.dataset)

    for batch, (data, target) in enumerate(dataloader):
        data, target = data.to(device), target.to(device)

        # Compute prediction error
        pred = model(data)
        loss = loss_fn(pred, target)

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        train_losses.append(loss.item())
        # Print Stats once every 100 Batches
        if batch % 100 == 0:
            loss, current = loss.item(), batch * len(data)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

    train_loss = np.average(train_losses)
    avg_train_losses.append(train_loss)
    return avg_train_losses


def test(dataloader, model, test_losses, avg_test_losses):
    size = len(dataloader.dataset)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for data, target in dataloader:
            data, target = data.to(device), target.to(device)
            pred = model(data)
            test_loss += loss_fn(pred, target).item()
            test_losses.append(test_loss/size)
            correct += (pred.argmax(1) ==
                        target).type(torch.float32).sum().item()

    t_loss = np.average(test_losses)
    avg_test_losses.append(t_loss)
    test_loss /= size
    correct /= size
    print(
        f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")
    return avg_test_losses, t_loss


epochs = 200
patience = 10

# to track the average training loss per epoch as the model trains
avg_train_losses = []
avg_test_losses = []

# initialize the early_stopping object
early_stopping = EarlyStopping(patience=patience, verbose=True)

# visualize the loss as the network trained
fig = plt.figure(figsize=(10, 8))


def viz():
    plt.plot(range(1, len(avg_train_loss)+1),
             avg_train_loss, label='Training Loss')
    plt.plot(range(1, len(avg_test_loss)+1),
             avg_test_loss, label='Validation Loss')

    # find position of lowest validation loss
    minposs = avg_test_loss.index(min(avg_test_loss))+1
    plt.axvline(minposs, linestyle='--', color='r',
                label='Early Stopping Checkpoint')

    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.ylim(0, 1)  # consistent scale
    plt.xlim(0, len(avg_train_loss)+1)  # consistent scale
    plt.grid(True)
    plt.legend()
    plt.tight_layout()


for t in range(epochs):
    train_losses = []
    val_losses = []

    print(f"Epoch {t+1}\n-------------------------------")
    avg_train_loss = train(dataloader=train_dataloader,
                           model=model,
                           loss_fn=loss_fn,
                           optimizer=optimizer,
                           patience=patience,
                           train_losses=train_losses,
                           avg_train_losses=avg_train_losses)
    # print(f"Train L = {avg_train_loss}")
    avg_test_loss, t_loss = test(dataloader=test_dataloader,
                                 model=model,
                                 test_losses=val_losses,
                                 avg_test_losses=avg_test_losses)
    early_stopping(t_loss, model)
    if early_stopping.early_stop:
        print("Early stopping")
        break

    drawnow(viz)


# load the last checkpoint with the best model
model.load_state_dict(torch.load('checkpoint.pt'))

fig.savefig('loss_plot.png', bbox_inches='tight')

print("Done!")
