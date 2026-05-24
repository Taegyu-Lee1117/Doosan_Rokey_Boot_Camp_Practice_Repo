import torch
import numpy as np

x_train = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y_train = torch.tensor([[3.0], [5.0], [7.0], [9.0]])

W = torch.tensor(1.0, requires_grad=True).float()
B = torch.tensor(1.0, requires_grad=True).float()

lr = 0.01
epochs = 500

history = np.zeros((0, 2))

def pred(x):
    return W * x + B

def mse(Yp, Y):
    return ((Yp - Y) ** 2).mean()

for i in range(epochs):
    Yp = pred(x_train)
    loss = mse(Yp, y_train)

    loss.backward()

    with torch.no_grad():
        W -= lr * W.grad
        B -= lr * B.grad

        W.grad.zero_()
        B.grad.zero_()

    if (i % 100 == 0):
        item = np.array([i, loss.item()])
        history = np.vstack((history, item))

print(f'초기상태 손실: {history[0,1]:.4f}')
print(f'최종상태 손실: {history[-1,1]:.4f}')