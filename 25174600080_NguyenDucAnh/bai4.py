# a
def P_a(n):
    result = 1
    for i in range(n + 1):
        result *= (2 * i + 1)
    return result


# b) 
def S_b(n):
    result = 0
    for i in range(1, n + 1):
        result += (-1) ** (i + 1) * i
    return result


# c) 
def S_c(n):
    result = 0
    for i in range(1, n + 1):
        result += sum(range(1, i + 1))
    return result


# d) 
def P_d(x, y):
    return x ** y



if __name__ == "__main__":
    n = 5
    print("a) P(n) =", P_a(n))
    print("b) S(n) =", S_b(n))
    print("c) S(n) =", S_c(n))
    print("d) P(x,y) =", P_d(2, 3))