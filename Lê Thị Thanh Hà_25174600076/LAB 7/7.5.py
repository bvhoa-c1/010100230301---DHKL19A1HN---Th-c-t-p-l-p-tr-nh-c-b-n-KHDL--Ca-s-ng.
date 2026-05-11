text = input("Nhập đoạn văn: ")

words = text.lower().split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

max_word = max(freq, key=freq.get)
min_word = min(freq, key=freq.get)

print("Từ xuất hiện nhiều nhất:", max_word)
print("Số lần:", freq[max_word])

print("Từ xuất hiện ít nhất:", min_word)
print("Số lần:", freq[min_word])