# Bài 5.4: Loại bỏ ký tự không phải số và kiểm tra tính nguyên tố

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

text = input("Nhập xâu: ")

# Loại bỏ ký tự không phải số
digits_only = ''.join(c for c in text if c.isdigit())

if digits_only:
    number = int(digits_only)
    print(f"Xâu sau khi loại bỏ ký tự không phải số: {digits_only}")
    print(f"Số nguyên: {number}")
    if is_prime(number):
        print(f"{number} là số nguyên tố!")
    else:
        print(f"{number} không phải số nguyên tố!")
else:
    print("Không có chữ số nào trong xâu!")
