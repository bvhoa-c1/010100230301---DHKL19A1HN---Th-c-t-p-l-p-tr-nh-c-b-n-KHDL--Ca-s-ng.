#5.1
n = int(input("Nhập số: "))
binary = ""
while n > 0:
    binary = str(n % 2) + binary
    n //= 2
print("Nhị phân:", binary)
#5.2
str1 = input("Chuỗi 1: ")
str2 = input("Chuỗi 2: ")
found = False
for length in range(1, len(str1)+1):
    for i in range(len(str1)-length+1):
        sub = str1[i:i+length]
        if sub in str2:
            print("Chuỗi con chung ngắn nhất:", sub)
            found = True
            break
    if found:
        break
#5.3
text = input("Nhập văn bản: ")
keyword = input("Nhập từ khóa: ")
index = text.find(keyword)
while index != -1:
    print("Xuất hiện tại:", index)
    index = text.find(keyword, index + 1)
words = text.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
max_word = max(freq, key=freq.get)
print("Từ xuất hiện nhiều nhất:", max_word)
print("Số lần:", freq[max_word])
#5.4
s = input("Nhập chuỗi: ")
digits = ""
for c in s:
    if c.isdigit():
        digits += c
n = int(digits)
prime = True
if n < 2:
    prime = False
else:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            prime = False
            break
print("Số sau khi lọc:", n)
if prime:
    print("Là số nguyên tố")
else:
    print("Không phải số nguyên tố")
#5.5
s1 = input("Chuỗi 1: ")
s2 = input("Chuỗi 2: ")
result = []
min_len = min(len(s1), len(s2))
for i in range(min_len):
    result.append(s1[i])
    result.append(s2[i])
print("-".join(result))
#5.6
s = input("Nhập chuỗi: ")
special = {}
for c in s:
    if not c.isalnum():
        special[c] = special.get(c, 0) + 1
for k, v in special.items():
    percent = v / len(s) * 100
    print(k, ":", v, "lần")
    print("Tỷ lệ:", round(percent,2), "%")
#5.7
s = input("Nhập chuỗi: ")
lower = upper = digit = special = 0
for c in s:
    if c.islower():
        lower += 1
    elif c.isupper():
        upper += 1
    elif c.isdigit():
        digit += 1
    else:
        special += 1
print("Chữ thường:", lower)
print("Chữ hoa:", upper)
print("Chữ số:", digit)
print("Ký tự đặc biệt:", special)
#5.8
s = input("Nhập chuỗi: ")
if len(s) > 10:
    print("Từ vị trí 2 đến 8:", s[2:9])
    print("5 ký tự từ vị trí 5:", s[5:10])
    print("3 ký tự cuối:", s[-3:])
    print("In hoa:", s.upper())
    print("In thường:", s.lower())
    print("Đảo ngược:", s[::-1])
#5.9
s1 = input("Chuỗi đầu: ")
s2 = input("Chuỗi đích: ")
if s1 == s2:
    print("Không cần chuyển đổi")
else:
    print("Có thể chuyển đổi bằng thêm/xóa/thay ký tự")
#5.10
s = input("Nhập chuỗi: ")
s = s.replace(" ", "")
print(s)







    