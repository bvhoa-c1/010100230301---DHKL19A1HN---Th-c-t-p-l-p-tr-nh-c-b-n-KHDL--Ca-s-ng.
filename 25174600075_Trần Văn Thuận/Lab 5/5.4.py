nhap_xau = input("Nhập chuỗi bất kỳ: ")
so_loc = ""
for i in nhap_xau:
    if '0' <= i <= '9':
        so_loc += i
if so_loc == "":
    print("Không có số nào trong chuỗi")
else:
    n = int(so_loc)
    print("số trích xuất đc:", n)
    so_ngto = True
    if n < 2:
        so_ngto = False
    else:
        for i in range(2, n+1):
            if n % i == 0:
                so_ngto = False
                break
    if so_ngto:
        print("Là số nguyên tố", n)
    else:
        print("Không phải số nguyên tố", n)