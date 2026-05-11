def sumPdivisors(n):
    tong = 0

    for i in range(1, n):
        if n % i == 0:
            tong += i

    return tong


n = int(input("Nhap n: "))
print("Tong cac uoc so thuc su =", sumPdivisors(n))