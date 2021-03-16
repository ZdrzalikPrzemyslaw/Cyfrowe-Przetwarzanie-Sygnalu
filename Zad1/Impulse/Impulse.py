from SignalAndImpulse import SignalAndImpulse


class Impulse(SignalAndImpulse):
    def __init__(self):
        super().__init__()

    def generate_values(self, x: float):
        return 1
