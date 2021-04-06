from SingalsAndImpulses.Signal.SinusoidalSignal import SinusoidalSignal
import math


class SinusoidalSignalWyprosowanyJednopolowkowo(SinusoidalSignal):

    def __init__(self, amplitude: float = 1, term: float = 1):
        super().__init__(amplitude, term)

    def generate_value(self, x: float):
        return 0.5 * self.A * (math.sin(x/self.T * 2 * math.pi) + math.fabs(math.sin(x/self.T * 2 * math.pi)))
