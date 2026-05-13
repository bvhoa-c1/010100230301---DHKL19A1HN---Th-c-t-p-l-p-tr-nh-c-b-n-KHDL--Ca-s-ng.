# Bài 5.3: Tìm vị trí từ khóa và thống kê tần suất từ

text = input("Nhập chuỗi văn bản: ")
keyword = input("Nhập từ khóa: ")

# Tìm vị trí xuất hiện của từ khóa
positions = []
start = 0
while True:
    pos = text.find(keyword, start)
    if pos == -1:
        break
    positions.append(pos)
    start = pos + 1

if positions:
    print(f"Vị trí xuất hiện của '{keyword}': {positions}")
else:
    print(f"Từ khóa '{keyword}' không được tìm thấy!")

# Thống kê tần suất từ
words = text.lower().split()
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

if word_freq:
    most_frequent_word = max(word_freq, key=word_freq.get)
    print(f"Từ xuất hiện nhiều nhất: '{most_frequent_word}' ({word_freq[most_frequent_word]} lần)")
