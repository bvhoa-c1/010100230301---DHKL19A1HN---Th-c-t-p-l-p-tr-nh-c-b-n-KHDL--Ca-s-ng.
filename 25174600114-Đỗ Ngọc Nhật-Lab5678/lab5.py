# 5.1
n = int(input("Nhập số nguyên dương: "))
binary = bin(n)[2:]
print("Số nhị phân là:", binary)

# 5.2
str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")

result = ""

for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        sub = str1[i:j]

        if sub in str2:
            if result == "" or len(sub) < len(result):
                result = sub

if result:
    print("Chuỗi con chung ngắn nhất:", result)
else:
    print("Không có chuỗi con chung")

#5.3
text = input("Nhập chuỗi văn bản: ")
keyword = input("Nhập từ khóa: ")

pos = text.find(keyword)

if pos != -1:
    print("Từ khóa xuất hiện tại vị trí:", pos)
else:
    print("Không tìm thấy từ khóa")

words = text.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

max_word = max(freq, key=freq.get)

print("Từ xuất hiện nhiều nhất:", max_word)
print("Số lần xuất hiện:", freq[max_word])

#5.4
s = input("Nhập xâu: ")

number_str = ""

for ch in s:
    if ch.isdigit():
        number_str += ch

print("Xâu chỉ chứa số:", number_str)

n = int(number_str)

is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải số nguyên tố")

#5.5
s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")

result = []

min_len = min(len(s1), len(s2))

for i in range(min_len):
    result.append(s1[i])
    result.append(s2[i])

result.extend(s1[min_len:])
result.extend(s2[min_len:])

print("-".join(result))

#5.6
s = input("Nhập xâu: ")

special = {}

for ch in s:
    if not ch.isalnum() and ch != " ":
        special[ch] = special.get(ch, 0) + 1

length = len(s)

for ch, count in special.items():
    percent = (count / length) * 100
    print(f"Ký tự '{ch}' xuất hiện {count} lần ({percent:.2f}%)")


#5.7
s = input("Nhập xâu: ")

lower = 0
upper = 0
digit = 0
special = 0

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


#5.8
s = input("Nhập xâu (>10 ký tự): ")

if len(s) > 10:

    print("Xâu con từ vị trí 2 đến 8:", s[2:9])

    print("5 ký tự từ vị trí 5:", s[5:10])

    print("3 ký tự cuối:", s[-3:])

    print("Chữ hoa:", s.upper())

    print("Chữ thường:", s.lower())

    print("Xâu đảo ngược:", s[::-1])

else:
    print("Xâu không đủ độ dài")


#5.9
s1 = input("Nhập chuỗi ban đầu: ")
s2 = input("Nhập chuỗi mục tiêu: ")

if s1 == s2:
    print("Hai chuỗi giống nhau")
else:
    if len(s1) == len(s2):
        print("Có thể chuyển đổi bằng thao tác thay thế ký tự")
    elif len(s1) < len(s2):
        print("Có thể chuyển đổi bằng thao tác thêm ký tự")
    else:
        print("Có thể chuyển đổi bằng thao tác xóa ký tự")


#5.10
s = input("Nhập xâu: ")

result = s.replace(" ", "")

print("Xâu sau khi xóa khoảng trắng:")
print(result)