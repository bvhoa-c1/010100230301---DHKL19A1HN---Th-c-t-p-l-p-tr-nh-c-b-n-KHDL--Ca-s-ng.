# Bài 7.3: Đếm tần suất xếp loại học tức

def score_to_grade(score):
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

print("Nhập thông tin sinh viên:")
for i in range(n):
    name = input(f"Tên sinh viên {i+1}: ")
    score = float(input(f"Điểm thi của {name}: "))
    students[name] = score

# Ánh xạ điểm sang xếp loại
grades = {name: score_to_grade(score) for name, score in students.items()}

# Đếm tần suất xếp loại
grade_count = {}
for grade in grades.values():
    grade_count[grade] = grade_count.get(grade, 0) + 1

print("\nThông tin sinh viên:")
for name in students:
    print(f"{name}: {students[name]} - {grades[name]}")

print("\nBáo cáo tần suất xếp loại:")
for grade in sorted(grade_count.keys(), reverse=True):
    print(f"Xếp loại {grade}: {grade_count[grade]} sinh viên")
