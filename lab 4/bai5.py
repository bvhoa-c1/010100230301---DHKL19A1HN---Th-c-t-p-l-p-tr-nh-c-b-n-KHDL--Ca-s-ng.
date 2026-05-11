n = input("Nhập số: ")
dao = ""
i = 0
while i < len(n):
    dao = n[i] + dao
    i += 1

if n == dao:
    print(f"{n}->Đúng")
else:
    print(f"{n}->Sai")
