import abc

from src.ducks.observer.quack_observable import QuackObservable


class Quackable(QuackObservable):
    @abc.abstractmethod
    def quack(self):
        pass
