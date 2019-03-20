import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = np.linspace(start=-20, stop=20, num=100000)

    fig, ax = plt.subplots()
    ax.plot(x, x, label='Linear Function')
    ax.plot(x, x**2, label='Quadratic Function')
    ax.plot(x, x + x**2 + x**3, label='Polynomial Function')
    ax.legend(loc='upper left')
    ax.set_ylim(bottom=-100, top=100)
    fig.savefig('turbulent_velocity.pdf')
