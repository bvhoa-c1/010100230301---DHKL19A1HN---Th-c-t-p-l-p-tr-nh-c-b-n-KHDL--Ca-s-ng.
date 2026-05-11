ds = [1, 2, 3, 5, 7, 8, 9]
chan = list(filter(lambda x:x%2 == 0, ds))
le = list(filter(lambda x:x%2 != 0, ds))
lap_phuong_chan = list(map(lambda x: x**3, chan))
binh_phuong_le = list(map(lambda x:x**2, le))
print("lập phương số chẵn:", lap_phuong_chan)
print("Bình phương số lẻ:", binh_phuong_le)