#câu1
n = int(input("nhập n:"))
a = 0 
b = 1
i = 1
while i < n :
    c = a +b
    a = b 
    b = c
    i = i+1
if n==0:
    print("số fibonacci thứ nhất là",a)
else:
    print("số fibonacci thứ n là",b)
#câu2 
mat_khau = input("Nhập mật khẩu: ")
while mat_khau != "123456":
    print("Mật khẩu không đúng")
    mat_khau = input("Nhập lại mật khẩu: ")
mat_khau == "123456"
print("Nhập mật khẩu thành công")
#câu3
n = int(input("Nhập n: "))
i = n - 1
while i > 0:
    if n % i == 0:
        uoc_chung_lon_nhất = i
        break
    i -= 1
print("Ước số lớn nhất của", n, "khác chính nó là:", uoc_chung_lon_nhất)
#câu4
tong = 0
dem = 0
so_lon_nhat = None
while True:
    n = int(input("Nhập số (0 để dừng): "))
    if n == 0:
        break   
    tong += n
    dem += 1
    if so_lon_nhat is None or n > so_lon_nhat:
        so_lon_nhat = n
print("Tổng các số đã nhập:", tong)
print("Số lượng số đã nhập:", dem)
print("Số lớn nhất là:", so_lon_nhat)
#câu5
n = input("Nhập số n: ")
if n == n[::-1]:
    print(n, "là số đối xứng ")
else:
    print(n, "không phải số đối xứng ")
#câu6
n = int(input("Nhập số n: "))
so_goc = n
tong = 0
temp = n
so_chu_so = len(str(n))  
while temp > 0:
    chu_so = temp % 10      
    tong += chu_so ** so_chu_so
    temp //= 10           
if tong == so_goc:
    print(n, "là số Armstrong ")
else:
    print(n, "không phải số Armstrong ")
#câu8
n = int(input("Nhập số n: "))
so_goc = n
tong = 0
tich = 1
so_dao = 0
temp = n
while temp > 0:
    chu_so = temp % 10    
    tong += chu_so           
    tich *= chu_so           
    so_dao = so_dao * 10 + chu_so 
    temp //= 10              
print("Tổng các chữ số:", tong)
print("Tích các chữ số:", tich)
print("Số đảo của", so_goc, "là:", so_dao)
#câu9
while True:
    print("\n----- MENU -----")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")
    choice = input("Chọn chức năng (0-4): ")
    if choice == "0":
        print("Thoát chương trình. Bye!")
        break  
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    if choice == "1":
        print("Kết quả:", a + b)
    elif choice == "2":
        print("Kết quả:", a - b)
    elif choice == "3":
        print("Kết quả:", a * b)
    elif choice == "4":
        if b != 0:
            print("Kết quả:", a / b)
        else:
            print("Lỗi: không thể chia cho 0!")
    else:
        print("Lựa chọn không hợp lệ, vui lòng thử lại.")