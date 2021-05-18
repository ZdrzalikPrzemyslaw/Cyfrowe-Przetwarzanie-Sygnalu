from SingalsAndImpulses.Filter.Window import Window


class RectangularWindow(Window):
    def __init__(self, M: int):
        super().__init__(M)

    def value(self, n):
        return 1