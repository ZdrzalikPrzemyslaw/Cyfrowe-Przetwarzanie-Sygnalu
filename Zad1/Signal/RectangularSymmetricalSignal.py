from Signal.RectangularSignal import RectangularSignal


class RectangularSymmetricalSignal(RectangularSignal):
    def __init__(self):
        super().__init__()

    def generate_value(self, x: float):
        x = x % self.T
        return self.A if x < self.T * self.kw else -self.A
