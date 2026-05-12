n = int(input("Nhập số sinh viên: "))

students = {}

for i in range(n):
    name = input("Nhập tên sinh viên: ")
    score = float(input("Nhập điểm: "))
    students[name] = score

print("\nXếp loại:")

for name, score in students.items():
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

    print(name, ":", rank)

