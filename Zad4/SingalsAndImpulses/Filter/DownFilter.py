import math

from SingalsAndImpulses.Filter.Window import Window


class DownFilter:
    def __init__(self, window: Window, M: int, fp: float, fo: float):
        self.window = window
        self.M = M
        self.K = 1 / (fp * fo)
        self.fo = fo
        self.fp = fp

    def generate_value(self, n):
        n = n * 1 / self.fp
        middle_point = (self.M - 1) / 2
        if n == middle_point:
            return (2 / self.K) * self.window.value(n)
        wynik = self.window.value(n) * math.sin(2 * math.pi * (n - middle_point) / self.K) / (math.pi * (n - middle_point))
        print()
        return wynik
