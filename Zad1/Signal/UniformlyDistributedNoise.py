import random
from Signal import Signal


class UniformlyDistributedNoise(Signal):
    ns: int
    p: float
    A: float

    def __init__(self):
        super().__init__()
        self.A = 1

    def generate_value(self, x):
        return random.random() * 2 * self.A - self.A
