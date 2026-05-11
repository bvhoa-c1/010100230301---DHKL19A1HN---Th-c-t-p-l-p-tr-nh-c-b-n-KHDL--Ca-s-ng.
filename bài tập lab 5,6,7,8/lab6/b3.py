n = int(input("Nhập số phần tử: "))
arr = []
for i in range(n):
    arr.append(float(input("Nhập số: ")))
max_val = arr[0]
min_val = arr[0]
for x in arr:
    if x > max_val:
        max_val = x
    if x < min_val:
        min_val = x
print("Max:", max_val, "Min:", min_val)