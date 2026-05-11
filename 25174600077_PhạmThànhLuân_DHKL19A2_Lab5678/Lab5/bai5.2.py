str1 = input("Nhập chuỗi 1 : ")
str2 =input("Nhập chuối 2 : ")
chuoi_min = ""
min = 10**9
for i in range(len(str1)) :
    for j in range(i+1,len(str1)+1) :
        s = str1[i:j]
        if s in str2 :
            if len(s) < min :
                min = len(s)
                chuoi_min = s 
print(f"Chuỗi con chung ngắn nhất {chuoi_min}")