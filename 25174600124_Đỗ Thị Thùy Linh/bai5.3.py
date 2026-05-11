text = input("Nhap chuoi: ")
key = input("Nhap tu khoa: ")

pos = text.find(key)

if pos != -1:
    print("Vi tri xuat hien:", pos)
else:
    print("Khong tim thay")

words = text.split()

freq = {}

for word in words:

    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

max_word = max(freq, key=freq.get)

print("Tu xuat hien nhieu nhat:",
      max_word,
      "-",
      freq[max_word],
      "lan")