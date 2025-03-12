from src.ducks.abstract_duck_factory import AbstractDuckFactory
from src.ducks.quack_counter import QuackCounter
from src.ducks.mallard_duck import MallardDuck
from src.ducks.redhead_duck import RedheadDuck
from src.ducks.duck_call import DuckCall
from src.ducks.rubber_duck import RubberDuck


class CountingDuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self):
        return QuackCounter(MallardDuck())

    def create_redhead_duck(self):
        return QuackCounter(RedheadDuck())

    def create_duck_call(self):
        return QuackCounter(DuckCall())

    def create_rubber_duck(self):
        return QuackCounter(RubberDuck())
