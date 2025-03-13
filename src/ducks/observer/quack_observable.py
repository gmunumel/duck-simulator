import abc


class QuackObservable(abc.ABC):
    @abc.abstractmethod
    def register_observer(self, observer):
        pass

    @abc.abstractmethod
    def notify_observers(self):
        pass

    def iterate_over(self, fields):
        iterator = iter(fields)
        while True:
            try:
                item = next(iterator)
                yield item
            except StopIteration:
                break
