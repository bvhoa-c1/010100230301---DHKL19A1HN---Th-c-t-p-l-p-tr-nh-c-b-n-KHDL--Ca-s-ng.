n = input("Nhập số nguyên dương n: ")
while not n.isdigit() or int(n) <= 0:
    n = input("n phải là số nguyên dương, vui lòng nhập lại: ")
chu_so = [int(ch) for ch in n]
tong = sum(chu_so)
tich = 1
for ch in chu_so:
    tich *= ch
so_dao = n[::-1]

print("Tổng các chữ số =", tong)
print("Tích các chữ số =", tich)
print("Số đảo =", so_dao)