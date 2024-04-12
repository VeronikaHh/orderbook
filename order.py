
class Order:
    def __init__(self, user_id, amount, price, side):
        self.user_id = user_id
        self.amount = amount
        self.price = price
        self.side = side

    def __str__(self):
        return f'Order(user_id={self.user_id}, amount={self.amount}, price={self.price}, side={self.side})'
