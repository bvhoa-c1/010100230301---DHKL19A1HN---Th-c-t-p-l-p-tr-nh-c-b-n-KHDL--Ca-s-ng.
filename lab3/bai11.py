n = int(input("Nhập n: "))
a = 0
b = 1
print(f"{n} số Fibonacci đầu tiên là:")
for i in range(n):
    print(a, end=" ")
    temp = a
    a = b
    b = temp + b