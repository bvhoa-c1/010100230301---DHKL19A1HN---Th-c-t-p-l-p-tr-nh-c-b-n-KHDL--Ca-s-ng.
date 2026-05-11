def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def is_perfect(x):
    s = 0
    for i in range(1, x):
        if x % i == 0:
            s += i
    return s == x

n = int(input("Nhập số phần tử: "))
arr = []
for i in range(n):
    arr.append(int(input("Nhập số: ")))
result = []
for x in arr:
    if is_prime(x) or is_perfect(x):
        result.append(x)
print("Kết quả:", result)