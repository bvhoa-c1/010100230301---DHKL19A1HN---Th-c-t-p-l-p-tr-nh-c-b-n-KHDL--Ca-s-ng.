text = input("Nhập đoạn văn: ")

words = text.lower().split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Tần suất xuất hiện:")

for word, count in freq.items():
    print(word, ":", count)