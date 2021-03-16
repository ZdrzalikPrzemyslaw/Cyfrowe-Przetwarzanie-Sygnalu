import numpy as np

from SignalAndImpulse import SignalAndImpulse


def create_signal_and_impulse(signal: SignalAndImpulse, start_time: float, end_time: float, delta: float):
    data = {}
    for i in np.arange(start_time, end_time, delta):
        data[i] = signal.generate_value(i)
    return data
