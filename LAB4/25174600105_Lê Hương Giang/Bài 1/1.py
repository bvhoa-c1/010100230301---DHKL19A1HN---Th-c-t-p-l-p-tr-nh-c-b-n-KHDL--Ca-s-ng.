n = int(input("Nhập n: "))

a = 0
b = 1
c = 1

while c < n:
    d = a + b
    a = b
    b = d
    c += 1

print("Số Fibonacci thứ", n, "là:", a)