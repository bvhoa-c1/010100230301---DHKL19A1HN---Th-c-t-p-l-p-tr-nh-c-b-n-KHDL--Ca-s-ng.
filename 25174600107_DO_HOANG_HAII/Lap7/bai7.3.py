def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

n = int(input("Nhập số lượng sinh viên: "))

students = {}
for i in range(n):
    name = input(f"Nhập tên sinh viên thứ {i+1}: ")
    score = float(input(f"Nhập điểm của {name}: "))
    students[name] = score

grades = {name: get_grade(score) for name, score in students.items()}

grade_count = {}
for grade in grades.values():
    grade_count[grade] = grade_count.get(grade, 0) + 1

print("\nThống kê tần suất xếp loại:")
print(f"{'Xếp loại':<10} {'Số lượng':<10} {'Tỷ lệ %':<10}")
print("-" * 30)

for grade in sorted(grade_count.keys(), reverse=True):
    count = grade_count[grade]
    percentage = (count / n) * 100
    print(f"{grade:<10} {count:<10} {percentage:.2f}%")
