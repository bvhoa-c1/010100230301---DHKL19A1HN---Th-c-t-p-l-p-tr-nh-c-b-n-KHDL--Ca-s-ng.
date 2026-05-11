n = int(input("Nhap so sinh vien: "))

students = {}

for i in range(n):
    name = input("Nhap ten: ")
    score = float(input("Nhap diem: "))

    if score >= 8.5:
        grade = "A"
    elif score >= 7:
        grade = "B"
    elif score >= 5.5:
        grade = "C"
    elif score >= 4:
        grade = "D"
    else:
        grade = "F"

    students[name] = grade

print(students)