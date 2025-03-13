from src.ducks.factories.abstract_duck_factory import AbstractDuckFactory
from src.ducks.mallard_duck import MallardDuck
from src.ducks.redhead_duck import RedheadDuck
from src.ducks.duck_call import DuckCall
from src.ducks.rubber_duck import RubberDuck


class DuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self):
        return MallardDuck()

    def create_redhead_duck(self):
        return RedheadDuck()

    def create_duck_call(self):
        return DuckCall()

    def create_rubber_duck(self):
        return RubberDuck()
