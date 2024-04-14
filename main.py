import logging
from orderbook import OrderBook
from order import Order

def main() -> None:
    order_book = OrderBook()
    order_book.add_order(Order(1, 100, 0.025, 'sell'))
    order_book.add_order(Order(2, 50, 0.026, 'buy'))
    print(str(order_book))
    order_book.match_orders()
    print(str(order_book))
    balance_changes = order_book.get_balance_changes()
    for change in balance_changes:
        print(change)
        print(str(order_book))

if __name__ == "__main__":
    main()
