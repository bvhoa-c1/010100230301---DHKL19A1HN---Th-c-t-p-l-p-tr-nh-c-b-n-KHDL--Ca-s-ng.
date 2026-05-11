text = input("Nhap doan van ban: ")
text = text.lower()
for ch in ",.!?;:":
    text = text.replace(ch, "")

words = text.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Tan suat xuat hien:")
print(freq)