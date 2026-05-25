n = int(input())
def gt(n):

    g_t = 1
    for i in range(1 , n +1):
        g_t *= i
    return g_t
print(gt(n))