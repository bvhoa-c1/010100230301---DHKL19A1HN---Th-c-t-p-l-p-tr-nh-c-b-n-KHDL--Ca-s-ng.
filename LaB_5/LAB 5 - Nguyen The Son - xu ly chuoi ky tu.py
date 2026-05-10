
# Bài 5.1: Đổi số thập phân sang nhị phân
n = int(input("Nhập số nguyên dương: "))
binary = bin(n)[2:]
print("Dạng nhị phân:", binary)

# Bài 5.2: Tìm xâu con chung ngắn nhất
str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")

found = False

for length in range(1, min(len(str1), len(str2)) + 1):
    for i in range(len(str1) - length + 1):
        sub = str1[i:i+length]

        if sub in str2:
            print("Xâu con chung ngắn nhất:", sub)
            found = True
            break

    if found:
        break

if not found:
    print("Không có xâu con chung")
# Bài 5.3: Tìm kiếm và thống kê tần suất
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

# Bài 5.4: Loại bỏ ký tự không phải số và kiểm tra số nguyên tố

s = input("Nhập chuỗi: ")

digits = ""

for ch in s:
    if ch.isdigit():
        digits += ch

print("Chuỗi số:", digits)

if digits != "":
    number = int(digits)

    if number < 2:
        print(number, "không phải số nguyên tố")
    else:
        prime = True

        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                prime = False
                break

        if prime:
            print(number, "là số nguyên tố")
        else:
            print(number, "không phải số nguyên tố")
else:
    print("Không có chữ số nào")

# Bài 5.5: Trộn hai chuỗi ký tự

s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")

result = []
max_len = max(len(s1), len(s2))

for i in range(max_len):

    if i < len(s1):
        result.append(s1[i])

    if i < len(s2):
        result.append(s2[i])

print("-".join(result))

# Bài 5.6: Đếm ký tự đặc biệt và tính %

s = input("Nhập chuỗi: ")

special = {}
length = len(s)

for ch in s:
    if not ch.isalnum() and ch != " ":
        special[ch] = special.get(ch, 0) + 1

print("Ký tự đặc biệt:")

for ch, count in special.items():
    percent = (count / length) * 100
    print(f"{ch}: {count} lần - {percent:.2f}%")

# Bài 5.7: Thống kê ký tự

s = input("Nhập chuỗi: ")

lower = upper = digit = special = 0

for ch in s:

    if ch.islower():
        lower += 1

    elif ch.isupper():
        upper += 1

    elif ch.isdigit():
        digit += 1

    else:
        special += 1

print("Chữ thường:", lower)
print("Chữ hoa:", upper)
print("Chữ số:", digit)
print("Ký tự đặc biệt:", special)

# Bài 5.8: Xử lý chuỗi > 10 ký tự

s = input("Nhập chuỗi: ")

if len(s) > 10:

    print("Từ vị trí 2 đến 8:", s[2:9])

    print("5 ký tự từ vị trí 5:", s[5:10])

    print("3 ký tự cuối:", s[-3:])

    print("In hoa:", s.upper())

    print("In thường:", s.lower())

    print("Đảo ngược:", s[::-1])

else:
    print("Chuỗi phải lớn hơn 10 ký tự")

# Bài 5.9: Kiểm tra khả năng chuyển đổi chuỗi

s1 = input("Chuỗi ban đầu: ")
s2 = input("Chuỗi mục tiêu: ")

if s1 == s2:
    print("Hai chuỗi giống nhau")

else:
    print("Có thể chuyển đổi bằng thêm/xóa/thay thế ký tự")

# Bài 5.10: Xóa khoảng trắng trong chuỗi

s = input("Nhập chuỗi: ")

result = s.replace(" ", "")

print("Chuỗi sau khi xóa khoảng trắng:", result)