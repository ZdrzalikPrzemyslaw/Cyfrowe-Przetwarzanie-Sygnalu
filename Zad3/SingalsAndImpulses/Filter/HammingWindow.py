import math

from SingalsAndImpulses.Filter.Window import Window


class HammingWindow(Window):
    def __init__(self, M: int):
        super().__init__(M)

    def value(self, n):
        return 0.53836 - 0.46164 * math.cos(2 * math.pi * n / self.M)
