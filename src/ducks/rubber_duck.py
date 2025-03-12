from src.ducks.quackable import Quackable
from src.log import logger


class RubberDuck(Quackable):
    def quack(self):
        logger.info("Squeak")
