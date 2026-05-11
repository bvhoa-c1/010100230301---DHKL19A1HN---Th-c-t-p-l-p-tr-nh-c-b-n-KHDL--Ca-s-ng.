n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    x = int(input("Nhập phần tử: "))
    a.append(x)
chan = 0
le = 0
for i in a:
    if i % 2 == 0:
        chan += i
    else:
        le += i
print("Tổng số chẵn:", chan)
print("Tổng số lẻ:", le)