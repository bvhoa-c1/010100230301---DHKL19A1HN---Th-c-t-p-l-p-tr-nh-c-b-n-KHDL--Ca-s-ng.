# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Nhập chuỗi
s = input("Nhập chuỗi: ")

# Lấy các ký tự là chữ số
digits = ""

for ch in s:
    if ch.isdigit():
        digits += ch

# Kiểm tra kết quả
if digits == "":
    print("Không có chữ số trong chuỗi.")
else:
    number = int(digits)

    print("Số sau khi tách:", number)

    if is_prime(number):
        print(number, "là số nguyên tố")
    else:
        print(number, "không phải là số nguyên tố")