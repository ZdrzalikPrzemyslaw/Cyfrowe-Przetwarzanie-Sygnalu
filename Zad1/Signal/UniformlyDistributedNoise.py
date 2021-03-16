import random
from Signal.Signal import Signal


class UniformlyDistributedNoise(Signal):
    A: float

    def __init__(self):
        super().__init__()
        self.A = 1

    def generate_value(self, x):
        return random.random() * 2 * self.A - self.A
