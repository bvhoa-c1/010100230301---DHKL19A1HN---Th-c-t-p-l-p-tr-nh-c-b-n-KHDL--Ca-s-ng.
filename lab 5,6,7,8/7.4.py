# Đếm số lần xuất hiện của từng từ trong văn bản

text = input("Nhập đoạn văn: ")

# Làm sạch chuỗi
text = text.lower()

for ch in ",.;:!?":
    text = text.replace(ch, "")

words = text.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)