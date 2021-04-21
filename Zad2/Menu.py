import datetime
import os
from typing import Union

from SingalsAndImpulses.Impulse.ImpulseNoise import ImpulseNoise
from SingalsAndImpulses.Impulse.SingularImpulse import SingularImpulse
from SingalsAndImpulses.Signal.GaussianNoise import GaussianNoise
from SingalsAndImpulses.Signal.RectangularSignal import RectangularSignal
from SingalsAndImpulses.Signal.RectangularSymmetricalSignal import RectangularSymmetricalSignal
from SingalsAndImpulses.Signal.SingularJump import SingularJump
from SingalsAndImpulses.Signal.SinusoidalSignal import SinusoidalSignal
from SingalsAndImpulses.Signal.SinusoidalSignalWyprostowanyDwupolowkowo import SinusoidalSignalWyprostowanyDwupolowkowo
from SingalsAndImpulses.Signal.SinusoidalSignalWyprostowanyJednopolowkowo import \
    SinusoidalSignalWyprosowanyJednopolowkowo
from SingalsAndImpulses.Signal.TriangleSignal import TriangleSignal
from SingalsAndImpulses.Signal.UniformlyDistributedNoise import UniformlyDistributedNoise
from SingalsAndImpulses.SignalAndImpulse import SignalAndImpulse
from SingalsAndImpulses.SignalAndImpulseCreator import SignalData
from global_vars import signals

EXIT_PROGRAM = 7


def choose_mode():
    i = -1
    while i not in [1, 2, 3, 4, 5, 6, EXIT_PROGRAM]:
        print("1. Generacja sygnału/szumu/impulsu \n"
              "2. Odczyt z pliku binarnego \n"
              "3. Operacje na sygnałach \n"
              "4. Wyswietl sygnały znajdujące się w pamięci progamu \n"
              "5. Probkowanie, Kwantyzacja, Rekonstrukcja \n" +
              "6. Porównanie \n" +
              str(EXIT_PROGRAM) + ". Wylacz program")
        try:
            i = int(input())
        except ValueError:
            print("zly input")
            pass
    return i




def program_loop():
    choice = -1
    while choice != EXIT_PROGRAM:
        choice = choose_mode()
        if choice == 1:
            signal_data = wybor_1()
            signal_data.plot()
            signals[datetime.datetime.now().isoformat()] = signal_data
            signal_data.print_information()
            ch = 'x'
            while ch not in ['y', 'n']:
                ch = input("Czy chcesz zachować plik sygnału? [y/n]")
                if ch not in ['y', 'n']:
                    print("Invalid character")
                elif ch == 'y':
                    signal_data.save_file()
        elif choice == 2:
            wybor_2()
        elif choice == 3:
            wybor_3()
        elif choice == 4:
            wybor_4()
        elif choice == 5:
            wybor_5()
        elif choice == 6:
            wybor_6()


def wybor_1() -> Union[None, SignalData]:
    choice = -1
    print("Wybierz rodzaj sygnału / szumu / impulsu: \n"
          "1.  Szum o rozkładzie jednostajnym \n"
          "2.  Szum gaussowski \n"
          "3.  Sygnał sinusoidalny \n"
          "4.  Sygnał sinusoidalny wyprostowany jednopołówkowo\n"
          "5.  Sygnał sinusoidalny wyprostowany dwupołówkowo\n"
          "6.  Sygnał prostokątny\n"
          "7.  Sygnał prostokątny symetryczny\n"
          "8.  Sygnał trójkątny\n"
          "9.  Skok jednostkowy\n"
          "10. Impuls jednostkowy\n"
          "11. Szum impulsowy\n"
          )
    try:
        choice = int(input())
    except ValueError:
        print("zly input")
        pass
    if choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        # fixme:
        print("Zły wybór : (")
        return
    beg_time = 0
    duration = 10
    print("Podaj czas początkowy")
    try:
        beg_time = float(input())
    except ValueError:
        print("zly input")
        pass
    print("Podaj czas trwania")
    try:
        duration = float(input())
    except ValueError:
        print("zly input")
        pass
    signal_impulse = SignalAndImpulse()
    print("Podaj amplitudę")
    amplitude = 1
    try:
        inp = float(input())
        if 0 <= inp:
            amplitude = inp
        else:
            raise ValueError
    except ValueError:
        print("zly input")
        pass

    if choice == 1:
        signal_impulse = UniformlyDistributedNoise(amplitude)
        pass

    if choice == 2:
        signal_impulse = GaussianNoise(amplitude)
        pass

    if choice == 3:
        signal_impulse = SinusoidalSignal(amplitude, get_term())
        pass

    if choice == 4:
        signal_impulse = SinusoidalSignalWyprosowanyJednopolowkowo(amplitude, get_term())
        pass

    if choice == 5:
        signal_impulse = SinusoidalSignalWyprostowanyDwupolowkowo(amplitude, get_term())
        pass

    if choice == 6:
        signal_impulse = RectangularSignal(amplitude, get_term(), get_kw())
        pass

    if choice == 7:
        signal_impulse = RectangularSymmetricalSignal(amplitude, get_term(), get_kw())
        pass

    if choice == 8:
        signal_impulse = TriangleSignal(amplitude, get_term(), get_kw())
        pass

    if choice == 9:
        signal_impulse = SingularJump(amplitude, get_ts())
        pass

    # todo poprawić, 3 razy to samo

    if choice == 10:
        signal_impulse = SingularImpulse(amplitude)
        print("Podaj częstotliwość próbkowania")
        try:
            inp = float(input())
            if inp == 0:
                delta_time = 1
                raise ValueError
            delta_time = 1 / inp
        except ValueError:
            print("zly input")
            pass

    if choice == 11:
        signal_impulse = ImpulseNoise(amplitude, get_probability())
        print("Podaj częstotliwość próbkowania")
        try:
            inp = float(input())
            if inp == 0:
                delta_time = 1
                raise ValueError
            delta_time = 1 / inp
        except ValueError:
            print("zly input")
            pass
        pass
    if 'delta_time' in locals():
        return SignalData(signal_and_impulse=signal_impulse, start_time=beg_time, end_time=beg_time + duration,
                          delta=delta_time)
    else:
        return SignalData(signal_and_impulse=signal_impulse, start_time=beg_time, end_time=beg_time + duration)


def get_kw():
    kw = 0.5
    print("Podaj współczynnik wypełnienia")
    try:
        inp = float(input())
        if 0 <= inp <= 1:
            kw = inp
        else:
            raise ValueError
    except ValueError:
        print("zly input wsp. wypełnienia")
        pass
    return kw


def get_ts():
    ts = 0
    print("Podaj czas skoku jednostkowego")
    try:
        inp = float(input())
        if 0 <= inp:
            ts = inp
        else:
            raise ValueError
    except ValueError:
        print("zly input")
        pass
    return ts


def get_probability():
    ts = 0.1
    print("Podaj prawdopodobieństwo wystąpienia wartości amplitudy")
    try:
        inp = float(input())
        if 0 <= inp <= 1:
            ts = inp
        else:
            raise ValueError
    except ValueError:
        print("zly input")
        pass
    return ts


def get_term():
    term = 1
    print("Podaj okres")
    try:
        inp = float(input())
        if 0 <= inp:
            term = inp
        else:
            raise ValueError
    except ValueError:
        print("zly input")
        pass
    return term


def wybor_2():
    print("Podaj sciezke pliku: ")
    try:
        inp = input()
        if os.path.isfile(inp):
            signal = SignalData.load_file(inp)
            signal.plot()
        else:
            raise ValueError
    except ValueError:
        print("zly input")
        pass


def wybor_3():
    while True:
        print("Podaj sciezke pierwszego pliku: ")
        try:
            inp = input()
            if os.path.isfile(inp):
                first_signal = SignalData.load_file(inp)
                break
            else:
                raise ValueError
        except ValueError:
            print("zly input")
            pass

    while True:
        print("Podaj sciezke drugiego pliku: ")
        try:
            inp = input()
            if os.path.isfile(inp):
                second_signal = SignalData.load_file(inp)
                break
            else:
                raise ValueError
        except ValueError:
            print("zly input")
            pass
    i = 0
    while i not in [1, 2, 3, 4]:
        print("1. Dodawanie \n"
              "2. Odejmowanie \n"
              "3. Mnożenie \n"
              "4. Dzielenie \n")
        try:
            i = int(input())
        except ValueError:
            print("zly input")
            pass

    operations = ["add", "sub", "mul", "div"]
    first_signal.operation(second_signal, operations[i - 1])


def wybor_4():
    print(signals)


def wybor_5():
    while True:
        print("Podaj sciezke pliku: ")
        try:
            inp = input()
            if os.path.isfile(inp):
                input_signal = SignalData.load_file(inp)
                break
            else:
                raise ValueError
        except ValueError:
            print("zly input")
            pass
    i = 0
    while i not in [1, 2, 3, 4]:
        print("1. Probkowanie \n"
              "2. Kwantyzacja \n"
              "3. Rekonstrukcja \n")
        try:
            i = int(input())
        except ValueError:
            print("zly input")
            pass

    operations = ["sampling", "quantization", "reconstruction"]
    input_signal.operation_on_one_signal(operation=operations[i - 1])


def wybor_6():
    while True:
        print("Podaj sciezke pliku z wygenerowanym sygnalem: ")
        try:
            inp = input()
            if os.path.isfile(inp):
                input_signal_1 = SignalData.load_file(inp)
                break
            else:
                raise ValueError
        except ValueError:
            print("zly input")
            pass
    i = 0
    while True:
        print("Podaj sciezke pliku z zrekonstruowanym sygnalem: ")
        try:
            inp = input()
            if os.path.isfile(inp):
                input_signal_2 = SignalData.load_file(inp)
                break
            else:
                raise ValueError
        except ValueError:
            print("zly input")
            pass
    i = 0
    input_signal_1.compare_signals(input_signal_2)
