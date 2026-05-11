n = int(input("Nhap so sinh vien: "))

students = {}

for i in range(n):
    name = input("Nhap ten: ")
    score = float(input("Nhap diem: "))

    if score >= 8.5:
        rank = "A"
    elif score >= 7:
        rank = "B"
    elif score >= 5.5:
        rank = "C"
    elif score >= 4:
        rank = "D"
    else:
        rank = "F"

    students[name] = {
        "diem": score,
        "xeploai": rank
    }

print(students)