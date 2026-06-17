#Bài5.1:
n = int(input("Nhập số nguyên dương: "))
binary = bin(n)[2:]
print("Dạng nhị phân:", binary)

#Bài5.2:
str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")

giao_nhau = set(str1) & set(str2)

if giao_nhau:
    ket_qua = list(giao_nhau)
    print(f"Chuỗi con chung ngắn nhất tìm được: {ket_qua}")
else:
    print("Hai chuỗi không có điểm chung")

#Bài5.3:
van_ban = input("Nhập đoạn văn: ")
tu_khoa = input("Nhập từ cần tìm: ")

vi_tri = []
start = 0
while True:
    pos = van_ban.find(tu_khoa, start)
    if pos == -1: break 
    vi_tri.append(pos)
    start = pos + 1
print(f"Từ khóa xuất hiện tại các vị trí: {vi_tri}")

danh_sach_tu = van_ban.split()
tu_nhieu_nhat = max(set(danh_sach_tu), key=danh_sach_tu.count)
print(f"Từ xuất hiện dày đặc nhất là: '{tu_nhieu_nhat}'")

#Bài5.4:
s = input("Nhập chuỗi: ")
num_str = ""
for c in s:
    if c.isdigit():
        num_str += c
if num_str == "":
    print("Không có chữ số")
else:
    n = int(num_str)
    if n < 2:
        print(n, "không phải số nguyên tố")
    else:
        n_to = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                n_to = False
                break
        if n_to:
            print(n, "là số nguyên tố")
        else:
            print(n, "không phải số nguyên tố")

#Bài5.5:
s1 = input("Chuỗi 1: ")
s2 = input("Chuỗi 2: ")
ket_qua = ""

for i in range(max(len(s1), len(s2))):
    if i < len(s1):
        ket_qua += s1[i] + "-"
    if i < len(s2):
        ket_qua += s2[i] + "-"

print(f"Kết quả trộn: {ket_qua[:-1]}")

#Bài5.6:
s = input("Nhập chuỗi: ")
special = 0
for c in s:
    if not c.isalnum():
        special += 1
phan_tram = (special / len(s)) * 100
print("Số ký tự đặc biệt:", special)
print("Phần trăm:", round(phan_tram, 2), "%")

#Bài5.7:
s = input("Nhập chuỗi: ")
upper = lower = digit = special = 0
for c in s:
    if c.isupper():
        upper += 1
    elif c.islower():
        lower += 1
    elif c.isdigit():
        digit += 1
    else:
        special += 1
print("Chữ in hoa:", upper)
print("Chữ thường:", lower)
print("Chữ số:", digit)
print("Ký tự đặc biệt:", special)

#Bài5.8:
s = input("Nhập chuỗi: ")
if len(s) > 10:
    print("Từ vị trí 2 đến 8:", s[2:9])
    print("Từ vị trí 5:", s[5:10])
    print("3 ký tự cuối:", s[-3:])
    print("In hoa:", s.upper())
    print("In thường:", s.lower())
    print("Đảo ngược:", s[::-1])
else:
    print("Chuỗi phải lớn hơn 10 ký tự")

#Bài5.9:
str1 = input("Nhập chuỗi ban đầu: ")
str2 = input("Nhập chuỗi mục tiêu: ")
if str1 == str2:
    print("Hai chuỗi giống nhau")
else:
    print("Có thể chuyển đổi bằng thêm/xóa/thay thế ký tự")

#Bài5.10:
s = input("Nhập chuỗi: ")
result = s.replace(" ", "")
print("Chuỗi sau xử lý:", result)