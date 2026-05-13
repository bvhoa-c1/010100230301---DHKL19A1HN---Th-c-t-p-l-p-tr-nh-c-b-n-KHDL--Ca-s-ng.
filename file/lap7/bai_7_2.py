# Bài 7.2: Từ điển sinh viên, ánh xạ điểm sang xếp loại (A-F)

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

print("\nThông tin sinh viên và xếp loại:")
for name in students:
    print(f"{name}: Điểm {students[name]} - Xếp loại: {grades[name]}")
