n = int(input("Nhập n: "))

if n < 0:
    print("Nhập lại số không âm!")
else:
    a, b = 0, 1   # F0 = 0, F1 = 1
    i = 2

    if n == 0:
        print("Fibonacci thứ 0 là:", 0)
    elif n == 1:
        print("Fibonacci thứ 1 là:", 1)
    else:
        while i <= n:
            a, b = b, a + b
            i += 1
        
        print("Fibonacci thứ", n, "là:", b)