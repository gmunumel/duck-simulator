import abc


class Quackable(abc.ABC):
    @abc.abstractmethod
    def quack(self):
        pass
