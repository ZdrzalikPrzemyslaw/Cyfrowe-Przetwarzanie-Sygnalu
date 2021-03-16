from Signal import Signal
import math


class SinusoidalSignal(Signal):
    T: float
    A: float

    def __init__(self):
        super().__init__()
        self.A = 1
        self.T = 1

    def generate_value(self, x: float):
        return self.A * math.sin(x)
