# BÀI TẬP:
# LAB 5:
# BÀI 5.1:
n = int(input("Nhập số nguyên dương: "))
print("Dạng nhị phân:", bin(n)[2:])
# Bài 5.2: Tìm chuỗi con chung ngắn nhất giữa 2 chuỗi

str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")

found = False

for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        sub = str1[i:j]
        if sub in str2:
            print("Chuỗi con chung ngắn nhất:", sub)
            found = True
            break
    if found:
        break

if not found:
    print("Không có chuỗi con chung")
# Bài 5.3: Tìm kiếm và thống kê tần suất từ

text = input("Nhập chuỗi văn bản: ")
keyword = input("Nhập từ khóa: ")

words = text.split()

count = words.count(keyword)
print("Tần suất của từ khóa:", count)

max_word = ""
max_count = 0

for w in words:
    c = words.count(w)
    if c > max_count:
        max_count = c
        max_word = w

print("Từ xuất hiện nhiều nhất:", max_word)
print("Số lần xuất hiện:", max_count)
# Bài 5.4: Loại bỏ ký tự không phải số và kiểm tra số nguyên tố

s = input("Nhập chuỗi: ")

num_str = ""

for ch in s:
    if ch.isdigit():
        num_str += ch

if num_str == "":
    print("Không có chữ số")
else:
    n = int(num_str)
    print("Số sau khi xử lý:", n)

    if n < 2:
        print("Không phải số nguyên tố")
    else:
        prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prime = False
                break

        if prime:
            print("Là số nguyên tố")
        else:
            print("Không phải số nguyên tố")
# Bài 5.5: Trộn hai chuỗi

s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")

result = ""

min_len = min(len(s1), len(s2))

for i in range(min_len):
    result += s1[i] + s2[i]

result += s1[min_len:] + s2[min_len:]

print("Chuỗi sau khi trộn:", result)
# Bài 5.6: Đếm ký tự đặc biệt và tính phần trăm

s = input("Nhập chuỗi: ")

special = {}

for ch in s:
    if not ch.isalnum() and ch != " ":
        if ch in special:
            special[ch] += 1
        else:
            special[ch] = 1

total = len(s)

for k, v in special.items():
    percent = v / total * 100
    print(k, "xuất hiện", v, "lần -", round(percent, 2), "%")
# Bài 5.7: Thống kê chữ thường, in hoa, số và ký tự đặc biệt

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
print("Chữ in hoa:", upper)
print("Chữ số:", digit)
print("Ký tự đặc biệt:", special)
# Bài 5.8: Xử lý chuỗi

s = input("Nhập chuỗi: ")

if len(s) > 10:
    print("Từ vị trí 2 đến 8:", s[2:9])
    print("5 ký tự từ vị trí 5:", s[5:10])
    print("3 ký tự cuối:", s[-3:])
    print("Chữ hoa:", s.upper())
    print("Chữ thường:", s.lower())
else:
    print("Chuỗi phải dài hơn 10 ký tự")
# Bài 5.9: Kiểm tra khả năng biến đổi chuỗi

s1 = input("Chuỗi ban đầu: ")
s2 = input("Chuỗi mục tiêu: ")

if s1 == s2:
    print("Hai chuỗi giống nhau")
elif abs(len(s1) - len(s2)) <= 1:
    print("Có thể biến đổi bằng thêm/xóa/thay thế ký tự")
else:
    print("Khó biến đổi")
# Bài 5.10: Xóa khoảng trắng trong chuỗi

s = input("Nhập chuỗi: ")

result = s.replace(" ", "")

print("Chuỗi sau khi xóa khoảng trắng:", result)

# LAB 6:
# BÀI 6.1

n = int(input("Nhập số phần tử: "))

a = []

for i in range(n):
    x = int(input(f"a[{i}] = "))
    a.append(x)

chan = []
le = []

for x in a:
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)

print("Danh sách số chẵn:", chan)
print("Tổng số chẵn:", sum(chan))

print("Danh sách số lẻ:", le)
print("Tổng số lẻ:", sum(le))


# BÀI 6.2

n = int(input("\nNhập số phần tử: "))
a = []

for i in range(n):
    a.append(int(input()))

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def is_perfect(x):
    s = 0
    for i in range(1, x):
        if x % i == 0:
            s += i
    return s == x

print("Các số nguyên tố hoặc hoàn hảo:")

for x in a:
    if is_prime(x) or is_perfect(x):
        print(x, end=" ")


# BÀI 6.3

n = int(input("\n\nNhập số phần tử: "))

a = []

for i in range(n):
    x = float(input())
    a.append(x)

print("Giá trị lớn nhất:", max(a))
print("Giá trị nhỏ nhất:", min(a))


# BÀI 6.4

n = int(input("\nNhập n: "))

fib = [0, 1]

for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

result = [fib[i] for i in range(n)]

print(result)


# BÀI 6.5

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

prime_list = [x for x in range(100) if is_prime(x)]

print(prime_list)


# BÀI 6.6

n = int(input("\nNhập số phần tử: "))

a = []

for i in range(n):
    a.append(int(input()))

d = a[1] - a[0]

check = True

for i in range(1, n - 1):
    if a[i+1] - a[i] != d:
        check = False
        break

if check:
    print("Dãy là cấp số cộng")
else:
    print("Dãy không phải cấp số cộng")


# BÀI 6.7

m = int(input("\nNhập số hàng: "))
n = int(input("Nhập số cột: "))

a = []

for i in range(m):
    row = list(map(int, input().split()))
    a.append(row)

tong = 0

for row in a:
    tong += sum(row)

print("Tổng ma trận:", tong)


# BÀI 6.8

m = int(input("\nNhập số hàng ma trận A: "))
n = int(input("Nhập số cột ma trận A = số hàng ma trận B: "))
p = int(input("Nhập số cột ma trận B: "))

print("Nhập ma trận A:")
A = []

for i in range(m):
    A.append(list(map(int, input().split())))

print("Nhập ma trận B:")
B = []

for i in range(n):
    B.append(list(map(int, input().split())))

C = [[0 for j in range(p)] for i in range(m)]

for i in range(m):
    for j in range(p):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

print("Ma trận tích:")

for row in C:
    print(row)


# BÀI 6.9

n = int(input("\nNhập cấp ma trận vuông: "))

A = []

for i in range(n):
    A.append(list(map(int, input().split())))

AT = []

for j in range(n):
    row = []
    for i in range(n):
        row.append(A[i][j])
    AT.append(row)

print("Ma trận chuyển vị:")

for row in AT:
    print(row)

if A == AT:
    print("Ma trận đối xứng")
else:
    print("Ma trận không đối xứng")


# BÀI 6.10

import numpy as np

n = int(input("\nNhập cấp ma trận: "))

A = []

for i in range(n):
    A.append(list(map(float, input().split())))

A = np.array(A)

det = np.linalg.det(A)

if det == 0:
    print("Ma trận không khả nghịch")
else:
    inv = np.linalg.inv(A)

    print("Ma trận nghịch đảo:")
    print(inv)
# LAB 7:
# BÀI 7.1

N = int(input("Nhập N: "))

d = {}

for x in range(1, N + 1):
    d[x] = x**3

print(d)


# BÀI 7.2

students = {}

n = int(input("\nNhập số sinh viên: "))

for i in range(n):
    name = input("Tên sinh viên: ")
    score = float(input("Điểm: "))

    if score >= 8.5:
        rank = "A"
    elif score >= 7:
        rank = "B"
    elif score >= 5.5:
        rank = "C"
    elif score >= 4:
        rank = "D"
    else:
        rank = "F"

    students[name] = rank

print(students)


# BÀI 7.3

count_rank = {}

for rank in students.values():
    if rank in count_rank:
        count_rank[rank] += 1
    else:
        count_rank[rank] = 1

print("Số lượng từng học lực:")
print(count_rank)


# BÀI 7.4

text = input("\nNhập đoạn văn tiếng Anh: ")

text = text.lower()

for ch in ",.!?;:":
    text = text.replace(ch, "")

words = text.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)


# BÀI 7.5

max_word = max(freq, key=freq.get)
min_word = min(freq, key=freq.get)

print("Từ xuất hiện nhiều nhất:", max_word, "-", freq[max_word], "lần")
print("Từ xuất hiện ít nhất:", min_word, "-", freq[min_word], "lần")


# BÀI 7.6

inventory = {
    "gold": 500,
    "backpack": ["sword", "shield"],
}

inventory["pocket"] = ["flint", "twine", "gemstone"]

inventory["gold"] += 50

print(inventory)


# BÀI 7.7

inventory["backpack"].sort()

item_remove = input("\nNhập vật phẩm cần xóa: ")

if item_remove in inventory["backpack"]:
    inventory["backpack"].remove(item_remove)

print(inventory["backpack"])


# BÀI 7.8

quantity = {
    "Bút": 10,
    "Vở": 5,
    "Thước": 3
}

price = {
    "Bút": 5000,
    "Vở": 12000,
    "Thước": 8000
}

print("\nHÓA ĐƠN")

total = 0

for item in quantity:
    cost = quantity[item] * price[item]
    total += cost

    print(item, ":", quantity[item], "x", price[item], "=", cost)

print("Tổng tiền:", total)


# BÀI 7.9

sell_item = input("\nNhập mặt hàng bán: ")
sell_quantity = int(input("Nhập số lượng bán: "))

if sell_item in quantity:
    quantity[sell_item] -= sell_quantity

print("Tồn kho sau cập nhật:")
print(quantity)


# BÀI 7.10

warehouse = {"Bút", "Vở", "Thước", "Tẩy", "Compa"}

customer = {"Bút", "Thước"}

not_buy = warehouse - customer

print("Sản phẩm chưa được mua:")
print(not_buy)
# LAB 8:
# BÀI 8.1

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

print("Các cặp số nguyên tố sinh đôi < 1000:")

for i in range(2, 1000):
    if is_prime(i) and is_prime(i + 2):
        print((i, i + 2))


# BÀI 8.2

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

n = int(input("\nNhập n: "))

print("Giai thừa:", factorial(n))


# BÀI 8.3

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

n = int(input("\nNhập n: "))
r = int(input("Nhập r: "))

permutation = factorial(n) // factorial(n - r)
combination = factorial(n) // (factorial(r) * factorial(n - r))

print("Hoán vị:", permutation)
print("Tổ hợp:", combination)


# BÀI 8.4
def cubesum(n):
    tong_lap_phuong = 0
    while n > 0:
        thanh_phan = n % 10
        tong_lap_phuong += thanh_phan**3
        n //= 10
    return tong_lap_phuong

n = int(input("Nhập số: "))
print("Tổng lập phương chữ số:", cubesum(n))

# BÀI 8.5
def cubesum(n):
    tong_lap_phuong = 0
    temp = n
    while temp > 0:
        thanh_phan = temp % 10
        tong_lap_phuong += thanh_phan**3
        temp //= 10
    return tong_lap_phuong

def isArmstrong(n):
    return cubesum(n) == n

print("Các số Armstrong < 1000:")
for i in range(1000):
    if isArmstrong(i):
        print(i, end=" ")

# BÀI 8.6
def sumDivisors(n):
    uoc_cua_n = 0
    for i in range(1, n):
        if n % i == 0:
            uoc_cua_n += i
    return uoc_cua_n
n = int(input("Nhập số: "))
print("Tổng ước số thực sự:", sumDivisors(n))

# BÀI 8.7
def sumDivisors(n):
    uoc_cua_n = 0
    for i in range(1, n):
        if n % i == 0:
            uoc_cua_n += i
    return uoc_cua_n

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
if sumDivisors(a) == b and sumDivisors(b) == a:
    print("Là cặp Amicable")
else:
    print("Không phải cặp Amicable")

# BÀI 8.8
tap_hop = [1, 2, 3, 4, 5, 6, 7, 8]

so_chan = filter(lambda x: x % 2 == 0, tap_hop)
print("Số chẵn:", list(so_chan))

so_le = filter(lambda x: x % 2 != 0, tap_hop)
print("Số lẻ:", list(so_le))

# BÀI 8.9
tap_hop = [1, 2, 3, 4, 5]

lap_phuong = map(lambda x: x**3, tap_hop)
print("Danh sách lập phương:", list(lap_phuong))

# BÀI 8.10
tap_hop = [1, 2, 3, 4, 5, 6]

so_chan = filter(lambda x: x % 2 == 0, tap_hop)
lap_phuong = map(lambda x: x**3, so_chan)
print("Lập phương số chẵn:", list(lap_phuong))

so_le = filter(lambda x: x % 2 != 0, tap_hop)
binh_phuong = map(lambda x: x**2, so_le)
print("Bình phương số lẻ:", list(binh_phuong))
