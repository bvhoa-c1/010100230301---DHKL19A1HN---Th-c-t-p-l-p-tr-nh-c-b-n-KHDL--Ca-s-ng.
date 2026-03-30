def char_to_value(c):
    if c.isalpha():
        return ord(c) - ord('A') + 10
    return int(c)

container = input("Nhập mã container (10 ký tự): ")

tong = 0

for i in range(len(container)):
    value = char_to_value(container[i])
    tong += value * (2 ** i)

check_digit = tong % 11
if check_digit == 10:
    check_digit = 0

print("Số kiểm tra là:", check_digit)