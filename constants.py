from enum import Enum

class Currency(Enum):
    UAH: str = 'UAH'
    USD: str = 'USD'

class Side(Enum):
    BUY: str = 'buy'
    SELL: str = 'sell'
