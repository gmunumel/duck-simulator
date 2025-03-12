from src.ducks.quackable import Quackable


class QuackCounter(Quackable):
    number_of_quacks = 0

    def __init__(self, duck: Quackable):
        self.duck = duck

    def quack(self):
        self.duck.quack()
        QuackCounter.number_of_quacks += 1

    @classmethod
    def get_quacks(cls):
        return cls.number_of_quacks
