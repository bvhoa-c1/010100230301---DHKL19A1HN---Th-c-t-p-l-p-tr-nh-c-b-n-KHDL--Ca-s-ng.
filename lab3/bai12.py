# Bảng mã hóa ký tự chữ cái (bỏ qua các bội số của 11)
char_map = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19,
    'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29,
    'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}

# Nhập số container (ví dụ: SUDU307007)
container_id = input("Nhập chuỗi 10 ký tự container: ").upper()

total_sum = 0

# Bước 1 & 2: Duyệt qua từng ký tự và tính tổng trọng số
for n in range(len(container_id)):
    char = container_id[n]
    
    # Lấy giá trị của ký tự
    if char.isalpha():
        value = char_map[char]
    else:
        value = int(char)
    
    # Tính trọng số: giá trị * 2^n
    weight = value * (2**n)
    total_sum += weight

# Bước 3: Tính số kiểm tra (check digit)
remainder = total_sum % 11

# Nếu số dư là 10 thì lấy kết quả bằng 0
check_digit = 0 if remainder == 10 else remainder

print(f"Tổng trọng số: {total_sum}")
print(f"Số kiểm tra (Check Digit) cần tìm là: {check_digit}")