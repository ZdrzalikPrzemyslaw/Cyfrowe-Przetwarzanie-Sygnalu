from SingalsAndImpulses.Signal.RectangularSignal import RectangularSignal


class RectangularSymmetricalSignal(RectangularSignal):
    def __init__(self, amplitude: float = 1, term: float = 1, kw: float = 0.5):
        super().__init__(amplitude, term, kw)

    def generate_value(self, x: float):
        x = x % self.T
        return self.A if x < self.T * self.kw else -self.A
