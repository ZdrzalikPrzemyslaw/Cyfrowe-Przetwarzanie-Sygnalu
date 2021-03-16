import random
from Signal.Signal import Signal


class GaussianNoise(Signal):
    A: float

    def __init__(self, amplitude: float = 1):
        super().__init__()
        self.A = amplitude

    def generate_value(self, x):
        return random.gauss(0, 1) * 2 * self.A - self.A
