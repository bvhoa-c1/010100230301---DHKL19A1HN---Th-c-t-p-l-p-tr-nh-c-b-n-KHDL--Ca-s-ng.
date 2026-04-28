def in_fibonacci(n):
    fib1 = 0
    fib2 = 1
    i = 0
    while i < n:
        print(fib1,end = " ")
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i += 1
print("10 số fibonacci đầu tiên :")
in_fibonacci(10)