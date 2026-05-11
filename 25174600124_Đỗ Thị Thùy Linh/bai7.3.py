students = {
    "An": "A",
    "Binh": "B",
    "Lan": "A",
    "Hoa": "C",
    "Minh": "B"
}

count = {}

for grade in students.values():

    if grade in count:
        count[grade] += 1
    else:
        count[grade] = 1

print("Thong ke hoc luc:")

for k, v in count.items():
    print(k, ":", v)