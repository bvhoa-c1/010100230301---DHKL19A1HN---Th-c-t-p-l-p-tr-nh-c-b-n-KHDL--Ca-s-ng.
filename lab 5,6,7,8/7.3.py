# Đếm số lượng sinh viên ở từng mức học lực

classified = {
    "An": "A",
    "Bình": "B",
    "Cường": "C",
    "Dung": "D",
    "Em": "F"
}

count = {}

for level in classified.values():
    count[level] = count.get(level, 0) + 1

print(count)