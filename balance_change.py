from constants import Currency

class BalanceChange:
    def __init__(self, user_id: int, value: float, currency: Currency) -> None:
        self.user_id = user_id
        self.value = value
        self.currency = currency

    def __str__(self) -> str:
        return f'BalanceChange(user_id={self.user_id}, value={self.value}, currency={self.currency.value})'