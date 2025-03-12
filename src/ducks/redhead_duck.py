from src.ducks.quackable import Quackable
from src.log import logger


class RedheadDuck(Quackable):
    def quack(self):
        logger.info("Quack")
