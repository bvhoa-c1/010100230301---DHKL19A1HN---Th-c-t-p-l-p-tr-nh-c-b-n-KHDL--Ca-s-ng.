str1 = input("Nhập chuỗi kí tự thứ nhất: ")
str2 = input("Nhập chuỗi kí tự thứ hai: ")
chuoi = ''
for i in range(len(str1)):
    chuoi = chuoi + str1[i] + "-" + str2[i] + "-"
print(chuoi)