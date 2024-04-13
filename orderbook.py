import heapq
from balance_change import BalanceChange

class OrderBook:
    def __init__(self):
        self.sell_orders = []
        self.buy_orders = []

    def add_order(self, order):
        if order.side == 'sell':
            self.sell_orders.append(order)
            self.sell_orders.sort(key=lambda x: x.price)
        else:
            self.buy_orders.append(order)
            self.buy_orders.sort(key=lambda x: x.price, reverse=True)

    def match_orders(self):
        while self.sell_orders and self.buy_orders:
            top_sell = self.sell_orders[0]
            top_buy = self.buy_orders[0]
            if top_sell.price > top_buy.price:
                break
            sell_amount = top_sell.amount
            buy_amount = top_buy.amount
            if sell_amount == buy_amount:
                self.sell_orders.pop(0)
                self.buy_orders.pop(0)
            elif sell_amount < buy_amount:
                top_buy.amount -= sell_amount
                self.sell_orders.pop(0)
            else:
                top_sell.amount -= buy_amount
                self.buy_orders.pop(0)

    def get_balance_changes(self):
        balance_changes = []
        for order in self.sell_orders:
            balance_changes.append(BalanceChange(order.user_id, -order.amount, 'UAH'))
            balance_changes.append(BalanceChange(order.user_id, order.amount*order.price, 'USD'))
        for order in self.buy_orders:
            balance_changes.append(BalanceChange(order.user_id, order.amount, 'UAH'))
            balance_changes.append(BalanceChange(order.user_id, -order.amount*order.price, 'USD'))
        return balance_changes

    def __str__(self):
        sell_str = 'Sell orders:\n'
        for order in self.sell_orders:
            sell_str += f'  {order}\n'
        buy_str = 'Buy orders:\n'
        for order in self.buy_orders:
            buy_str += f'  {order}\n'
        return f'Order book:\n{sell_str}{buy_str}'
