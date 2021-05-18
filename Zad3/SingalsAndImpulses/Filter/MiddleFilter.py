import math

from SingalsAndImpulses.Filter.DownFilter import DownFilter
from SingalsAndImpulses.Filter.Window import Window


class MiddleFilter(DownFilter):
    def __init__(self, window: Window, M: int, fp: float, fo: float):
        super().__init__(window, M, fp, fo)

    def value(self, n):
        return super().value(n) * 2 * math.sin(math.pi * n / 2) * self.window.value(n)
