from Signal.RectangularSignal import RectangularSignal
from Signal.Signal import Signal


class TriangleSignal(RectangularSignal):

    def __init__(self, amplitude: float = 1, term: float = 1, kw: float = 0.5):
        super().__init__(amplitude, term, kw)

    def generate_value(self, x: float):
        x = x % self.T
        return (self.A / (self.kw * self.T)) * x if x < self.T * self.kw \
            else - self.A / (self.T * (1 - self.kw)) * x + (self.A / (1 - self.kw))
