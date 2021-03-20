from SingalsAndImpulses.Signal.Signal import Signal


class SingularJump(Signal):
    ts: float
    A: float

    def __init__(self, amplitude: float = 1, ts: float = 0):
        super().__init__()
        self.A = amplitude
        self.ts = ts

    def generate_value(self, x: float):
        if x == self.ts:
            return self.A / 2
        return self.A if x > self.ts else 0
