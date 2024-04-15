import torch
import torch.nn as nn
import torch.optim as optim
import pyitt
# Define a simple neural network
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc = nn.Linear(1, 1)
    def forward(self, x):
        return self.fc(x)
# Create a model, define loss function and optimizer
model = Net()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
# Generate some data
x_train = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y_train = torch.tensor([[2.0], [4.0], [6.0], [8.0]])
# Training loop
with pyitt.task('Training'):
    for epoch in range(1000):
        optimizer.zero_grad()
        output = model(x_train)
        loss = criterion(output, y_train)
        loss.backward()
        optimizer.step()
        if epoch % 100 == 0:
            print(f"Epoch {epoch+1}, Loss: {loss.item()}")
# Test the trained model
with pyitt.task('Prediction'):
    x_test = torch.tensor([[5.0]])
    print("\nPrediction for x=5:")
    print(model(x_test))

