s1 = input("Nhập chuỗi thứ 1: ")
s2 = input("Nhập chuỗi thứ 2: ")
kq = " "
max_len = len(s1)
if len(s2) > max_len:
    max_len = len(s2)
for i in range(max_len): 
    if i < len(s1):
        kq += s1[i] + "-"
    if i < len(s2):
        kq += s2[i] + "-"
if kq.endswith("-"):
    kq = kq[:-1]
print("chuỗi sau khi tròn:", kq)