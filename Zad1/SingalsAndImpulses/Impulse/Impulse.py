from SingalsAndImpulses.SignalAndImpulse import SignalAndImpulse


class Impulse(SignalAndImpulse):
    def __init__(self):
        super().__init__()

    def generate_value(self, x: float):
        return 1
