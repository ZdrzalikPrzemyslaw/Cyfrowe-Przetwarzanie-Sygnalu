from Impulse.Impulse import Impulse


class SingularImpulse(Impulse):
    ns: int
    A: float

    def __init__(self, amplitude: float = 1, ns: int = 0):
        super().__init__()
        self.ns = ns
        self.A = amplitude

    def generate_values(self, x: float):
        return self.A if x == self.ns else 0
