s = input("Nhập xâu: ")
result = ""
for ch in s:
    if ch != " ":
        result += ch
print("Xâu không khoảng trắng:", result)