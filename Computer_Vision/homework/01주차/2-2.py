import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x, a):
    return 1 / (1 + np.exp(-a * x))

x = np.linspace(-10, 10, 100)
y = sigmoid(x, 1)

plt.plot(x, y)
plt.title("Sigmoid Function")
plt.xlabel("x")
plt.ylabel("sigmoid(x)")
plt.grid()

plt.show()