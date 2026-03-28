# bài 1: Tính số Fibonacci thứ n bằng vòng lặp while.
n = 6
f1, f2 = 1, 1
count = 2
if n == 1 or n == 2:
    print(f"Số Fibonacci thứ {n} là: 1")
else:
    while count < n:
        f_next = f1 + f2
        f1, f2 = f2, f_next
        count += 1
    print(f"Số Fibonacci thứ {n} là: {f2}")

# bài 2: Nhập mật khẩu đúng mới dừng.
mat_khau = ""
while mat_khau != "123456":
    mat_khau = input("Nhập mật khẩu: ")
print("Đăng nhập thành công!")

# bài 3: Tìm ước số lớn nhất của n (khác n).
n = 20
uoc = n - 1
while uoc > 0:
    if n % uoc == 0:
        print(f"Ước lớn nhất của {n} (khác {n}) là: {uoc}")
        break
    uoc -= 1

# bài 4: Nhập số đến khi gặp 0, tính tổng, đếm số lượng, tìm số lớn nhất.
tong = 0
dem = 0
lon_nhat = None

while True:
    so = float(input("Nhập số (0 để dừng): "))
    if so == 0:
        break
    tong += so
    dem += 1
    if lon_nhat is None or so > lon_nhat:
        lon_nhat = so

print(f"Tổng: {tong}, Số lượng: {dem}, Lớn nhất: {lon_nhat}")

# bài 5: Kiểm tra số đối xứng
n_doi = int(input("Nhập số để kiểm tra đối xứng: "))
temp = n_doi
so_dao = 0

while temp > 0:
    chu_so = temp % 10
    so_dao = so_dao * 10 + chu_so
    temp //= 10

if n_doi == so_dao:
    print(f"{n_doi} là số đối xứng (đúng)")
else:
    print(f"{n_doi} không là số đối xứng (sai)")

# bài 6: Tính số kiểm tra Armstrong
n_armstrong = 153
temp = n_armstrong
tong_armstrong = 0
so_luong_chu_so = len(str(n_armstrong))

while temp > 0:
    chu_so = temp % 10
    tong_armstrong += chu_so ** so_luong_chu_so
    temp //= 10

if tong_armstrong == n_armstrong:
    print(f"{n_armstrong} là số Armstrong.")
else:
    print(f"{n_armstrong} không phải số Armstrong.")

# bài 7: Bảng cửu chương từ 2 đến 9.
i = 2
while i <= 9:
    j = 1
    while j <= 10:
        print(f"{i} x {j} = {i*j:<2}", end="  ")
        j += 1
    print()
    i += 1

# bài 8: Tách chữ số, tính tổng, tích, số đảo
n_tach = int(input("Nhập số để tách chữ số: "))
temp = n_tach
tong_cs = 0
tich_cs = 1
dao = 0

while temp > 0:
    chu_so = temp % 10
    tong_cs += chu_so
    tich_cs *= chu_so
    dao = dao * 10 + chu_so
    temp //= 10
print(f"Số: {n_tach} -> Tổng CS: {tong_cs}, Tích CS: {tich_cs}, Số đảo: {dao}")

# bài 9: Menu toán học
while True:
    print("1. Cộng\\n2. Trừ\\n3. Nhân\\n4. Chia\\n0. Thoát")
    chon = int(input("Chọn (0-4): "))
    if chon == 0:
        break
    if chon in [1, 2, 3, 4]:
        a = float(input("Nhập số 1: "))
        b = float(input("Nhập số 2: "))
        if chon == 1:
            print("Kết quả:", a + b)
        elif chon == 2:
            print("Kết quả:", a - b)
        elif chon == 3:
            print("Kết quả:", a * b)
        elif chon == 4:
            if b != 0:
                print("Kết quả:", a / b)
            else:
                print("Lỗi chia 0!")
    else:
        print("Lựa chọn không hợp lệ.")

# bài 10: In tam giác ngược
so_hang = 4
while so_hang > 0:
    print("*" * so_hang)
    so_hang -= 1

# bài 11: Tính 4 tổng S1, S2, S3, S4
n = int(input("Nhập n (n > 10): "))
while n <= 10:
    n = int(input("n phải lớn hơn 10. Nhập lại: "))

a = 1
S1 = S2 = S3 = S4 = 0

while a <= n:
    S1 += 6 ** a
    S2 += 1 / (3 ** (2*a - 1))
    S3 += ((-1) ** a) * (a ** 2)
    S4 += a * (a + 1) * (a + 2)
    a += 1

print(f"S1 = {S1}")
print(f"S2 = {S2}")
print(f"S3 = {S3}")
print(f"S4 = {S4}")