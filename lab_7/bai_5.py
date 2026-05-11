import re
from collections import Counter

text = input("text = ")
words = re.findall(r"[a-z]+(?:'[a-z]+)?", text.lower())
frequency = Counter(words)

if not frequency:
    print([], [])
else:
    highest = max(frequency.values())
    lowest = min(frequency.values())
    highest_words = sorted(word for word, count in frequency.items() if count == highest)
    lowest_words = sorted(word for word, count in frequency.items() if count == lowest)
    print(highest_words, highest)
    print(lowest_words, lowest)
