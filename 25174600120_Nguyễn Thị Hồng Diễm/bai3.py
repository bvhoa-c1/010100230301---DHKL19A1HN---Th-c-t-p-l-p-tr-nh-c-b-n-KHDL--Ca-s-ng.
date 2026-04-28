#a
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == "__main__":
    n = int(input("Nhập số nguyên dương n (kiểm tra nguyên tố): ").strip())
    print(f"{n} là số nguyên tố" if is_prime(n) else f"{n} không phải số nguyên tố")
#b
def is_perfect(n: int) -> bool:
    if n <= 1:
        return False
    s = 1  
    i = 2
    while i * i <= n:
        if n % i == 0:
            s += i
            j = n // i
            if j != i:
                s += j
        i += 1
    return s == n

if __name__ == "__main__":
    n = int(input("Nhập số nguyên dương n (kiểm tra hoàn hảo): ").strip())
    print(f"{n} là số hoàn hảo" if is_perfect(n) else f"{n} không phải số hoàn hảo")
#c
def is_palindrome_number(n: int) -> bool:
    s = str(n)
    return s == s[::-1]

def print_palindromes_upto_1000():
    count_in_line = 0
    max_per_line = 15
    for n in range(1, 1001):  
        if is_palindrome_number(n):
            print(f"{n:5d}", end='')
            count_in_line += 1
            if count_in_line == max_per_line:
                print()  
                count_in_line = 0
    if count_in_line != 0:
        print()  

if __name__ == "__main__":
    print_palindromes_upto_1000()
