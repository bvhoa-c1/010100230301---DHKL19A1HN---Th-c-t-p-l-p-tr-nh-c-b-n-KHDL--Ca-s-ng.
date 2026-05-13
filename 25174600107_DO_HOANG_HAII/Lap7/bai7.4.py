text = input("Nhập đoạn văn bản tiếng Anh: ")

text = text.lower()
text = ''.join(c if c.isalpha() or c == ' ' else '' for c in text)

words = text.split()

word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print("\nThống kê tần suất từ vựng:")
print(f"{'Từ':<20} {'Tần suất':<10}")
print("-" * 30)

for word in sorted(word_freq.keys()):
    print(f"{word:<20} {word_freq[word]:<10}")

print(f"\nTổng số từ độc lập: {len(word_freq)}")
print(f"Tổng số từ: {len(words)}")
