from Signal.UniformlyDistributedNoise import UniformlyDistributedNoise
from SignalAndImpulse import SignalAndImpulse
from SignalAndImpulseCreator import SignalData
from plot import plot


def choose_mode():
    i = -1
    while i not in [1, 2, 3, 4, 5]:
        print("1. Generacja sygnału/szumu/impulsu \n"
              "2. Odczyt z pliku binarnego \n"
              "3. Operacje na sygnałach \n"
              "5. Wylacz program")
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
    end_time = 10
    delta_time = 0.05
    print("Podaj czas początkowy")
    try:
        beg_time = float(input())
    except ValueError:
        print("zly input")
        pass
    print("Podaj czas końcowy")
    try:
        end_time = float(input())
    except ValueError:
        print("zly input")
        pass
    print("Podaj odstęp pomiędzy pomiarami wartości")
    try:
        delta_time = float(input())
    except ValueError:
        print("zly input")
        pass
    signal_impulse = SignalAndImpulse()
    if choice == 1:
        print("Podaj Amplitudę sygnału")
        amplitude = 1
        try:
            amplitude = float(input())
        except ValueError:
            print("zly input")
            pass
        signal_impulse = UniformlyDistributedNoise(amplitude)
        pass
    return SignalData(signal_impulse, beg_time, end_time, delta_time)


def wybor_2():
    pass


def wybor_3():
    pass


def wybor_4():
    pass
