# Nhập số n từ bàn phím
n = int(input("Nhập số n: "))


if n <= 1:
    print(f"Số {n} không có ước số thỏa mãn yêu cầu.")
else:
    
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            print(f"Ước số lớn nhất của {n} (khác {n}) là: {i}")
            break 