from src.ducks.quackable import Quackable
from src.log import logger


class MallardDuck(Quackable):
    def quack(self):
        logger.info("Quack")
