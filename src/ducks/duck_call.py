from src.ducks.quackable import Quackable
from src.ducks.observer.observer import Observer
from src.ducks.observer.observable import Observable
from src.log import logger


class DuckCall(Quackable):
    def __init__(self):
        self.observable: Observable = Observable(self)

    def quack(self):
        logger.info("Kwak")
        self.notify_observers()

    def register_observer(self, observer: Observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()

    def __repr__(self):
        return "Duck Call"
