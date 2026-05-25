bi = "this girl made me feel like less of a man 'cause I'm feeling depressed and stuff"
bi_2 = "damn it that fukkin crazy zzz "
huh = []
a = bi.split()
b = bi_2.split()
for i in a:
    for j in b:
        if len(i) == len(j):
            huh.append((i , j))
print(huh)