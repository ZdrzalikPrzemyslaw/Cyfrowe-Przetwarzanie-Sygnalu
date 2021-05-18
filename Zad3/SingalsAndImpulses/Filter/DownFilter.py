import math

from SingalsAndImpulses.Filter.Window import Window


class DownFilter:
    def __init__(self, window: Window, M: int, fp: float, fo: float):
        self.window = window
        self.M = M
        self.K = fp / fo

    def value(self, n):
        middle_point = (self.M - 1) / 2
        if n == middle_point:
            return 2 / self.K
        return (math.sin(2 * math.pi * (n - middle_point / self.K))
                / (math.pi * (n - middle_point))) * self.window.value(n)
