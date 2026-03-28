n = int(input("Nhập n: "))
if n <= 1:
    print(0)
elif n == 2:
    print(1)
else:
    a = 0
    b = 1
    i = 2
    while i < n:
        c = a + b
        a = b
        b = c
        i += 1
    print(b)