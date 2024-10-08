import torch 
import torch.nn as nn   
import torch.optim as optim
import torch.nn.functional as F
import torchvision.datasets as datasets
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

# MLP Network (Multi-Layer Perceptron)
class NN(nn.Module):
    def __init__(self, input_size, num_classes):
        super(NN, self).__init__()
        self.fc1 = nn.Linear(input_size, 50)
        self.fc2 = nn.Linear(50, 50)
        self.fc3 = nn.Linear(50, num_classes)   

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)  
        return x

# Load dataset
train_dataset = datasets.MNIST(root='dataset/', train=True, transform=transforms.ToTensor(), download=True)
valid_dataset = datasets.MNIST(root='dataset/', train=False, transform=transforms.ToTensor(), download=True)

train_loader = DataLoader(dataset=train_dataset, batch_size=100, shuffle=True)
valid_loader = DataLoader(dataset=valid_dataset, batch_size=100, shuffle=True)

image, labels = next(iter(train_loader))
print(f"Shape of image: {image.size()}")
print(f"Shape of labels: {labels.size()}")

input_size = 28 * 28
num_classes = 10
learning_rate = 0.01
num_epochs = 20  

model = NN(input_size=input_size, num_classes=num_classes)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Training
for epoch in range(num_epochs):
    for batch_idx, (data, targets) in enumerate(train_loader):

        data = data.reshape(data.shape[0], -1)
        
        # Forward
        scores = model(data)
        loss = criterion(scores, targets)

        # Backward
        optimizer.zero_grad()
        loss.backward()

        # Gradient descent
        optimizer.step()

def check_accuracy(loader, model):
    if loader == train_loader:
        print("Checking accuracy on training data")
    else:
        print("Checking accuracy on validation data")

    num_correct = 0 
    num_samples = 0 
    model.eval()

    with torch.no_grad():  # แก้ไขจาก torch.no_grand() เป็น torch.no_grad()
        for x, y in loader:
            x = x.reshape(x.shape[0], -1)
            scores = model(x)
            _, predictions = scores.max(1)
            num_correct += (predictions == y).sum().item()
            num_samples += predictions.size(0)
        print(f"Got {num_correct}/{num_samples} with accuracy {float(num_correct) / float(num_samples) * 100:.2f}")
    model.train()

check_accuracy(train_loader, model)
check_accuracy(valid_loader, model)

# N_image = 10
# fig, ax = plt.subplots(1, N_image, figsize=(17, 7))
# for i in range(N_image):
#     im, label = train_dataset[i]
#     ax[i].imshow(im[0,:,:], cmap='gray', interpolation='bilinear')
#     ax[i].set_title(f"{label}")
# plt.show()