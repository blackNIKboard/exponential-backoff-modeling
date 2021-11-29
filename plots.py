import numpy as np
import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('macosx')

fig_size = (11, 8)

if __name__ == "__main__":
    data = np.genfromtxt('data/average_delay_on_lambda.csv', delimiter=", ", names=["x", "y"])
    plt.figure(figsize=fig_size)
    plt.title('Average delay on Lambda')
    plt.xticks(np.linspace(0, max(data["x"]), 10))
    plt.yticks(np.linspace(0, max(data["y"]), 20))
    plt.xlabel('λ')
    plt.ylabel('d(λ)')
    plt.grid(True)
    plt.plot(data["x"], data["y"])
    plt.draw()

    data = np.genfromtxt('data/output_intensity_on_input_intensity.csv', delimiter=", ", names=["x", "y"])
    plt.figure(figsize=fig_size)
    plt.title('Output intensity on input intensity')
    plt.xticks(np.linspace(0, max(data["x"]), 10))
    plt.yticks(np.linspace(0, max(data["x"]), 20))
    plt.xlabel('λ')
    plt.ylabel('λ')
    plt.grid(True)
    plt.plot(data["x"], data["x"])
    plt.plot(data["x"], data["y"])
    plt.draw()

    data = np.genfromtxt('data/average_delay_on_exponent.csv', delimiter=", ", names=["x", "y"])
    plt.figure(figsize=fig_size)
    plt.title('Average delay on Exponent')
    plt.xticks(np.linspace(0, max(data["x"]), 10))
    plt.yticks(np.linspace(0, max(data["y"]), 20))
    plt.xlabel('e')
    plt.ylabel('d(e)')
    plt.grid(True)
    plt.plot(data["x"], data["y"])
    plt.draw()

    data = np.genfromtxt('data/intensity_on_exponent.csv', delimiter=", ", names=["x", "y", "z"])
    plt.figure(figsize=fig_size)
    plt.title('Output intensity on Exponent')
    plt.xticks(np.linspace(0, max(data["x"]), 10))
    plt.yticks(np.linspace(0, max(max(data["y"]), max(data["z"])), 20))
    plt.xlabel('e')
    plt.ylabel('λ(e)')
    plt.grid(True)
    plt.plot(data["x"], data["y"])
    plt.plot(data["x"], data["z"])
    plt.draw()

    plt.show()
