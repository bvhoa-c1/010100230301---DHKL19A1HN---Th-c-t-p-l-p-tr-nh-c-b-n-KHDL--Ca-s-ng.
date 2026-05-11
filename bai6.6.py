# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử: "))

# Nhập dãy số
day_so = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    day_so.append(x)

# Tính sai phân
sai_phan = [day_so[i+1] - day_so[i] for i in range(len(day_so)-1)]

print("Dãy số:", day_so)
print("Sai phân giữa các phần tử liên tiếp:", sai_phan)

# Kiểm tra cấp số cộng
if len(sai_phan) > 0 and all(x == sai_phan[0] for x in sai_phan):
    print("=> Dãy số là cấp số cộng")
else:
    print("=> Dãy số không phải cấp số cộng")