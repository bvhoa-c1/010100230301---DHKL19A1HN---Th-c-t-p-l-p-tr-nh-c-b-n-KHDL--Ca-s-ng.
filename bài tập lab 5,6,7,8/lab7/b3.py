# Bài 7.2 + 7.3 gộp lại để chạy liên tục
students = {}
n = int(input("Số sinh viên: "))
for i in range(n):
    name = input("Tên sinh viên: ")
    score = float(input("Điểm: "))
    students[name] = score

# Phân loại học lực
grades = {}
for name, score in students.items():
    if score >= 90:
        grades[name] = "A"
    elif score >= 80:
        grades[name] = "B"
    elif score >= 70:
        grades[name] = "C"
    elif score >= 60:
        grades[name] = "D"
    else:
        grades[name] = "F"

# Bài 7.3: Đếm số lượng theo từng mức học lực
count_grade = {}
for g in grades.values():
    if g in count_grade:
        count_grade[g] += 1
    else:
        count_grade[g] = 1

print("Phân loại học lực từng sinh viên:", grades)
print("Số lượng theo từng mức:", count_grade)