text = input("Nhập chuỗi văn bản: ")
keyword = input("Nhập từ khóa tìm kiếm: ")

positions = []
start = 0
while True:
    pos = text.find(keyword, start)
    if pos == -1:
        break
    positions.append(pos)
    start = pos + 1

if positions:
    print(f"Từ khóa '{keyword}' xuất hiện tại vị trí: {positions}")
    print(f"Tổng số lần xuất hiện: {len(positions)}")
else:
    print(f"Từ khóa '{keyword}' không xuất hiện trong chuỗi!")

words = text.lower().split()
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

if word_freq:
    max_word = max(word_freq, key=word_freq.get)
    max_count = word_freq[max_word]
    print(f"\nTừ xuất hiện với tần suất cao nhất: '{max_word}'")
    print(f"Tần suất: {max_count} lần")
else:
    print("Chuỗi rỗng!")
