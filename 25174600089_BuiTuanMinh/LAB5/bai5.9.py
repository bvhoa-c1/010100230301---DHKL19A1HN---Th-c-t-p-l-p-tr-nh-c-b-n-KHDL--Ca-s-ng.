chuoi = input("nhap >10 ky tu:")
if len(chuoi) <=10:
    print("nhap them")
else:
    print("chuỗi gốc",chuoi)
    print("chuỗi từ 2 đến 8",chuoi[1:8])
    print("đảo ngược chuỗi",chuoi[::-1])
    