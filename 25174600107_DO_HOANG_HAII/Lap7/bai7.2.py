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

print("\nThông tin sinh viên:")
print(f"{'Tên':<20} {'Điểm':<10} {'Xếp loại':<10}")
print("-" * 40)

for name in students:
    print(f"{name:<20} {students[name]:<10.2f} {grades[name]:<10}")
