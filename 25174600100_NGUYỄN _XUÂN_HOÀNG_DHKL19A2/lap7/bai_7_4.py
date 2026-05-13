# Bài 7.4: Phân tích văn bản tiếng Anh

import re

text = input("Nhập đoạn văn bản tiếng Anh: ")

# Xử lý làm sạch chuỗi
# Chuyển thành chữ thường
text = text.lower()

# Loại bỏ dấu câu
text = re.sub(r'[.,!?;:\'-]', '', text)

# Tách thành các từ
words = text.split()

# Lưu trữ tần suất từ vựng
word_frequency = {}
for word in words:
    if word:  # Bỏ qua từ rỗng
        word_frequency[word] = word_frequency.get(word, 0) + 1

print(f"\nTổng số từ: {len(words)}")
print(f"Số từ riêng biệt: {len(word_frequency)}")

print("\nTần suất từ vựng:")
for word in sorted(word_frequency.items(), key=lambda x: x[1], reverse=True):
    print(f"'{word[0]}': {word[1]} lần")
