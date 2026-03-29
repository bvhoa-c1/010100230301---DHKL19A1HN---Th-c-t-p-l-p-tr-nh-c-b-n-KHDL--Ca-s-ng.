""" ---BÀI TẬP VỀ NHÀ LAB_4 ---"""


""" Bài 1: Nhập n. Tìm số Fibonacci thứ n bằng while """

n = int(input("Nhập n (bài 1): "))
a = 0
b = 1
i = 0

while i < n:
    a, b = b, a + b
    i += 1
print("Số Fibonacci thứ", n, "là: ", a)


""" Bài 2: Viết chương trình cho phép nhập mật khẩu liên tục cho đến khi đúng "123456"."""

mat_khau = " "
while mat_khau != "123456":
    mat_khau = input("Nhập mật khẩu: ")

print("Mật khẩu chính xác !")


""" Bài 3: Nhập số n. Tìm ước số lớn nhất của n (khác n)."""

n = int(input("Nhập số n (bài 3): "))
i = n // 2

while i > 0:
    if n % i == 0:
        print("Ước số lớn nhất của", n, "là: ", i)
        break
    i -= 1    # giảm dần i để kiểm tra các số nhỏ hơn


""" Bài 4: Nhập số liên tục cho đến khi nhập số 0 thì dừng. Tính tổng các số- Đếm số lượng số- Tìm số lớn nhất   """ 

tong = 0
dem = 0
so_max = None

while True:
    n = int(input("Nhập số liên tục (nhập 0 để dừng): "))
    if n == 0:
        break
    
    tong += n
    dem += 1
    
    if so_max is None or n > so_max:
        so_max = n

print("Tổng các số là: ", tong)
print("Số lượng (không tính số 0): ", dem)

if dem > 0:
    print("Số lớn nhất là:", so_max)
else:
    print("Không có số nào được nhập!")


""" Bài 5: Nhập số n. Kiểm tra n có phải số đối xứng (palindrome) không. Ví dụ: 121 → đúng, 123 → sai    """

n = int(input("Nhập số n (bài 5): "))
ban_dau = n
so_dao = 0

while n > 0:
    chu_so = n % 10
    so_dao = so_dao * 10 + chu_so
    n = n // 10

if ban_dau == so_dao:
    print("Là số đối xứng")
else:
    print("Không phải số đối xứng")


""" Bài 6: Nhập n. Kiểm tra n có phải số Armstrong không (VD: 153 = 1³ + 5³ + 3³)  """

n = int(input("Nhập số n (bài 6): "))
so_ban_dau = n
tong = 0
dem = 0
t = n  # t là biến phụ

while t > 0:
    dem += 1
    t = t // 10

while so_ban_dau > 0:
    chu_so = so_ban_dau % 10
    tong += chu_so ** dem
    so_ban_dau = so_ban_dau // 10

if tong == n:
    print("Là số Armstrong")
else:
    print("Không phải số Armstrong !")


""" Bài 7: In bảng cửu chương từ 2 → 9 bằng while lồng nhau """

i = 2
while i <= 9:
    print("Bảng cửu chương", i)
    
    j = 1
    while j <= 10:
        print(i, "x", j, "=", i * j)
        j += 1
    
    print() 
    i += 1


""" Bài 8: Viết chương trình:
➢ Nhập số n
➢ Tách từng chữ số
➢ Tính:
▪ Tổng chữ số
▪ Tích chữ số
▪ Số đảo
 """  

n = int(input("Nhập số n (bài 8): "))
so_ban_dau = n
tong = 0
tich = 1
so_dao = 0

while so_ban_dau > 0:
    chu_so = so_ban_dau % 10      # lấy chữ số cuối
    tong += chu_so                # cộng vào tổng
    tich *= chu_so                # nhân vào tích
    so_dao = so_dao * 10 + chu_so # tạo số đảo
    so_ban_dau = so_ban_dau // 10      # bỏ chữ số cuối

print("Tổng chữ số là: ", tong)
print("Tích chữ số là: ", tich)
print("Số đảo là: ", so_dao)  


""" Bài 9: Viết chương trình menu:
1. Cộng
2. Trừ
3. Nhân
4. Chia
0. Thoát
"""

while True:
    print("----- MENU -----")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")

    chon = int(input("Chọn chương trình: "))

    if chon == 0:
        print("Thoát chương trình!")
        break

    if chon >= 1 and chon <= 4:
        a = float(input("Nhập số a: "))
        b = float(input("Nhập số b: "))

        if chon == 1:
            print("Kết quả phép cộng:", a + b)
        elif chon == 2:
            print("Kết quả phép trừ:", a - b)
        elif chon == 3:
            print("Kết quả phép nhân:", a * b)
        elif chon == 4:
            if b == 0:
                print("Không thể chia cho 0!")
            else:
                print("Kết quả phép chia:", a / b)
    else:
        print("Lựa chọn chương trình không hợp lệ!")


""" Bài 10: In tam giác ngược (bằng dấu *) """   

n = int(input("Nhập số dòng: "))

i = n
while i > 0:
    j = 0
    while j < i:
        print("*", end=" ")
        j += 1
    print()
    i -= 1


""" Bài 11: Tính các biểu thức """   

n = int(input("Nhập số nguyên n (bài 11) (n > 10): "))
while n <= 0:
    n = int(input(" Yêu cầu nhập lại n (n > 0): "))
a = 1
S1 = 0
S2 = 0
S3 = 0
S4 = 0

while a <= n:
    # a
    S1 += 6 ** a
    # b
    S2 += 1 / (3 ** (2 * a + 1))
    # c
    S3 += ((-1) ** a) * (a ** 2)
    # d
    S4 += a * (a + 1) * (a + 2)

    a += 1
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)












