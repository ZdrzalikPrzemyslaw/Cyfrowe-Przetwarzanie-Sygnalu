import numpy as np

from Signal.Signal import Signal
from SignalAndImpulse import SignalAndImpulse
from typing import Union


def create_signal_and_impulse(signal: SignalAndImpulse, start_time: float, end_time: float, delta: float):
    data = {}
    for i in np.arange(start_time, end_time, delta):
        data[i] = signal.generate_value(i)
    return data


class SignalData:
    is_signal: bool
    time_values_dict: dict
    start_time: float
    end_time: float
    delta: float
    T: Union[float, None]

    def __str__(self):
        return "is_signal {0}" \
               "\nstart_time {1}" \
               "\nend_time {2}" \
               "\ndelta {3}" \
               "\nT {4}" \
               "\ntime_values: \n{5}".format(str(self.is_signal),
                                             str(self.start_time),
                                             str(self.end_time),
                                             str(self.delta),
                                             str(self.T),
                                             str(self.time_values_dict))

    def __init__(self, signal_and_impulse: SignalAndImpulse, start_time: float, end_time: float, delta: float):
        self.start_time = start_time
        self.end_time = end_time
        self.delta = delta
        self.T = None
        if isinstance(signal_and_impulse, Signal):
            self.is_signal = True
            # jesli ma okres, zapisujemy okres, jesli nie ma, zapisujemy None
            if hasattr(signal_and_impulse, 'T'):
                self.T = signal_and_impulse.T
        else:
            self.is_signal = False
        self.time_values_dict = create_signal_and_impulse(signal_and_impulse, start_time, end_time, delta)
        print(self)

    def write_self_to_file(self, path: str):
        with open(path, 'w') as file:
            file.write(self.__str__())
