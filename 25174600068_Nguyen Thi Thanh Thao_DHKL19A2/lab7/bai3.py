xep_loai_sinh_vien = {
    "An": "A",
    "Binh": "B",
    "Cuong": "A",
    "Dung": "C",
    "Hoa": "B"
}

dem_hoc_luc = {}

for hoc_luc in xep_loai_sinh_vien.values():
    dem_hoc_luc[hoc_luc] = dem_hoc_luc.get(hoc_luc, 0) + 1

print(dem_hoc_luc)