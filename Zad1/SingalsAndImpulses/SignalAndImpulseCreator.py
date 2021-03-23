from typing import Union

import matplotlib.pyplot as plt
import numpy as np

from SingalsAndImpulses.Signal.Signal import Signal
from SingalsAndImpulses.Signal.SinusoidalSignal import SinusoidalSignal
from SingalsAndImpulses.SignalAndImpulse import SignalAndImpulse


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
    is_real: bool
    T: Union[float, None]

    def __repr__(self):
        return "Signal" if self.is_signal is True else "Impulse"

    def __str__(self):
        return "is_signal: {0}" \
               "\nstart_time: {1}" \
               "\nend_time: {2}" \
               "\ndelta: {3}" \
               "\nT: {4}" \
               "\nis_real: {5}" \
               "\ntime_values: \n{6}".format(str(self.is_signal),
                                             str(self.start_time),
                                             str(self.end_time),
                                             str(self.delta),
                                             str(self.T),
                                             str(self.is_real),
                                             str(self.time_values_dict))

    def __init__(self, signal_and_impulse: SignalAndImpulse = SinusoidalSignal(1, 1), start_time: float = 0,
                 end_time: float = 10, delta: float = 0.05, is_real: bool = True, is_new: bool = True):
        if is_new:
            self.is_real = is_real
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
        else:
            pass

    @staticmethod
    def __can_return_none(val):
        if val == "None":
            return None
        else:
            return float(val)

    @staticmethod
    def load_file(path: str):
        with open(path, 'r') as file:
            is_signal: bool = bool(file.readline().strip().split()[1])
            start_time: float = float(file.readline().strip().split()[1])
            end_time: float = float(file.readline().strip().split()[1])
            delta: float = float(file.readline().strip().split()[1])
            T: Union[float, None] = SignalData.__can_return_none(file.readline().strip().split()[1])
            is_real: bool = bool(file.readline().strip().split()[1])
            file.readline()
            times_values_dict: dict = eval(file.readline().strip())
            ret_val = SignalData(is_new=False)
            ret_val.is_signal = is_signal
            ret_val.start_time = start_time
            ret_val.end_time = end_time
            ret_val.delta = delta
            ret_val.T = T
            ret_val.is_real = is_real
            ret_val.time_values_dict = times_values_dict
            return ret_val

    def __get_values_for_calc(self) -> dict:
        if self.T is None:
            return self.time_values_dict
        elif (self.end_time - self.start_time) % self.T == 0:
            return self.time_values_dict
        else:
            end_time = self.end_time - ((self.end_time - self.start_time) % self.T)
            return dict([(k, self.time_values_dict[k]) for k in self.time_values_dict if k <= end_time])

    def mean(self) -> float:
        ret_val = 0
        for key, value in self.__get_values_for_calc().items():
            ret_val += value
        return ret_val / len(self.time_values_dict)

    def mean_abs(self) -> float:
        ret_val = 0
        for key, value in self.__get_values_for_calc().items():
            ret_val += abs(value)
        return ret_val / len(self.time_values_dict)

    def mean_power(self) -> float:
        ret_val = 0
        for key, value in self.__get_values_for_calc().items():
            ret_val += value ** 2
        return ret_val / len(self.time_values_dict)

    def variance(self) -> float:
        ret_val = 0
        mean = self.mean()
        for key, value in self.__get_values_for_calc().items():
            ret_val += (value - mean) ** 2
        return ret_val / len(self.time_values_dict)

    def root_mean_square(self):
        # TODO: sprawdzic czy to rzeczywiscie jest sqrt
        return self.variance() ** (1.0 / 2)

    def save_plot(self):
        # TODO
        pass

    def save_file(self, path: str):
        # TODO pobierz sciezke
        with open(path, 'w') as file:
            file.write(self.__str__())

    def plot_analog(self):
        array_from_list = np.asarray(list(self.time_values_dict.items()))
        plt.plot(array_from_list[:, 0], array_from_list[:, 1])
        plt.show()
        unique = np.unique(array_from_list[:, 1])
        plt.hist(array_from_list[:, 1], bins=len(unique))
        plt.show()

    def plot_discrete(self):
        array_from_list = np.asarray(list(self.time_values_dict.items()))
        plt.scatter(array_from_list[:, 0], array_from_list[:, 1])
        plt.show()
        unique = np.unique(array_from_list[:, 1])
        plt.hist(array_from_list[:, 1], bins=len(unique))
        plt.show()

    def plot(self):
        if self.is_signal:
            self.plot_analog()
        else:
            self.plot_discrete()

    def operation(self, signal, operation: str):
        if operation == "add":
            self.__add_signals(signal)
        elif operation == "sub":
            self.__sub_signals(signal)
        elif operation == "mul":
            self.__mul_signals(signal)
        elif operation == "div":
            self.__div_signals(signal)
        else:
            pass

    def __add_signals(self, signal):
        pass

    def __sub_signals(self, signal):
        pass

    def __mul_signals(self, signal):
        pass

    def __div_signals(self, signal):
        pass
