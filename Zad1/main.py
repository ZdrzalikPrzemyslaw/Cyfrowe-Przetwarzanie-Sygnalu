import matplotlib.pyplot as plt
import numpy as np
from Impulse.Impulse import Impulse
from Signal.Signal import Signal
from SignalAndImpulseCreator import create_signal
from Signal.RectangularSignal import RectangularSignal


def plot_analog(signal_dictionary: dict):
    array_from_list = np.asarray(list(signal_dictionary.items()))
    plt.plot(array_from_list[:, 0], array_from_list[:, 1])
    plt.show()


def plot_discrete(impulse_dictionary: dict):
    array_from_list = np.asarray(list(impulse_dictionary.items()))
    plt.scatter(array_from_list[:, 0], array_from_list[:, 1])
    plt.show()


if __name__ == '__main__':
    dic = create_signal(RectangularSignal(), 0.0, 10.0, 0.01)
    plot_analog(dic)
