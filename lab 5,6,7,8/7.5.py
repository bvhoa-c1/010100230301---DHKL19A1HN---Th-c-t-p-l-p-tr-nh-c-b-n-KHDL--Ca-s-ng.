# Tìm từ xuất hiện nhiều nhất và ít nhất

text = input("Nhập đoạn văn: ")

text = text.lower()

for ch in ",.;:!?":
    text = text.replace(ch, "")

words = text.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

max_word = max(freq, key=freq.get)
min_word = min(freq, key=freq.get)

print("Từ xuất hiện nhiều nhất:", max_word, "-", freq[max_word])
print("Từ xuất hiện ít nhất:", min_word, "-", freq[min_word])