n = int(input("Nhập số sinh viên: "))

count = {
    "Giỏi": 0,
    "Khá": 0,
    "Trung bình": 0,
    "Yếu": 0
}

for i in range(n):
    score = float(input(f"Nhập điểm sinh viên {i+1}: "))

    if score >= 8:
        count["Giỏi"] += 1
    elif score >= 6.5:
        count["Khá"] += 1
    elif score >= 5:
        count["Trung bình"] += 1
    else:
        count["Yếu"] += 1

print(count)

