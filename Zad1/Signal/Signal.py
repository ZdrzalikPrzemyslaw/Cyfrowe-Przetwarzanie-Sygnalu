from SignalAndImpulse import SignalAndImpulse


class Signal(SignalAndImpulse):
    def __init__(self):
        super().__init__()

    def generate_value(self, x: float):
        return 1
