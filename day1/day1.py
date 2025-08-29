# Day 1 - Python Basics Practice
# Developer: Amir
# Comment: Python Basic Practice (list, dict, function)

# -----------------------------------------------------
# تمرین 1: کار با لیست قیمت کالاها
# -----------------------------------------------------

prices = [12000, 48000, 284000, 18000, 108000, 34000]
total_prices = sum(prices) # جمع
average_prices = total_prices / len(prices) # میانگین
max_price = max(prices) # بیشترین قیمت

print("Prices:", prices)
print("Total:", total_prices)
print("Maximum Prices:", max_price)


# -----------------------------------------------------
# تمرین 2: دیکشنری اطلاعات شخصی
# -----------------------------------------------------

person = {
    "name": "Amir",
    "age": 27,
    "job": "Developer",
    "city": "Tehran"
}

print("\n Initialize Information:", person)

person["age"] = 37 # تغییر مقدار
print("\n Information after change:", person)


# -----------------------------------------------------
# تمرین 3: تابع پیدا کردن بزرگترین عدد
# -----------------------------------------------------

def find_max(*numbers):
    """ تابعی که بزرگترین عدد بین اعداد ارسالی را برمی گرداند"""
    return max(numbers)


print("\n Maximum Number:", find_max(13, 29, 14, 26))
