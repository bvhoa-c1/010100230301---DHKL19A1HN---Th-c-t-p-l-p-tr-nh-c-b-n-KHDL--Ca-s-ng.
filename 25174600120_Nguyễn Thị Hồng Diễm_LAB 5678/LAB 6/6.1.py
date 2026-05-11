n = int(input("Nhập số lượng phần tử: "))
loai = []
for i in range(n):
    loai.append(int(input(f"Nhập số thứ{i+1}: ")))
chan = []
le = []
for x in loai:
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)
print("Nhóm chẵn:", chan, "-Tổng:", sum(chan))
print("Nhóm lẻ:", le, "-Tổng:", sum(le))