from Impulse import Impulse


class SingularImpulse(Impulse):
    ns: int
    A: float

    def __init__(self):
        super().__init__()
        self.ns = 0
        self.A = 1

    def generate_values(self, x: float):
        return self.A if x == self.ns else 0
