import math
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
                 end_time: float = 10, delta: float = 0.05, is_real: bool = True, is_new: bool = True, T: float = None,
                 is_signal: bool = None, time_values_dict: dict = None):
        self.is_real = is_real
        self.start_time = start_time
        self.end_time = end_time
        self.delta = delta
        if is_new:
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
            self.T = T
            self.time_values_dict = time_values_dict
            self.is_signal = is_signal

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
            ret_val = SignalData(start_time=start_time, end_time=end_time, is_signal=is_signal, delta=delta,
                                 is_new=False, T=T, time_values_dict=times_values_dict, is_real=is_real)
            return ret_val

    def __get_values_for_calc(self) -> dict:
        if self.T is None:
            return self.time_values_dict
        elif (self.end_time - self.start_time) % self.T == 0:
            return self.time_values_dict
        else:
            end_time = self.end_time - ((self.end_time - self.start_time) % self.T)
            return dict([(k, self.time_values_dict[k]) for k in self.time_values_dict if k <= end_time])

    def __mean(self) -> float:
        ret_val = 0
        for key, value in self.__get_values_for_calc().items():
            ret_val += value
        return ret_val / len(self.time_values_dict)

    def __mean_abs(self) -> float:
        ret_val = 0
        for key, value in self.__get_values_for_calc().items():
            ret_val += abs(value)
        return ret_val / len(self.time_values_dict)

    def __mean_power(self) -> float:
        ret_val = 0
        for key, value in self.__get_values_for_calc().items():
            ret_val += value ** 2
        return ret_val / len(self.time_values_dict)

    def __variance(self) -> float:
        ret_val = 0
        mean = self.__mean()
        for key, value in self.__get_values_for_calc().items():
            ret_val += (value - mean) ** 2
        return ret_val / len(self.time_values_dict)

    def __root_mean_square(self):
        # TODO: sprawdzic czy to rzeczywiscie jest sqrt
        return math.sqrt(self.__mean_power())

    def print_information(self):
        print("\nWartosc srednia: " + str(self.__mean()))
        print("Wartosc srednia bezwzgledna: " + str(self.__mean_abs()))
        print("Wartosc skuteczna: " + str(self.__root_mean_square()))
        print("Wariancja: " + str(self.__variance()))
        print("Moc srednia: " + str(self.__mean_power()) + "\n")

    def save_plot(self):
        ch = 'x'
        while ch not in ['y', 'n']:
            ch = input("Czy chcesz zachować wykres sygnału? [y/n]")
            if ch not in ['y', 'n']:
                print("zly input")
            elif ch == 'y':
                print("Podaj nazwę pliku dla wykresu")
                while True:
                    inp = input()
                    if not inp.isspace() or not len(inp) == 0:
                        plt.savefig(inp + '.png')
                        break
                    else:
                        print("zly input")

    def save_file(self):
        print("Podaj nazwę pliku")
        while True:
            inp = input()
            if not inp.isspace() or not len(inp) == 0:
                with open(inp, 'w') as file:
                    file.write(self.__str__())
                break
            else:
                print("zly input")

    def plot_analog(self):
        array_from_list = np.asarray(list(self.time_values_dict.items()))
        plt.plot(array_from_list[:, 0], array_from_list[:, 1])
        self.save_plot()
        plt.show()
        array_from_list = np.asarray(list(self.__get_values_for_calc().items()))
        values = array_from_list[:, 1]
        plt.hist(values.astype('float'))
        plt.show()

    def plot_discrete(self):
        array_from_list = np.asarray(list(self.time_values_dict.items()))
        plt.scatter(array_from_list[:, 0], array_from_list[:, 1])
        self.save_plot()
        plt.show()
        array_from_list = np.asarray(list(self.__get_values_for_calc().items()))
        values = array_from_list[:, 1]
        plt.hist(values.astype('float'))
        plt.show()

    def plot(self):
        if self.is_signal:
            self.plot_analog()
        else:
            self.plot_discrete()

    def operation(self, signal, operation: str):
        if operation == "add":
            self.__make_operation(signal, self.__add_signals)
        elif operation == "sub":
            self.__make_operation(signal, self.__sub_signals)
        elif operation == "mul":
            self.__make_operation(signal, self.__mul_signals)
        elif operation == "div":
            self.__make_operation(signal, self.__div_signals)
        else:
            pass

    def operation_on_one_signal(self, operation: str):
        if operation == "sampling":
            self.__sampling()
        elif operation == "quantization":
            self.__quantization()
        elif operation == "reconstruction":
            self.__make_operation_on_one_signal(self.__mul_signals)
        else:
            pass

    def __sampling(self):
        choice = -1
        print("Ile próbek na sekunde: ")
        try:
            choice = float(input())
        except ValueError:
            print("zly input")
            pass

        modulo = (1 / self.delta) / choice

        new_times_values = {}
        for idx, time in enumerate(self.time_values_dict):
            if round(idx % modulo) == 0:
                new_times_values[time] = self.time_values_dict[time]
        print(new_times_values)
        new_signal = SignalData(start_time=min(new_times_values.keys()),
                                end_time=max(new_times_values.keys()),
                                is_signal=False, delta=1 / choice,
                                is_new=False, T=None, time_values_dict=new_times_values,
                                is_real=self.is_real)
        new_signal.plot()
        new_signal.save_file()

    def __quantization(self):
        choice = -1
        print("Liczba poziomów kwantyzacji: ")
        try:
            choice = float(input())
        except ValueError:
            print("zly input")
            pass
        max_value = max(self.time_values_dict.values())
        min_value = min(self.time_values_dict.values())
        delta = (max_value - min_value) / choice

        new_times_values = {}
        for time in self.time_values_dict:
            i = math.floor((self.time_values_dict[time] - min_value) / delta)
            i = min(i, choice - 1)
            if i == 0:
                new_value = min_value
            elif i == choice - 1:
                new_value = max_value
            else:
                new_value = ((min_value + (i * delta)) * 2 + delta) / 2
            new_times_values[time] = new_value
        print(new_times_values)
        new_signal = SignalData(start_time=min(new_times_values.keys()),
                                end_time=max(new_times_values.keys()),
                                is_signal=False, delta=1 / choice,
                                is_new=False, T=None, time_values_dict=new_times_values,
                                is_real=self.is_real)
        new_signal.plot()

    # def __make_operation_on_one_signal(self, op):
    #     new_signal = self.__calculating(signal, self, op)
    #     new_signal.plot()
    #     new_signal.save_file()
    #     new_signal.print_information()

    def __make_operation(self, signal, op):
        if self.delta < signal.delta:
            new_signal = self.__calculating(self, signal, op)
        else:
            new_signal = self.__calculating(signal, self, op)
        new_signal.plot()
        new_signal.save_file()
        new_signal.print_information()

    @staticmethod
    def __calculating(first_signal, second_signal, op):
        list_signal_time = list(second_signal.time_values_dict.keys())
        list_signal_time.sort()
        new_signal = {}
        for time in first_signal.time_values_dict:
            if time < list_signal_time[0] or time > list_signal_time[-1]:
                new_signal[time] = first_signal.time_values_dict[time]
            else:
                if time in list_signal_time:
                    new_signal[time] = op(first_signal.time_values_dict[time], second_signal.time_values_dict[time])
                else:
                    index = next(x for x, val in enumerate(list_signal_time) if val > time)
                    percentage = (time - list_signal_time[index - 1]) / (
                            list_signal_time[index] - list_signal_time[index - 1])
                    temp = second_signal.time_values_dict[index - 1] + (
                            second_signal.time_values_dict[index] - second_signal.time_values_dict[
                        index - 1]) * percentage
                    new_signal[time] = op(first_signal.time_values_dict[time], temp)
        new_signal_data = SignalData(start_time=first_signal.start_time, end_time=first_signal.end_time,
                                     is_signal=first_signal.is_signal, delta=first_signal.delta,
                                     is_new=False, T=first_signal.T, time_values_dict=new_signal,
                                     is_real=first_signal.is_real)
        return new_signal_data

    @staticmethod
    def __add_signals(a, b):
        return a + b

    @staticmethod
    def __sub_signals(a, b):
        return a - b

    @staticmethod
    def __mul_signals(a, b):
        return a * b

    @staticmethod
    def __div_signals(a, b):
        if b == 0:
            return 0
        return a / b
