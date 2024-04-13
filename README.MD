# Orderbook
To run the program you shoud install Python on your PC and then run command:
```console
pip freeze > requirements.txt
pip install -r requirements.txt
```
Then you can run main.py using command:
```console
python main.py
```

# Complexity
The time complexity of adding an order is O(log n) due to sorting, 
and the time complexity of matching orders is O(n) in the worst case, 
where n is the number of orders in the book. Therefore, 
the overall time complexity of this implementation is O(n log n) in the worst case.

# Time spent on solution:
- investigation ~ 1 hour
- implementation ~ 1 hour
