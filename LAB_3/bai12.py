letter_map = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 'J': 20,
    'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29, 'S': 30, 'T': 31,
    'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}

container = input("Nhập số container (10 ký tự): ").strip().upper()

while len(container) != 10 or not all(ch.isdigit() or ch.isalpha() for ch in container[:4]) or not container[4:].isdigit():
    container = input("Mã container không hợp lệ, vui lòng nhập lại: ").strip().upper()

tong = 0
for i in range(10):
    ch = container[i]
    if ch.isalpha():
        value = letter_map[ch]
    else:
        value = int(ch)
    weight = value * (2 ** i)
    tong += weight

check_digit = tong % 11
if check_digit == 10:
    check_digit = 0

print("Mã container:", container)
print("Tổng trọng số =", tong)
print("Số kiểm tra =", check_digit)