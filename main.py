from orderbook import OrderBook
from order import Order
from constants import Side

def main() -> None:
    order_book = OrderBook()
    order_book.add_order(Order(user_id=1, amount=100, price=0.025, side=Side.SELL))
    order_book.add_order(Order(user_id=2, amount=50, price=0.026, side=Side.BUY))
    print(str(order_book))
    order_book.match_orders()
    print(str(order_book))
    balance_changes = order_book.get_balance_changes()
    for change in balance_changes:
        print(change)
        print(str(order_book))

if __name__ == "__main__":
    main()
