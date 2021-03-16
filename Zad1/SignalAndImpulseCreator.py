from Signal.Signal import Signal
from Impulse.Impulse import Impulse
import numpy as np


def create_signal(signal: Signal, start_time: float, end_time: float, delta: float):
    data = {}
    for i in np.arange(start_time, end_time, delta):
        data[i] = signal.signal(i)
    return data


def create_impulse(impulse: Impulse, start_time: float, end_time: float, delta: float):
    data = {}
    for i in np.arange(start_time, end_time, delta):
        data[i] = impulse.impulse(i)
    return data
