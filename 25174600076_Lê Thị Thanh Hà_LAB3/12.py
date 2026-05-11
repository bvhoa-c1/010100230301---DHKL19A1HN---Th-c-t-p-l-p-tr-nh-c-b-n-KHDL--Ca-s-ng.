s = input("Nhập mã container: ")

tong = 0

for i in range(len(s)):
    ch = s[i]
    
    if ch.isalpha():  # nếu là chữ
        value = ord(ch) - ord('A') + 10
        if value % 11 == 0:
            value += 1
    else:  # nếu là số
        value = int(ch)
    
    tong += value * (2 ** i)

check = tong % 11
if check == 10:
    check = 0

print("Số kiểm tra là:", check)