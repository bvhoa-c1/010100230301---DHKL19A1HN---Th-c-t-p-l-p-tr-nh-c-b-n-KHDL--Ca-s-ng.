import re
from collections import Counter

text = input("text = ")
words = re.findall(r"[a-z]+(?:'[a-z]+)?", text.lower())
frequency = dict(Counter(words))

print(frequency)
