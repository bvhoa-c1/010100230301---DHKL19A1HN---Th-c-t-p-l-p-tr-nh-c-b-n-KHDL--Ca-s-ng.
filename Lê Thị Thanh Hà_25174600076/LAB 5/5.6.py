s = input("Nhập chuỗi: ")

special = 0

for ch in s:
    if not ch.isalnum():
        special += 1

length = len(s)

if length > 0:
    percent = special / length * 100
else:
    percent = 0

print("Số ký tự đặc biệt:", special)
print("Tỷ lệ:", percent, "%")
