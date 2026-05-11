students = {}
n = int(input("Số sinh viên: "))
for i in range(n):
    name = input("Tên: ")
    score = int(input("Điểm: "))
    students[name] = score
grades = {}
for name, score in students.items():
    if score >= 90:
        grades[name] = 'A'
    elif score >= 80:
        grades[name] = 'B'
    elif score >= 70:
        grades[name] = 'C'
    elif score >= 60:
        grades[name] = 'D'
    else:
        grades[name] = 'F'
print(grades)