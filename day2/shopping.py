def add_to_cart(products, item, count):
    return products[item] * count

def shopping():
    products = {
        "apple": 10,
        "banana": 5,
        "milk": 15
    } # دیکشنری نمونه ای از کالاها و قیمت ها
    total = 0

    while True:
        item = input("What product do you want?('exit' to exit) ")
        if item == "exit":
            break
        if item in products:
            count = int(input("How many? "))
            total += add_to_cart(products, item, count)
            print(f"{count} {item} added to cart")
        else:
            print("This product is not available")

    print("Your total purchase:", total)


if __name__ == "__main__":
    shopping()
