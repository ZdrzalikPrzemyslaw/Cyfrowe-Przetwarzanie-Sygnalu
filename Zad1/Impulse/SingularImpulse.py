from Impulse.Impulse import Impulse


class SingularImpulse(Impulse):
    A: float

    def __init__(self, amplitude: float = 1):
        super().__init__()
        self.A = amplitude

    def generate_value(self, x: float):
        #TODO: zrobic tutaj to ns bo to musi byc opisane wzorem
        return self.A if x == self.ns else 0
