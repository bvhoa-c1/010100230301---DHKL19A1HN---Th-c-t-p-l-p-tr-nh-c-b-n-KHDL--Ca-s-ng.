def filter_even_odd(arr):
    even = []
    odd = []
    for x in arr:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    return even, odd
arr = [1, 2, 3, 4, 5]
even, odd = filter_even_odd(arr)
print("Chẵn:", even, "Lẻ:", odd)