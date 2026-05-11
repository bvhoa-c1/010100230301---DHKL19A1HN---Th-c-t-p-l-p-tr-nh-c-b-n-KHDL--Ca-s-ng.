so = int(input("Nhập số: "))

tong_chu_so = 0
tich_chu_so = 1
so_dao = 0

so_tam = so   # dùng để xử lý, giữ nguyên số ban đầu

while so_tam > 0:
    chu_so = so_tam % 10

    tong_chu_so += chu_so
    tich_chu_so *= chu_so
    so_dao = so_dao * 10 + chu_so

    so_tam //= 10

print("Tổng chữ số:", tong_chu_so)
print("Tích chữ số:", tich_chu_so)
print("Số đảo:", so_dao)