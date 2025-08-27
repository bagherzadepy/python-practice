def analyze_grades():
    highest = max(grades) # بالاترین نمره
    lowest = min(grades) # پایین ترین نمره
    average = sum(grades) / len(grades) # معدل
    # شمارش قبولی و مردودی
    passed = sum(1 for g in grades if g >= 10)
    failed = len(grades) - passed
    return highest, lowest, average, passed, failed # برگرداندن تاپلی از آنالیز نمرات

if __name__ == "__main__":
    # نمونه لیست نمرات
    grades = [12, 18, 9, 20, 15]
    highest, lowest, average, passed, failed = analyze_grades(grades)

    print("Highest grade:", highest)
    print("Lowest grade:", lowest)
    print("Average:", average)
    print("Number of passed:", passed)
    print("Number of failed:", failed)
