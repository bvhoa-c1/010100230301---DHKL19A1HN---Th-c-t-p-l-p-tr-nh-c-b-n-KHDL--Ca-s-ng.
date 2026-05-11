text = input("Nhập văn bản: ").lower()
punctuation = ".,!?;:()\"'"
for p in punctuation:
    text = text.replace(p, " ")
words = text.split()
freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
print(freq)