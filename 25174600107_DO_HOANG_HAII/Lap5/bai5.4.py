def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

s = input("Nhập xâu ký tự: ")

digits_only = ''.join(c for c in s if c.isdigit())

if not digits_only:
    print("Xâu không chứa chữ số nào!")
else:
    number = int(digits_only)
    print(f"Xâu sau khi loại bỏ ký tự không phải chữ số: {digits_only}")
    print(f"Số nguyên: {number}")
    
    if is_prime(number):
        print(f"{number} là số nguyên tố")
    else:
        print(f"{number} không phải là số nguyên tố")
