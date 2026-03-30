n = int(input("Nhập n: "))

a, b = 0, 1
print(f"{n} số Fibonacci đầu tiên là:")

for i in range(n):
    print(a, end=" ")
    
    a, b = b, a + b