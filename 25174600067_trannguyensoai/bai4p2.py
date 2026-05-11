def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b != 0:
        return a / b
    else:
        return None

# Nhập dữ liệu
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

# Gọi hàm và in kết quả
print("Cộng:", cong(a, b))
print("Trừ:", tru(a, b))
print("Nhân:", nhan(a, b))

ket_qua_chia = chia(a, b)
if ket_qua_chia is not None:
    print("Chia:", ket_qua_chia)
else:
    print("Không thể chia cho 0")