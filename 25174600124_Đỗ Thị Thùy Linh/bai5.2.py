str1 = input("Nhap chuoi 1: ")
str2 = input("Nhap chuoi 2: ")

found = False

for length in range(1, len(str1) + 1):

    for i in range(len(str1) - length + 1):

        sub = str1[i:i + length]

        if sub in str2:
            print("Xau con chung ngan nhat:", sub)
            found = True
            break

    if found:
        break

if not found:
    print("Khong co xau con chung")