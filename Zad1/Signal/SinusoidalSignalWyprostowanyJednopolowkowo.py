from Signal.SinusoidalSignal import SinusoidalSignal
import math


class SinusoidalSignalWyprosowanyJednopolowkowo(SinusoidalSignal):

    def __init__(self):
        super().__init__()

    def signal(self, x: float):
        return 0.5 * self.A * (math.sin(x) + math.fabs(math.sin(x)))
