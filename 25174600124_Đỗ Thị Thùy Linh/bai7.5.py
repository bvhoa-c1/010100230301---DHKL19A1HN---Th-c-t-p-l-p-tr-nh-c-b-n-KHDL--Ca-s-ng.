text = input("Nhap van ban: ")

text = text.lower()

for c in ",.!?;:":
    text = text.replace(c, "")

words = text.split()

freq = {}

for word in words:

    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

max_word = max(freq, key=freq.get)
min_word = min(freq, key=freq.get)

print("Tu xuat hien nhieu nhat:")
print(max_word, "-", freq[max_word], "lan")

print("Tu xuat hien it nhat:")
print(min_word, "-", freq[min_word], "lan")