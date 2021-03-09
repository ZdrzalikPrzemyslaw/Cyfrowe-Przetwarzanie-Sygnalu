# This is a sample Python script.
import matplotlib.pyplot as plt
from Signal import Signal
from SingularJump import SingularJump
from RectangularSignal import RectangularSignal
from RectangularSymmetricalSignal import RectangularSymmetricalSignal
from SinusoidalSignal import SinusoidalSignal
from SinusoidalSignalWyprostowanyDwupolowkowo import SinusoidalSignalWyprostowanyDwupolowkowo
from SinusoidalSignalWyprostowanyJednopolowkowo import SinusoidalSignalWyprosowanyJednopolowkowo


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(signal: Signal):
    plt.plot([x / 100 for x in range(-1000, 1000)], [signal.signal(x / 100) for x in range(-1000, 1000)])
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(SingularJump())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
