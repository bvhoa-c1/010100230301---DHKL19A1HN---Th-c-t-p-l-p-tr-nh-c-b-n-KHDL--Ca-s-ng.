text = input("Nhap chuoi van ban: ")
keyword = input("Nhap tu khoa: ")

# Tim vi tri
positions = []
start = 0

while True:
    pos = text.find(keyword, start)
    if pos == -1:
        break
    positions.append(pos)
    start = pos + 1

print("Vi tri xuat hien:", positions)

# Thong ke tan suat
words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

max_word = max(freq, key=freq.get)

print("Tu xuat hien nhieu nhat:", max_word)
print("Tan suat:", freq[max_word])