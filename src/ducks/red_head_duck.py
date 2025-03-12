from src.ducks.quackable import Quackable
from src.log import logger


class RedHeadDuck(Quackable):
    def quack(self):
        logger.info("Quack")
