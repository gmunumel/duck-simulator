from src.ducks.quackable import Quackable
from src.log import logger


class DuckCall(Quackable):
    def quack(self):
        logger.info("Kwak")
