from src.ducks.mallard_duck import MallardDuck
from src.ducks.red_head_duck import RedHeadDuck
from src.ducks.duck_call import DuckCall
from src.ducks.rubber_duck import RubberDuck
from src.geese.goose_adapter import GooseAdapter
from src.geese.goose import Goose
from src.log import logger


class DuckSimulator:
    def __init__(self):
        self.simulate()

    def simulate(self):
        mallard_duck = MallardDuck()
        red_head_duck = RedHeadDuck()
        duck_call = DuckCall()
        rubber_duck = RubberDuck()
        goose_duck = GooseAdapter(Goose())

        logger.info("Duck Simulator")

        self.simulate_quack(mallard_duck)
        self.simulate_quack(red_head_duck)
        self.simulate_quack(duck_call)
        self.simulate_quack(rubber_duck)
        self.simulate_quack(goose_duck)

    def simulate_quack(self, duck):
        duck.quack()
