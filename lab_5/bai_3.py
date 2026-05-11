import re
from collections import Counter

text = input("text = ")
keyword = input("keyword = ")

positions = []
start = 0

while True:
    index = text.find(keyword, start)
    if index == -1:
        break
    positions.append(index)
    start = index + 1

words = re.findall(r"[A-Za-z0-9_]+", text.lower())
counter = Counter(words)

print(positions)

if counter:
    max_count = max(counter.values())
    result = sorted(word for word, count in counter.items() if count == max_count)
    print(result, max_count)
else:
    print([], 0)
