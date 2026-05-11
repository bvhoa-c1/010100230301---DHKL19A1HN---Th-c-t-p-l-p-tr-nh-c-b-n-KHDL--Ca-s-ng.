# Bài 8.4: Hàm tính tổng lập phương các chữ số
def cubesum(n):
    total = 0
    n_abs = abs(n)  # xử lý số âm nếu có
    for ch in str(n_abs):
        digit = int(ch)
        total += digit ** 3
    return total

# Bài 8.5: Kiểm tra số Armstrong
def isArmstrong(n):
    if n < 0:
        return False
    return cubesum(n) == n

# Xuất danh sách số Armstrong < 1000
print("Các số Armstrong nhỏ hơn 1000:")
for i in range(1000):
    if isArmstrong(i):
        print(i, end=" ")
print()

# Kiểm tra một số cụ thể
num = int(input("Nhập số để kiểm tra: "))
if isArmstrong(num):
    print(num, "là số Armstrong")
else:
    print(num, "không là số Armstrong")