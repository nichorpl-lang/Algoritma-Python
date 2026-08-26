# Contoh: Kategori Nilai
nilai = int(input("Masukan Nilai (0-100): "))

if nilai >= 90:
    kategori = "A (Sangat baik)"
elif nilai >=80:
    kategori = "B (Baik)"
elif nilai >=70:
    kategori = "C (Cukup)"
elif nilai >=60:
    kategori = "D (Kurang)"
else:
    kategori = "E (Sangat kurang)"

print ("Nilai :", nilai)
print ("Kategori:", kategori)