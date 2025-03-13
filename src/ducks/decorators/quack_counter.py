from src.ducks.quackable import Quackable
from src.ducks.observer.observer import Observer


class QuackCounter(Quackable):
    number_of_quacks: int = 0

    def __init__(self, duck: Quackable):
        self.duck: Quackable = duck

    def quack(self):
        self.duck.quack()
        QuackCounter.number_of_quacks += 1

    @classmethod
    def get_quacks(cls):
        return cls.number_of_quacks

    def register_observer(self, observer: Observer):
        self.duck.register_observer(observer)

    def notify_observers(self):
        # self.duck.notify_observers()
        pass
