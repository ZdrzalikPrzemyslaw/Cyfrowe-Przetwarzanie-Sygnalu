from Signal.Signal import Signal
import math


class SinusoidalSignal(Signal):
    T: float
    A: float

    def __init__(self, amplitude: float = 1, term: float = 1):
        super().__init__()
        self.A = amplitude
        self.T = term

    def generate_value(self, x: float):
        return self.A * math.sin(x)
