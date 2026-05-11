xep_loai = {
    "A": "F",
    "B": "B",
    "C": "B",
    "M": "D",
    "H": "A"
}
dem = {}
for loai in xep_loai.values():
    dem[loai] = dem.get(loai, 0) + 1
print("Số lượng từng học lực: ")
for loai in dem:
    print(loai, ":", dem[loai])