n = int(input("Nhập số n: "))
a = n

tong = 0
tich = 1
dao = 0

while a > 0:
    chu_so = a % 10      # lấy chữ số cuối
    tong += chu_so         # cộng vào tổng
    tich *= chu_so         # nhân vào tích
    dao = dao * 10 + chu_so  # tạo số đảo
    
    a //= 10             # bỏ chữ số cuối

print("Tổng chữ số:", tong)
print("Tích chữ số:", tich)
print("Số đảo:", dao)