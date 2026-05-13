# Bài 7.5: Tìm từ có tần suất cao nhất và thấp nhất

import re

text = input("Nhập đoạn văn bản tiếng Anh: ")

# Xử lý làm sạch chuỗi
text = text.lower()
text = re.sub(r'[.,!?;:\'-]', '', text)

# Tách thành các từ
words = text.split()

# Tính tần suất từ vựng
word_frequency = {}
for word in words:
    if word:
        word_frequency[word] = word_frequency.get(word, 0) + 1

if not word_frequency:
    print("Không có từ nào trong đoạn văn bản!")
else:
    # Tìm tần suất cao nhất và thấp nhất
    max_freq = max(word_frequency.values())
    min_freq = min(word_frequency.values())
    
    # Tìm các từ có tần suất cao nhất
    high_freq_words = [word for word, freq in word_frequency.items() if freq == max_freq]
    
    # Tìm các từ có tần suất thấp nhất
    low_freq_words = [word for word, freq in word_frequency.items() if freq == min_freq]
    
    print(f"\nTừ có tần suất cao nhất ({max_freq} lần):")
    print(', '.join(high_freq_words))
    
    print(f"\nTừ có tần suất thấp nhất ({min_freq} lần):")
    print(', '.join(low_freq_words))
