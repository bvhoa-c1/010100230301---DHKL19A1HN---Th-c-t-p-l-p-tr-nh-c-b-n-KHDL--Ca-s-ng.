text = input("Nhập đoạn văn bản tiếng Anh: ")

text = text.lower()
text = ''.join(c if c.isalpha() or c == ' ' else '' for c in text)

words = text.split()

word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

max_word = max(word_freq, key=word_freq.get)
min_word = min(word_freq, key=word_freq.get)

max_freq = word_freq[max_word]
min_freq = word_freq[min_word]

print("\nThống kê tần suất từ vựng:")
print(f"{'Từ':<20} {'Tần suất':<10}")
print("-" * 30)

for word in sorted(word_freq.keys()):
    print(f"{word:<20} {word_freq[word]:<10}")

print(f"\nTừ có tần suất cao nhất: '{max_word}' ({max_freq} lần)")
print(f"Từ có tần suất thấp nhất: '{min_word}' ({min_freq} lần)")
