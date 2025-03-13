from typing import List, Any

from src.ducks.observer.quack_observable import QuackObservable


class Observable(QuackObservable):
    def __init__(self, duck: QuackObservable):
        self.observers: List[Any] = []
        self.duck: QuackObservable = duck

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.iterate_over(self.observers):
            observer.update(self.duck)
