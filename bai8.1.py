# Xây dựng hàm kiểm tra số nguyên tố độc lập
# Xuất các số nguyên tố nhỏ hơn 1000

# Hàm kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

# Quét và xuất các số nguyên tố nhỏ hơn 1000
print("Cac so nguyen to nho hon 1000:")

for i in range(1000):
    if kiem_tra_so_nguyen_to(i):
        print(i, end=" ")