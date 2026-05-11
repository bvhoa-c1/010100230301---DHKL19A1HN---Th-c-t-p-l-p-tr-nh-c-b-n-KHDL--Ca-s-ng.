def sumDivisors(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total

a = int(input("Nhap so thu nhat: "))
b = int(input("Nhap so thu hai: "))

if sumDivisors(a) == b and sumDivisors(b) == a:
    print("Day la cap so amicable")
else:
    print("Khong phai cap so amicable")