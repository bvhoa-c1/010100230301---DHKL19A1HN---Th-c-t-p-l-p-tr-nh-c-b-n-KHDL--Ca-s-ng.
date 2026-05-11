text = input("Nhap van ban: ")
words = text.lower().split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

max_word = max(freq, key=freq.get)
min_word = min(freq, key=freq.get)

print("Tu xuat hien nhieu nhat:", max_word)
print("So lan:", freq[max_word])

print("Tu xuat hien it nhat:", min_word)
print("So lan:", freq[min_word])