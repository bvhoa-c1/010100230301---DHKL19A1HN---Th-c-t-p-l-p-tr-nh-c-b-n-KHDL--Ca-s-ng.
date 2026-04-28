def tinh_toan(a, b):
    print("Tổng =", a + b)
    print("Hiệu =", a - b)
    print("Tích =", a * b)
    
    if b != 0:
        print("Thương =", a / b)
    else:
        print("Không thể chia cho 0")

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

tinh_toan(a, b)