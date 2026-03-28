n = input("Nhập số n: ")

dao_nguoc ="" #tạo chuỗi rỗng
for i in n:
    dao_nguoc = i + dao_nguoc

if n == dao_nguoc:
    print("Đúng")
else:
    print("sai")