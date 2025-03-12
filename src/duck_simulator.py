from src.geese.goose_adapter import GooseAdapter
from src.geese.goose import Goose
from src.ducks.quack_counter import QuackCounter
from src.ducks.counting_duck_factory import CountingDuckFactory
from src.ducks.abstract_duck_factory import AbstractDuckFactory
from src.log import logger


class DuckSimulator:
    def __init__(self):
        duck_factory = CountingDuckFactory()
        self.simulate(duck_factory)

    def simulate(self, duck_factory: AbstractDuckFactory):
        mallard_duck = duck_factory.create_mallard_duck()
        red_head_duck = duck_factory.create_redhead_duck()
        duck_call = duck_factory.create_duck_call()
        rubber_duck = duck_factory.create_rubber_duck()
        goose_duck = GooseAdapter(Goose())

        logger.info("Duck Simulator: With Abstract Factory")

        self.simulate_quack(mallard_duck)
        self.simulate_quack(red_head_duck)
        self.simulate_quack(duck_call)
        self.simulate_quack(rubber_duck)
        self.simulate_quack(goose_duck)

        logger.info("The ducks quacked %d times", QuackCounter.get_quacks())

    def simulate_quack(self, duck):
        duck.quack()
