str1 = input("Nhập chuỗi kí tự thứ nhất: ")
str2 = input("Nhập chuỗi kí tự thứ hai: ")
chuoi = ""
for i in str1:
    if i in str2:
        chuoi = i 
        break 
if chuoi:
    print(chuoi)
else:
    print("no")