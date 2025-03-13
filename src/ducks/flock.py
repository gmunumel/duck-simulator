from typing import List

from src.ducks.quackable import Quackable


class Flock(Quackable):
    def __init__(self):
        self.quackers: List[Quackable] = []

    def add(self, quacker: Quackable):
        self.quackers.append(quacker)

    def quack(self):
        iterator = iter(self.quackers)
        while True:
            try:
                quacker: Quackable = next(iterator)
                quacker.quack()
            except StopIteration:
                break
