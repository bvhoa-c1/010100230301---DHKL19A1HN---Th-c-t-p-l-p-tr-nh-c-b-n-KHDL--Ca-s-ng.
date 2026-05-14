# bài 5.1
n = int(input("Nhập số nguyên dương: "))

nhi_phan = bin(n)[2:]

print("Số nhị phân:", nhi_phan)
# bài 5.2
str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")

ket_qua = ""

for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        sub = str1[i:j]

        if sub in str2:
            if ket_qua == "" or len(sub) < len(ket_qua):
                ket_qua = sub

if ket_qua != "":
    print("Chuỗi con chung ngắn nhất:", ket_qua)
else:
    print("Không có chuỗi con chung")
    # bài 5.3
text = input("Nhập đoạn văn: ")
keyword = input("Nhập từ khóa: ")

# Tìm vị trí xuất hiện
pos = []
start = 0

while True:
    index = text.find(keyword, start)

    if index == -1:
        break

    pos.append(index)
    start = index + 1

print("Vị trí xuất hiện:", pos)

# Đếm tần suất từ
words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

max_word = max(freq, key=freq.get)

print("Từ xuất hiện nhiều nhất:", max_word)
print("Số lần:", freq[max_word])
#bài 5.4
s = input("Nhập chuỗi: ")

so = ""

for c in s:
    if c.isdigit():
        so += c

print("Chuỗi số:", so)

n = int(so)

la_nguyen_to = True

if n < 2:
    la_nguyen_to = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            la_nguyen_to = False
            break

if la_nguyen_to:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải số nguyên tố")
    # bài 5.5
    s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")

ket_qua = []

max_len = max(len(s1), len(s2))

for i in range(max_len):
    if i < len(s1):
        ket_qua.append(s1[i])

    if i < len(s2):
        ket_qua.append(s2[i])

print("-".join(ket_qua))
# bài 5.6
s = input("Nhập chuỗi: ")

special = {}

for c in s:
    if not c.isalnum() and not c.isspace():
        special[c] = special.get(c, 0) + 1

for k, v in special.items():
    ti_le = v / len(s) * 100
    print(k, ":", v, "lần -", round(ti_le, 2), "%")
    #bài 5.7
    s = input("Nhập chuỗi: ")

thuong = 0
hoa = 0
so = 0
dac_biet = 0

for c in s:
    if c.islower():
        thuong += 1
    elif c.isupper():
        hoa += 1
    elif c.isdigit():
        so += 1
    else:
        dac_biet += 1

print("Chữ thường:", thuong)
print("Chữ hoa:", hoa)
print("Chữ số:", so)
print("Ký tự đặc biệt:", dac_biet)
# bài 5.8
s = input("Nhập chuỗi: ")

if len(s) > 10:
    print("Từ vị trí 2 đến 8:", s[2:9])
    print("5 ký tự từ vị trí 5:", s[5:10])
    print("3 ký tự cuối:", s[-3:])
    print("Chữ hoa:", s.upper())
    print("Chữ thường:", s.lower())
    print("Đảo ngược:", s[::-1])
else:
    print("Chuỗi phải lớn hơn 10 ký tự")
    # bài 5.9
    s1 = input("Chuỗi ban đầu: ")
s2 = input("Chuỗi mục tiêu: ")

if s1 == s2:
    print("Hai chuỗi giống nhau")
else:
    print("Có thể chuyển đổi bằng thêm/xóa/thay thế ký tự")
    # bài 5.10
    s = input("Nhập chuỗi: ")

ket_qua = s.replace(" ", "")

print("Chuỗi sau khi xóa khoảng trắng:", ket_qua)
