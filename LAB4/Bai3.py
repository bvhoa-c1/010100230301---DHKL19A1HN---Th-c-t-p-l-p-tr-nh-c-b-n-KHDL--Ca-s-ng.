n = int(input("Nhập số n: "))
i = n // 2  # Bắt đầu kiểm tra từ một nửa của n

while i > 0:
    if n % i == 0:
        print(f"Ước số lớn nhất của {n} (khác chính nó) là: {i}")
        break  # Tìm thấy thì dừng luôn
    i -= 1