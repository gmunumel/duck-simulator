from typing import List

from src.ducks.quackable import Quackable
from src.ducks.observer.observer import Observer
from src.ducks.observer.observable import Observable


class Flock(Quackable):
    def __init__(self):
        self.quackers: List[Quackable] = []
        self.observable: Observable = Observable(self)

    def add(self, quacker: Quackable):
        self.quackers.append(quacker)

    def quack(self):
        for quacker in self.iterate_over(self.quackers):
            quacker.quack()

    def register_observer(self, observer: Observer):
        for quacker in self.iterate_over(self.quackers):
            quacker.register_observer(observer)

    def notify_observers(self):
        # self.observable.notify_observers()
        pass
