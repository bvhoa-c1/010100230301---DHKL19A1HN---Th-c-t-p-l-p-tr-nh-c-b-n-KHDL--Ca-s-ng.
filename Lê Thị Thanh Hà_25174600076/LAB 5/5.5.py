s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")

result = ""

min_len = min(len(s1), len(s2))

for i in range(min_len):
    result += s1[i] + s2[i]

result += s1[min_len:] + s2[min_len:]

print("Kết quả:", "-".join(result))
