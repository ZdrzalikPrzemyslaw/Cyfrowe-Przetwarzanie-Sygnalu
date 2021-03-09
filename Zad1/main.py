# This is a sample Python script.
import matplotlib.pyplot as plt

from Impulse import Impulse
from Signal import Signal
from SingularImpulse import SingularImpulse
from ImpulseNoise import ImpulseNoise
from UniformlyDistributedNoise import UniformlyDistributedNoise


def plot_analog(signal: Signal):
    plt.plot([x / 100 for x in range(0, 1000)], [signal.signal(x / 100) for x in range(0, 1000)])
    plt.show()


def plot_discrete(impulse: Impulse):
    plt.scatter([x / 1 for x in range(-5, 5)], [impulse.impulse(x / 1) for x in range(-5, 5)])
    plt.show()


if __name__ == '__main__':
    plot_analog(UniformlyDistributedNoise())
