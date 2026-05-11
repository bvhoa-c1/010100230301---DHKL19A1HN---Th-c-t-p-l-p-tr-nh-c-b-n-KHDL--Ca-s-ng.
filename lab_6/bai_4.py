def fibonacci(k):
    if k < 2:
        return k
    a = 0
    b = 1
    for _ in range(2, k + 1):
        a, b = b, a + b
    return b

n = int(input("n = "))
print([fibonacci(i) for i in range(n)])
