import abc

from src.ducks.observer.quack_observable import QuackObservable


class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self, duck: QuackObservable):
        pass
