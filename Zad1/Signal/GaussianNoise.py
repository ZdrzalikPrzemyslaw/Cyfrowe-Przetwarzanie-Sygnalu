import random
from Signal import Signal


class GaussianNoise(Signal):
    ns: int
    p: float
    A: float

    def __init__(self):
        super().__init__()
        self.A = 1

    def signal(self, x):
        return random.gauss(0, 1) * 2 * self.A - self.A
