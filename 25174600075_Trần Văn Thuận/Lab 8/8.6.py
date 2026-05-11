def sumpdivisors(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong
n = int(input("Nhập số: "))
print("Tổng các ước thực sự:", sumpdivisors(n))