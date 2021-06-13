from SingalsAndImpulses.Impulse.Impulse import Impulse
import random


class ImpulseNoise(Impulse):
    p: float
    A: float

    def __init__(self, amplitude: float = 1, probability: float = 0.5):
        super().__init__()
        self.p = probability
        self.A = amplitude

    def generate_value(self, x: float):
        return self.A if random.random() <= self.p else 0
