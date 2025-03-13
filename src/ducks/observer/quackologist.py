from src.ducks.observer.observer import Observer
from src.ducks.observer.quack_observable import QuackObservable
from src.log import logger


class Quackologist(Observer):
    def update(self, duck: QuackObservable):
        logger.info("Quackologist: %s just quacked", duck)
