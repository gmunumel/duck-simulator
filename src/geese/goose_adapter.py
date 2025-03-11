from src.interfaces.quackable import Quackable
from src.geese.goose import Goose


class GooseAdapter(Quackable):
    def __init__(self, goose: Goose):
        self.goose = goose

    def quack(self):
        self.goose.honk()
