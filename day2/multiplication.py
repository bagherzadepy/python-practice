def multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i} × {j} = {i*j}")
        print("-" * 20) # خط جداکننده بین هر جدول

if __name__ == "__main__":
    multiplication_table(10)
    