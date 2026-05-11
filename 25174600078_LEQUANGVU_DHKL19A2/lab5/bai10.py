5.1

n = int(input("Nhap n: "))

binary = ""

while n > 0:
    binary = str(n % 2) + binary
    n = n // 2

print(binary)

5.2

s1 = input("Nhap chuoi 1: ")
s2 = input("Nhap chuoi 2: ")

for i in s1:
    if i in s2:
        print("Ky tu chung:", i)
        break

5.3

text = input("Nhap chuoi: ")
keyword = input("Nhap tu khoa: ")

count = text.count(keyword)

print("So lan xuat hien:", count)

5.4

s = input("Nhap chuoi: ")

number = ""

for ch in s:
    if ch.isdigit():
        number += ch

print("So sau khi loc:", number)

n = int(number)

prime = True

if n < 2:
    prime = False

for i in range(2, n):
    if n % i == 0:
        prime = False
        break

if prime:
    print("La so nguyen to")
else:
    print("Khong phai so nguyen to")

5.5

s1 = input("Nhap chuoi 1: ")
s2 = input("Nhap chuoi 2: ")

result = ""

for i in range(len(s1)):
    result += s1[i]

    if i < len(s2):
        result += "-" + s2[i] + "-"

print(result)

5.6

s = input("Nhap chuoi: ")

count = 0

for ch in s:
    if not ch.isalnum() and ch != " ":
        count += 1

print("So ky tu dac biet:", count)

percent = count / len(s) * 100

print("Phan tram:", round(percent, 2), "%")

5.7
 

s = input("Nhap chuoi: ")

thuong = hoa = so = dacbiet = 0

for ch in s:
    if ch.islower():
        thuong += 1
    elif ch.isupper():
        hoa += 1
    elif ch.isdigit():
        so += 1
    else:
        dacbiet += 1

print("Chu thuong:", thuong)
print("Chu hoa:", hoa)
print("Chu so:", so)
print("Ky tu dac biet:", dacbiet)

5.8

s = input("Nhap chuoi: ")

print("Tu vi tri 2 den 8:", s[1:8])

print("5 ky tu tu vi tri 5:", s[4:9])

print("3 ky tu cuoi:", s[-3:])

print("Chu hoa:", s.upper())

print("Chu thuong:", s.lower())

print("Dao nguoc:", s[::-1])

5.9

s1 = input("Nhap chuoi 1: ")
s2 = input("Nhap chuoi 2: ")

if s1 == s2:
    print("Hai chuoi giong nhau")
else:
    print("Can chuyen doi")

5.10

s = input("Nhap chuoi: ")

result = ""

for ch in s:
    if ch != " ":
        result += ch

print(result)