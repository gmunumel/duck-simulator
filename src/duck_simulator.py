from src.geese.goose_adapter import GooseAdapter
from src.geese.goose import Goose
from src.ducks.quack_counter import QuackCounter
from src.ducks.counting_duck_factory import CountingDuckFactory
from src.ducks.abstract_duck_factory import AbstractDuckFactory
from src.ducks.quackable import Quackable
from src.ducks.flock import Flock
from src.log import logger


class DuckSimulator:
    def __init__(self):
        duck_factory = CountingDuckFactory()
        self.simulate(duck_factory)

    def simulate(self, duck_factory: AbstractDuckFactory):
        red_head_duck: Quackable = duck_factory.create_redhead_duck()
        duck_call: Quackable = duck_factory.create_duck_call()
        rubber_duck: Quackable = duck_factory.create_rubber_duck()
        goose_duck: Quackable = GooseAdapter(Goose())

        logger.info("Duck Simulator: With Composite - Flocks")

        flock_of_ducks: Flock = Flock()

        flock_of_ducks.add(red_head_duck)
        flock_of_ducks.add(duck_call)
        flock_of_ducks.add(rubber_duck)
        flock_of_ducks.add(goose_duck)

        flock_of_mallards: Flock = Flock()

        mallard_duck_one: Quackable = duck_factory.create_mallard_duck()
        mallard_duck_two: Quackable = duck_factory.create_mallard_duck()
        mallard_duck_three: Quackable = duck_factory.create_mallard_duck()
        mallard_duck_four: Quackable = duck_factory.create_mallard_duck()

        flock_of_mallards.add(mallard_duck_one)
        flock_of_mallards.add(mallard_duck_two)
        flock_of_mallards.add(mallard_duck_three)
        flock_of_mallards.add(mallard_duck_four)

        flock_of_ducks.add(flock_of_mallards)

        logger.info("Duck Simulator: Whole Flock Simulation")
        self.simulate_quack(flock_of_ducks)

        logger.info("Duck Simulator: Mallard Flock Simulation")
        self.simulate_quack(flock_of_mallards)

        logger.info("The ducks quacked %d times", QuackCounter.get_quacks())

    def simulate_quack(self, duck):
        duck.quack()
