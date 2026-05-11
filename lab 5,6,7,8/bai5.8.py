

s = input("Nhap chuoi: ")

if len(s) > 10:

    print("Xau con tu vi tri 2 den 8:", s[2:9])

    print("5 ky tu tu vi tri 5:", s[5:10])

    print("3 ky tu cuoi:", s[-3:])

    print("In hoa:", s.upper())

    print("In thuong:", s.lower())

    print("Dao nguoc xau:", s[::-1])

else:
    print("Chuoi phai co do dai lon hon 10 ky tu!")