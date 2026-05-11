s = input("Nhap chuoi (>10 ky tu): ")

if len(s) > 10:
    print("Tu vi tri 2 den 8:", s[2:9])
    print("5 ky tu tu vi tri 5:", s[5:10])
    print("3 ky tu cuoi:", s[-3:])
    print("Chu hoa:", s.upper())
    print("Chu thuong:", s.lower())
    print("Dao nguoc:", s[::-1])
else:
    print("Chuoi khong du do dai")