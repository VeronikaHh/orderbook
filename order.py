from constants import Side

class Order:
    def __init__(self, user_id: int, amount: float, price: float, side: Side) -> None:
        self.user_id = user_id
        self.amount = amount
        self.price = price
        self.side = side

    def __str__(self) -> str:
        return f'Order(user_id={self.user_id}, amount={self.amount}, price={self.price}, side={self.side.value})'
