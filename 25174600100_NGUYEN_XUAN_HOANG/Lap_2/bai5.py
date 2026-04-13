n = int(input("Nhap so n: "))

s = str(n)
s_dao = s[::-1]

if s == s_dao:
    print("Dung, so", n, "la so doi xung")
else:
    print("Sai, so", n, "khong la so doi xung")
