ds = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
chan = list(filter(lambda x:x%2==0, ds))
le = list(filter(lambda x:x%2!=0, ds))
print("Số chẵn:", chan)
print("số lẻ:", le)