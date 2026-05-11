# Bài 7.4 + 7.5 gộp lại
text = input("Nhập đoạn văn bản: ").lower()

# Loại bỏ dấu câu đơn giản
cleaned = ""
for ch in text:
    if ch.isalpha() or ch == " ":
        cleaned += ch

words = cleaned.split()

# Đếm tần suất từ
freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

# Bài 7.5: Tìm từ xuất hiện nhiều nhất và ít nhất
max_word = ""
max_count = 0
min_word = ""
min_count = float("inf")

for w, c in freq.items():
    if c > max_count:
        max_count = c
        max_word = w
    if c < min_count:
        min_count = c
        min_word = w

print("Từ xuất hiện nhiều nhất:", max_word, "với", max_count, "lần")
print("Từ xuất hiện ít nhất:", min_word, "với", min_count, "lần")