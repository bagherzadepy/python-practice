
# لیست نمرات
grades = [12, 18, 9, 20, 15]

# بالاترین نمره
highest = max(grades)

# پایین ترین نمره
lowest = min(grades)

# معدل
average = sum(grades) / len(grades)

# شمارش قبولی و مردودی
passed = 0
failed = 0
for g in grades:
    if g >= 10:
        passed += 1
    else:
        failed += 1

print("Highest grade:", highest)
print("Lowest grade:", lowest)
print("Average:", average)
print("Number of passed:", passed)
print("Number of failed:", failed)
