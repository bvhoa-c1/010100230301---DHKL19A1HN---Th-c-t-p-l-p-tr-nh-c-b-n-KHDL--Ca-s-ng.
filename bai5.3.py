# Tìm kiếm và thống kê tần suất từ khóa trong chuỗi

text = input("Nhập chuỗi văn bản: ")
keyword = input("Nhập từ khóa cần tìm: ")

# Chuyển về chữ thường để tìm chính xác hơn
text_lower = text.lower()
keyword_lower = keyword.lower()

# Tách các từ trong chuỗi
words = text_lower.split()

# Đếm số lần xuất hiện của từ khóa
count_keyword = words.count(keyword_lower)

print("Từ khóa xuất hiện", count_keyword, "lần")

# Thống kê tần suất các từ
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Tìm từ xuất hiện nhiều nhất
max_word = ""
max_count = 0

for word in frequency:
    if frequency[word] > max_count:
        max_count = frequency[word]
        max_word = word

print("Từ xuất hiện nhiều nhất là:", max_word)
print("Số lần xuất hiện:", max_count)