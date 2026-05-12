s1 =input("nhap chuoi 1:")
s2 = input("nhap chuoi 2:")
ket_qua=""
do_dai_ngan = min(len(s1), len(s2))
for i in range(do_dai_ngan):
    ket_qua += s1[i] +s2[i]+"-"

phan_thua= s1[do_dai_ngan:]+ s2[do_dai_ngan:]
if phan_thua:
    ket_qua += "-".join(phan_thua)
else:
    ket_qua = ket_qua[:-1]
print(ket_qua)