from Impulse.Impulse import Impulse
import random


class ImpulseNoise(Impulse):
    p: float
    A: float

    def __init__(self):
        super().__init__()
        self.p = 0.1
        self.A = 1

    def generate_values(self, x: float):
        return self.A if random.random() <= self.p else 0
