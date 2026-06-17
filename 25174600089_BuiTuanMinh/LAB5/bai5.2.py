str1 = input("nhập chuỗi 1:")
str2 = input("nhập chuỗi 2:")
ngan_nhat=""
for i in range(len(str1)):
    for j in range (i+1, len(str1)+1):
        chuoi_con= str1[i:j]
        if chuoi_con in str2:
            if ngan_nhat== "" or len(chuoi_con)<len(ngan_nhat):
                ngan_nhat=chuoi_con
if ngan_nhat:
    print(ngan_nhat)
else:
    print("ko co chuoi con chung")
