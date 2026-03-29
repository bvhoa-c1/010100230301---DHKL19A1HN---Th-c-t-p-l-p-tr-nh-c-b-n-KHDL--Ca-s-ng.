#Bai1
n = int(input("Nhập vào số n: "))
if n <= 0:
    print("Vui lòng nhập n là một số nguyên dương!")
else:
    f1 = 1
    f2 = 1
    i = 1 # Biến đếm
    while i < n:
        tam = f1
        f1 = f2
        f2 = tam + f2
        i += 1       
    print(f"Số Fibonacci thứ {n} là: {f1}")

#Bai2
mat_khau = ""
while mat_khau != "123456":
    mat_khau = input("Mời bạn nhập mật khẩu: ")
    if mat_khau == "123456":
        print("Mật khẩu chính xác! Đăng nhập thành công.")
    else:
        print("Mật khẩu sai. Vui lòng thử lại!")

#Bai3
n = int(input("Nhập số n: "))
if n <= 1:
    print(f"Số {n} không có ước số nào khác chính nó.")
else:
    i = n // 2 
    
    while i >= 1:
        if n % i == 0:
            print(f"Ước số lớn nhất của {n} (khác {n}) là: {i}")
            break 
        i -= 1

#Bai4
tong = 0
so_luong = 0
so_lon_nhat = None

while True:
    n = float(input("Nhập một số (nhập 0 để dừng): "))
    if n == 0:
        break
    tong += n            
    so_luong += 1       
    if so_lon_nhat is None or n > so_lon_nhat:
        so_lon_nhat = n
print(f"\n--- Kết quả ---")
print(f"Tổng các số đã nhập: {tong}")
print(f"Số lượng các số đã nhập (không tính số 0): {so_luong}")
if so_lon_nhat is not None:
    print(f"Số lớn nhất đã nhập: {so_lon_nhat}")
else:
    print("Bạn chưa nhập số nào ngoài số 0.")

#Bai5
n = int(input("Nhập số n: "))
temp = n
so_dao = 0
while n > 0:
    chu_so_cuoi = n % 10          
    so_dao = so_dao * 10 + chu_so_cuoi 
    n //= 10                      
if temp == so_dao:
    print(f"Số {temp} là số đối xứng (Palindrome).")
else:
    print(f"Số {temp} không phải là số đối xứng.")

#Bai6
n = int(input("Nhập số n: "))
temp = n
temp_count = n
tong_armstrong = 0
so_chu_so = len(str(abs(n))) 
while temp > 0:
    chu_so = temp % 10                
    tong_armstrong += chu_so ** so_chu_so 
    temp //= 10                       
if n == tong_armstrong:
    print(f"Số {n} là số Armstrong.")
else:
    print(f"Số {n} không phải là số Armstrong.")

#Bai7
i = 2
while i <= 9:
    print(f"--- Bảng cửu chương {i} ---")
    j = 1
    while j <= 10:
        print(f"{i} x {j} = {i * j}")
        j += 1  
    print() 
    i += 1 

#Bai8
n = int(input("Nhập số nguyên dương n: "))
temp = n
tong_chu_so = 0
tich_chu_so = 1
so_dao = 0
if n == 0:
    tich_chu_so = 0
while n > 0:
    chu_so = n % 10            
    
    tong_chu_so += chu_so       
    tich_chu_so *= chu_so       
    so_dao = so_dao * 10 + chu_so 
    n //= 10                   
print(f"--- Kết quả cho số {temp} ---")
print(f"Tổng các chữ số: {tong_chu_so}")
print(f"Tích các chữ số: {tich_chu_so}")
print(f"Số đảo ngược: {so_dao}")

#Bai9
while True:
    print("\n--------- MENU CHỨC NĂNG ---------")
    print("1. Phép Cộng")
    print("2. Phép Trừ")
    print("3. Phép Nhân")
    print("4. Phép Chia")
    print("0. Thoát chương trình")
    print("----------------------------------")
    try:
        chon = int(input("Mời bạn chọn chức năng (0-4): "))
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên!")
        continue
    if chon == 0:
        print("Đang thoát chương trình... Tạm biệt!")
        break
    if chon in [1,2,3,4]:
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))
        if chon == 1:
            print(f"Kết quả: {a} + {b} = {a + b}")
        elif chon == 2:
            print(f"Kết quả: {a} - {b} = {a - b}")
        elif chon == 3:
            print(f"Kết quả: {a} * {b} = {a * b}")
        elif chon == 4:
            if b != 0:
                print(f"Kết quả: {a} / {b} = {a / b}")
            else:
                print("Lỗi: Không thể chia cho số 0!")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại từ 0 đến 4.")
    

#Bai10
h = int(input("Nhập vào chiều cao của tam giác: "))
dong = h
while dong >= 1:
    cot = 1
    while cot <= dong:
        print("*", end="") 
        cot += 1
    print() 
    dong -= 1 

#Bai11
n = 0
while n <= 10:
    n = int(input("Nhập số nguyên n (n > 10): "))
    if n <= 10:
        print("Yêu cầu n > 10. Vui lòng nhập lại!")
s1 = 0
s2 = 0
s3 = 0
s4 = 0
a = 0  
while a <= n:
    s2 += 1 / (3**(2*a + 1))
    if a >= 1:
        s1 += 6**a
        s3 += ((-1)**a) * (a**2)
        s4 += a * (a + 1) * (a + 2)     
    a += 1 
print(f"--- Kết quả với n = {n} ---")
print(f"a) S1 = {s1}")
print(f"b) S2 = {s2:.10f}")
print(f"c) S3 = {s3}")
print(f"d) S4 = {s4}")