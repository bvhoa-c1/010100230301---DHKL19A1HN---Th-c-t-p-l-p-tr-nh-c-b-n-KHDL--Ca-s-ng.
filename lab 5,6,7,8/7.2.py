# Lưu tên và điểm sinh viên, xếp loại từ A đến F

students = {
    "An": 9.2,
    "Bình": 7.8,
    "Cường": 6.4,
    "Dung": 5.1,
    "Em": 3.9
}

rank = {}

for name, score in students.items():
    if score >= 8.5:
        rank[name] = "A"
    elif score >= 7:
        rank[name] = "B"
    elif score >= 5.5:
        rank[name] = "C"
    elif score >= 4:
        rank[name] = "D"
    else:
        rank[name] = "F"

print(rank)