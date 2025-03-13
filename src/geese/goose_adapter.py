from src.ducks.quackable import Quackable
from src.ducks.observer.observer import Observer
from src.ducks.observer.observable import Observable
from src.geese.goose import Goose


class GooseAdapter(Quackable):
    def __init__(self, goose: Goose):
        self.goose: Goose = goose
        self.observable: Observable = Observable(self)

    def quack(self):
        self.goose.honk()

    def register_observer(self, observer: Observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        # self.observable.notify_observers()
        pass
