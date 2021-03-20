from SingalsAndImpulses.Signal.Signal import Signal


class RectangularSignal(Signal):
    T: float
    A: float
    kw: float

    def __init__(self, amplitude: float = 1, term: float = 1, kw: float = 0.5):
        super().__init__()
        self.A = amplitude
        self.T = term
        self.kw = kw

    def generate_value(self, x: float):
        x = x % self.T
        return self.A if x < self.T * self.kw else 0
