s = input("Nhap chuoi: ")

count = 0

for ch in s:
    if not ch.isalnum() and ch != " ":
        count += 1

print("So ky tu dac biet:", count)

percent = count / len(s) * 100

print("Phan tram:", round(percent, 2), "%")