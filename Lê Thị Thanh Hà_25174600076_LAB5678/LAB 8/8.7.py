def sumDivisors(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total


def isAmicable(a, b):
    return sumDivisors(a) == b and sumDivisors(b) == a


a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

if isAmicable(a, b):
    print("Hai số là Amicable")
else:
    print("Hai số không phải Amicable")
