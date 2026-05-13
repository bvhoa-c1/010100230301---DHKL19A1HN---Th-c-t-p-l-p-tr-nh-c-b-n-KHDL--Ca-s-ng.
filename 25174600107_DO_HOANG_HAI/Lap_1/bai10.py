n = int(input())
if n <= 0:
    pass
elif n == 1:
    print(0)
else:
    a, b = 0, 1
    print(a, end=' ')
    print(b, end=' ')
    for _ in range(3, n + 1):
        c = a + b
        print(c, end=' ')
        a, b = b, c
