n = int(input("Nhập số lượng phần tử: "))

a = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(x)

chan = []
le = []

for x in a:
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)

print("Danh sách chẵn:", chan)
print("Tổng chẵn:", sum(chan))

print("Danh sách lẻ:", le)
print("Tổng lẻ:", sum(le))


