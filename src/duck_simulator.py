from src.geese.goose_adapter import GooseAdapter
from src.geese.goose import Goose
from src.ducks.decorators.quack_counter import QuackCounter
from src.ducks.factories.counting_duck_factory import CountingDuckFactory
from src.ducks.factories.abstract_duck_factory import AbstractDuckFactory
from src.ducks.quackable import Quackable
from src.ducks.flock import Flock
from src.ducks.observer.quackologist import Quackologist
from src.log import logger


class DuckSimulator:
    def __init__(self):
        duck_factory = CountingDuckFactory()
        self.simulate(duck_factory)

    def simulate(self, duck_factory: AbstractDuckFactory):
        logger.info("Duck Simulator: With Observer")

        flock_of_ducks: Flock = Flock()
        red_head_duck: Quackable = duck_factory.create_redhead_duck()
        duck_call: Quackable = duck_factory.create_duck_call()
        rubber_duck: Quackable = duck_factory.create_rubber_duck()
        goose_duck: Quackable = GooseAdapter(Goose())
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

        quackologist: Quackologist = Quackologist()
        flock_of_ducks.register_observer(quackologist)

        self.simulate_quack(flock_of_ducks)
        # self.simulate_quack(flock_of_mallards)

        logger.info("The ducks quacked %d times", QuackCounter.get_quacks())

    def simulate_quack(self, duck):
        duck.quack()
