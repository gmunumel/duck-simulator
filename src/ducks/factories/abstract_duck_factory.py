import abc


class AbstractDuckFactory(abc.ABC):
    @abc.abstractmethod
    def create_mallard_duck(self):
        pass

    @abc.abstractmethod
    def create_redhead_duck(self):
        pass

    @abc.abstractmethod
    def create_duck_call(self):
        pass

    @abc.abstractmethod
    def create_rubber_duck(self):
        pass
