

prices = [12000, 48000, 284000, 18000, 108000, 34000]
total_prices = sum(prices)
average_prices = total_prices / len(prices)
max_price = max(prices)

person = {
    "name": "Amir",
    "age": 27,
    "accupation": "developer",
    "city": "Tehran"
}
person["age"] = 37

def max_numbers(*numbers):
    return max(numbers)
print(max_numbers(13, 29, 14, 26))
