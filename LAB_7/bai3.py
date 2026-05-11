students = {
    "An": "A",
    "Binh": "B",
    "Cuong": "A",
    "Dung": "C",
    "Ha": "B"
}

count = {}

for rank in students.values():
    count[rank] = count.get(rank, 0) + 1

print("Thong ke hoc luc:")
print(count)