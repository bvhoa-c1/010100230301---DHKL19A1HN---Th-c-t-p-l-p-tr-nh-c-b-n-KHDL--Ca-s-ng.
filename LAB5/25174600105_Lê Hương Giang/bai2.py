def F(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        print(a,end=" ")
        s = a + b
        a = b
        b = s
        i += 1
print("10 số đầu tiên của Fibonacy")
F(10)
