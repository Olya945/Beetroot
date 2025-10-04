# Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
 
total_price = {}

for fruit in stock:
    total_price[fruit] = stock[fruit] * prices[fruit]

print(total_price)
