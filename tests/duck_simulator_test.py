import logging

from collections import Counter

from src.duck_simulator import DuckSimulator
from src.ducks.decorators.quack_counter import QuackCounter


def test_duck_simulator(caplog):
    caplog.set_level(logging.INFO)
    DuckSimulator()
    assert "Duck Simulator" in caplog.text
    assert "Quack" in caplog.text
    assert "Kwak" in caplog.text
    assert "Squeak" in caplog.text
    assert "Honk" in caplog.text
    message_counts = Counter(message for _, _, message in caplog.record_tuples)
    assert message_counts["Quack"] == 5
    assert QuackCounter.get_quacks() == 7
