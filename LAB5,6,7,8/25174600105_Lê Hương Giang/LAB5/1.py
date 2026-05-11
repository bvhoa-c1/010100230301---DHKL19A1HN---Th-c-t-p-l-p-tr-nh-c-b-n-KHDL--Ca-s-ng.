n = int(input("Nhập một số nguyên dương hệ thâpj phân: "))
chuoi = ""
while n > 0 :
    chuoi = str(n%2) + chuoi
    n = n // 2 
print(f"Số nguyên dương {n} chuyển sang hệ nhị phân là: {chuoi}")