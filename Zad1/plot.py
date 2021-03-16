import matplotlib.pyplot as plt
import numpy as np
from SignalAndImpulseCreator import SignalData


def plot_analog(signal_dictionary: dict):
    array_from_list = np.asarray(list(signal_dictionary.items()))
    plt.plot(array_from_list[:, 0], array_from_list[:, 1])
    plt.show()


def plot_discrete(impulse_dictionary: dict):
    array_from_list = np.asarray(list(impulse_dictionary.items()))
    plt.scatter(array_from_list[:, 0], array_from_list[:, 1])
    plt.show()


def plot(data: SignalData):
    if data.is_signal:
        plot_analog(data.time_values_dict)
    else:
        plot_discrete(data.time_values_dict)