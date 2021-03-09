from Impulse import Impulse


class SingularImpulse(Impulse):
    ns: int

    def __init__(self):
        super().__init__()
        self.ns = 0

    def impulse(self, x: float):
        return 1 if x == self.ns else 0
