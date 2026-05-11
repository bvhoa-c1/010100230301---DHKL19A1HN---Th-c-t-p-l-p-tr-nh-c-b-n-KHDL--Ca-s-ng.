s = input("Nhap chuoi: ")

special = {}

for c in s:

    if not c.isalnum() and c != " ":

        if c in special:
            special[c] += 1
        else:
            special[c] = 1

length = len(s)

for k, v in special.items():

    percent = v / length * 100

    print(k, ":", v, "lan",
          f"({percent:.2f}%)")