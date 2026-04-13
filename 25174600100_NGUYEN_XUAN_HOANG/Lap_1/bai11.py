s = input().strip()
code = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 'J': 20,
    'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29, 'S': 30, 'T': 31,
    'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}
s = s.upper()
if len(s) != 10:
    print(0)
else:
    total = 0
    for i in range(10):
        ch = s[i]
        if i < 4:
            value = code.get(ch, 0)
        else:
            value = int(ch) if ch.isdigit() else 0
        weight = 2 ** i
        total += value * weight
    check = total % 11
    if check == 10:
        check = 0
    print(check)
