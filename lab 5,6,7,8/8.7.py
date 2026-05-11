# Kiểm tra cặp số Amicable

def sumDivisors(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total


def isAmicable(a, b):
    return sumDivisors(a) == b and sumDivisors(b) == a


a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

if isAmicable(a, b):
    print("Là cặp số Amicable")
else:
    print("Không phải cặp số Amicable")