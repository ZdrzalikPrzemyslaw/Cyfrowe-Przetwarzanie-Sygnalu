from Signal import Signal


class TriangleSignal(Signal):
    T: float
    A: float
    kw: float

    def __init__(self):
        super().__init__()
        self.A = 1
        self.T = 2
        self.kw = 0.5

    def generate_value(self, x: float):
        x = x % self.T
        return (self.A / (self.kw * self.T)) * x if x < self.T * self.kw \
            else - self.A / (self.T * (1 - self.kw)) * x + (self.A / (1 - self.kw))
