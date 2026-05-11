from collections import Counter

s = input("s = ")
specials = [ch for ch in s if not ch.isalnum()]
counter = Counter(specials)

for ch, count in sorted(counter.items()):
    percent = count * 100 / len(s) if len(s) > 0 else 0
    print(ch, count, f"{percent:.2f}%")
