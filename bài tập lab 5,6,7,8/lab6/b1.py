n = int(input("Nhập số phần tử: "))
arr = []
for i in range(n):
    arr.append(int(input("Nhập số: ")))
sum_even = sum_odd = 0
for x in arr:
    if x % 2 == 0:
        sum_even += x
    else:
        sum_odd += x
print("Tổng chẵn:", sum_even)
print("Tổng lẻ:", sum_odd)