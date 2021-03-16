import numpy as np

from Signal.Signal import Signal
from SignalAndImpulse import SignalAndImpulse


def create_signal_and_impulse(signal: SignalAndImpulse, start_time: float, end_time: float, delta: float):
    data = {}
    for i in np.arange(start_time, end_time, delta):
        data[i] = signal.generate_value(i)
    return data


class SignalData:
    is_signal: bool
    time_values_dict: dict

    def __init__(self, signal_and_impulse: SignalAndImpulse, start_time: float, end_time: float, delta: float):
        if isinstance(signal_and_impulse, Signal):
            self.is_signal = True
        else:
            self.is_signal = False
        self.time_values_dict = create_signal_and_impulse(signal_and_impulse, start_time, end_time, delta)
