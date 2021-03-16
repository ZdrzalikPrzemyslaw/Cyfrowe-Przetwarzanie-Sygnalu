from Signal.SinusoidalSignal import SinusoidalSignal
import math


class SinusoidalSignalWyprostowanyDwupolowkowo(SinusoidalSignal):
    A: float

    def __init__(self, amplitude: float = 1, term: float = 1):
        super().__init__(amplitude, term)

    def generate_value(self, x: float):
        return self.A * math.fabs(math.sin(x/self.T))
