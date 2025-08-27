# دیکشنری کالاها و قیمت ها
products = {
    "apple": 10,
    "banana": 5,
    "milk": 15
}

total = 0

while True:
    item = input("What product do you want?('exit' to exit) ")
    if item == "exit":
        break

    if item in products:
        count = int(input("How many? "))
        total += products[item] * count
        print(f"{count} {item} added to cart")
    else:
        print("This product is not available")

print("Your total purchase:", total)