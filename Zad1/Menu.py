from Impulse.ImpulseNoise import ImpulseNoise
from Impulse.SingularImpulse import SingularImpulse
from Signal.GaussianNoise import GaussianNoise
from Signal.RectangularSignal import RectangularSignal
from Signal.RectangularSymmetricalSignal import RectangularSymmetricalSignal
from Signal.SingularJump import SingularJump
from Signal.SinusoidalSignal import SinusoidalSignal
from Signal.SinusoidalSignalWyprostowanyDwupolowkowo import SinusoidalSignalWyprostowanyDwupolowkowo
from Signal.SinusoidalSignalWyprostowanyJednopolowkowo import SinusoidalSignalWyprosowanyJednopolowkowo
from Signal.TriangleSignal import TriangleSignal
from Signal.UniformlyDistributedNoise import UniformlyDistributedNoise
from SignalAndImpulse import SignalAndImpulse
from SignalAndImpulseCreator import SignalData
from plot import plot


def choose_mode():
    i = -1
    while i not in [1, 2, 3, 4]:
        print("1. Generacja sygnału/szumu/impulsu \n"
              "2. Odczyt z pliku binarnego \n"
              "3. Operacje na sygnałach \n"
              "4. Wylacz program")
        try:
            i = int(input())
        except ValueError:
            print("zly input")
            pass
    return i


def program_loop():
    choice = -1
    while choice != 5:
        choice = choose_mode()
        if choice == 1:
            plot(wybor_1())
        elif choice == 2:
            wybor_2()
        elif choice == 3:
            wybor_3()
        elif choice == 4:
            wybor_4()


def wybor_1():
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
    delta_time = 0.05
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
        print("JESTEM TU")
        signal_impulse = ImpulseNoise(amplitude, get_probability())
        print("Podaj częstotliwość próbkowania")
        try:
            inp = float(input())
            if inp == 0 :
                delta_time = 1
                raise ValueError
            delta_time = 1 / inp
        except ValueError:
            print("zly input")
            pass
        pass

    return SignalData(signal_impulse, beg_time, beg_time + duration, delta_time)


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
    pass


def wybor_3():
    pass


def wybor_4():
    exit()
