from Signal.SinusoidalSignal import SinusoidalSignal
import math


class SinusoidalSignalWyprostowanyDwupolowkowo(SinusoidalSignal):
    def __init__(self):
        super().__init__()

    def generate_value(self, x: float):
        return self.A * math.fabs(math.sin(x))
