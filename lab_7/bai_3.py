from collections import Counter

def classify(score):
    if score > 10:
        score /= 10
    if score >= 8.5:
        return "A"
    if score >= 7.0:
        return "B"
    if score >= 5.5:
        return "C"
    if score >= 4.0:
        return "D"
    return "F"

n = int(input("n = "))
students = {}

for _ in range(n):
    name = input("name = ")
    score = float(input("score = "))
    students[name] = score

grades = {name: classify(score) for name, score in students.items()}
frequency = dict(Counter(grades.values()))

print(grades)
print(frequency)
