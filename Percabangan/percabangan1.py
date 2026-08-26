# Contoh : Kategori Nilai
nilai = int(input("Masukkan nilai(0-100)"))

if nilai >= 90:
    kategori = "A (Sangan Baik)"
elif nilai >=80:
    kategori = "B (baik)"
elif nilai >=70:
    kategori = "C (cukup)"
elif nilai >=60:
    kategori = "D (kurang)"
else:
    kategori = "E (sangant kurang)"

print("Nilai :",nilai)
print ("Kategori:", kategori)
