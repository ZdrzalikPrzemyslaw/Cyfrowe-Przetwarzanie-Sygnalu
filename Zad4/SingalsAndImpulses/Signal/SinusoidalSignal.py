from SingalsAndImpulses.Signal.Signal import Signal
import math


class SinusoidalSignal(Signal):
    T: float
    A: float
    przes: float

    def __init__(self, amplitude: float = 1, term: float = 1, przes: float = 0.0):
        super().__init__()
        self.A = amplitude
        self.T = term
        self.przes = przes

    def generate_value(self, x: float):
        return self.A * math.sin((x * 2 * math.pi / self.T) + self.przes)
