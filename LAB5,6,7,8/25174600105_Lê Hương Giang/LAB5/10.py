str = input("Nhập chuỗi kí tự: ")
chuoi = ""
for i in str:
    if i != " ":
        chuoi += i 
print("Chuỗi sau khi xóa khoảng trắng là: ",chuoi)