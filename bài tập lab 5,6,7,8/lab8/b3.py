# Bài 8.2: Hàm tính giai thừa
def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Bài 8.3: Hoán vị và tổ hợp
def permutation(n, r):
    if r > n or r < 0:
        return 0
    return factorial(n) // factorial(n - r)

def combination(n, r):
    if r > n or r < 0:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

# Chạy thử
n = int(input("Nhập n: "))
r = int(input("Nhập r: "))
print(f"P({n},{r}) =", permutation(n, r))
print(f"C({n},{r}) =", combination(n, r))