text = input("Nhập văn bản: ").split()
keyword = input("Nhập từ khóa: ")

# Tìm vị trí
positions = []
for i in range(len(text)):
    if text[i] == keyword:
        positions.append(i + 1)
print("Vị trí xuất hiện của từ khóa:", positions)

# Đếm tần suất
freq = {}
for word in text:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Tìm từ xuất hiện nhiều nhất
max_word = ""
max_count = 0
for word, count in freq.items():
    if count > max_count:
        max_count = count
        max_word = word
print("Từ xuất hiện nhiều nhất:", max_word, "với", max_count, "lần")