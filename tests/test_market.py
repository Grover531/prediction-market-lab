import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.market import Market


def test_market_creation():

    market = Market(
        id="123",
        title="Will it rain tomorrow?",
        price=0.62,
        volume=25000
    )
    # Assertions
    assert market.id == "123"
    assert market.title == "Will it rain tomorrow?"
    assert market.price == 0.62
    assert market.volume == 25000
    
def test_market_string_representation():
    market = Market(
        id="123",
        title="Will it rain tomorrow?",
        price=0.62,
        volume=25000
    )
    assert str(market) == "Will it rain tomorrow? (0.62)"