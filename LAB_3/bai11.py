# Bài 11: In ra n số Fibonacci đầu tiên bằng vòng lặp for

n = int(input("Nhập n: "))
if n == 0:
    print("Không có số nào")
else:
    fib1, fib2 = 0, 1
    print(fib1, end=" ")
    if n > 1:
        print(fib2, end=" ")
    for i in range(2, n):
        fib_next = fib1 + fib2
        print(fib_next, end=" ")
        fib1, fib2 = fib2, fib_next
    print()
