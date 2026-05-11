# Bài 8.6: Tính tổng các ước số thực sự
def sumPdivisors(n):
    if n <= 1:
        return 0
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

# Bài 8.7: Kiểm tra cặp số amicable
def isAmicable(a, b):
    return sumPdivisors(a) == b and sumPdivisors(b) == a

# Chạy thử
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
if isAmicable(a, b):
    print(f"{a} và {b} là cặp số amicable")
else:
    print(f"{a} và {b} không là cặp số amicable")

# Tìm các cặp amicable nhỏ hơn 1000
print("\nCác cặp amicable nhỏ hơn 1000:")
for i in range(2, 1000):
    j = sumPdivisors(i)
    if j > i and j < 1000 and sumPdivisors(j) == i:
        print(f"({i}, {j})")