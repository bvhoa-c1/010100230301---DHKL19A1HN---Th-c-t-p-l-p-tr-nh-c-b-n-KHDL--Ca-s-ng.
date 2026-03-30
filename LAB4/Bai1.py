n = int(input("Nhập n: "))
a, b = 0, 1
i = 0
while i < n:
    print(a, end=' ')
    a, b = b, a + b
    i += 1
print()
