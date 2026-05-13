# Bài 5.1: Chuyển đổi số nguyên dương từ hệ thập phân sang nhị phân

n = int(input("Nhập một số nguyên dương: "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    binary = bin(n)[2:]  # bin() trả về '0b...' nên cắt bỏ '0b'
    print(f"Số {n} dạng nhị phân: {binary}")
