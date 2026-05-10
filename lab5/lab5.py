#bài 5.1
n = int(input("Nhap so nguyen duong: "))

binary = bin(n)[2:]

print("Dang nhi phan:", binary)
#bài 5.2
str1 = input("Nhap chuoi 1: ")
str2 = input("Nhap chuoi 2: ")

result = ""

for length in range(1, min(len(str1), len(str2)) + 1):
    found = False

    for i in range(len(str1) - length + 1):
        sub = str1[i:i+length]

        if sub in str2:
            result = sub
            found = True
            break

    if found:
        break

if result:
    print("Xau con chung ngan nhat:", result)
else:
    print("Khong co")

#bài 5.3
text = input("Nhap chuoi: ")
keyword = input("Nhap tu khoa: ")

# tim vi tri
pos = text.find(keyword)

while pos != -1:
    print("Xuat hien tai:", pos)
    pos = text.find(keyword, pos + 1)

# thong ke
words = text.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

max_word = max(freq, key=freq.get)

print("Tu xuat hien nhieu nhat:", max_word)
print("So lan:", freq[max_word])

#bài 5.4
s = input("Nhap chuoi: ")

number_str = ""

for c in s:
    if c.isdigit():
        number_str += c

n = int(number_str)

print("So sau khi loc:", n)


def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False

    return True


if is_prime(n):
    print("La so nguyen to")
else:
    print("Khong la so nguyen to")

#bài 5.5
s1 = input("Nhap chuoi 1: ")
s2 = input("Nhap chuoi 2: ")

result = []

max_len = max(len(s1), len(s2))

for i in range(max_len):

    if i < len(s1):
        result.append(s1[i])

    if i < len(s2):
        result.append(s2[i])

print("-".join(result))

#bài 5.6
s = input("Nhap chuoi: ")

special = {}

for c in s:

    if not c.isalnum():

        special[c] = special.get(c, 0) + 1

for k, v in special.items():

    percent = v / len(s) * 100

    print(k, ":", v, "lan,", round(percent,2), "%")

#bài 5.7
s = input("Nhap chuoi: ")

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

print("Chu thuong:", lower)
print("Chu hoa:", upper)
print("Chu so:", digit)
print("Ky tu dac biet:", special)

#bài 5.8
s = input("Nhap chuoi: ")

if len(s) > 10:

    print("Vi tri 2->8:", s[2:9])

    print("5 ky tu tu vi tri 5:", s[5:10])

    print("3 ky tu cuoi:", s[-3:])

    print("In hoa:", s.upper())

    print("In thuong:", s.lower())

    print("Dao nguoc:", s[::-1])

else:
    print("Chuoi khong du do dai")

#bài 5.9
s1 = input("Nhap chuoi 1: ")
s2 = input("Nhap chuoi 2: ")

m = len(s1)
n = len(s2)

dp = [[0]*(n+1) for _ in range(m+1)]

for i in range(m+1):
    dp[i][0] = i

for j in range(n+1):
    dp[0][j] = j


for i in range(1, m+1):

    for j in range(1, n+1):

        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]

        else:
            dp[i][j] = 1 + min(
                dp[i-1][j],
                dp[i][j-1],
                dp[i-1][j-1]
            )

print("So thao tac toi thieu:", dp[m][n])

#bài 5.10
s = input("Nhap chuoi: ")

result = s.replace(" ", "")

print("Ket qua:", result)
