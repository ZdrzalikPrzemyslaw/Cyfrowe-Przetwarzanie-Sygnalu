from Signal import Signal


class SingularJump(Signal):
    ts: float
    A: float

    def __init__(self):
        super().__init__()
        self.A = 1
        self.ts = 0

    def generate_value(self, x: float):
        if x == self.ts:
            return self.A / 2
        return self.A if x > self.ts else 0
