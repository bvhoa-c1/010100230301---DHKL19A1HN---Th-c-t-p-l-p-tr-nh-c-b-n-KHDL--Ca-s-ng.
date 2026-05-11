n = input("Nhập số n: ")

tong = 0
tich = 1
dao_nguoc = "" # tạo chuỗi rỗng

for i in n:
    chu_so = int(i)
    
    tong += chu_so

    tich *= chu_so

    dao_nguoc = i + dao_nguoc
print("Tổng các chữ số là: ",tong)
print("Tích các chữ số là: ",tich)
print("Số đảo ngược là: ",dao_nguoc)