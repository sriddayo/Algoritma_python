berat = int(input("masukkan berat badan anda (kg):"))
tinggi = int(input("masukkan tinggi badan anda (m):"))
bmi = berat / tinggi ** 2 ;

print ("berat badan:", berat,"kg")
print ("tinggi bandan:", tinggi,"m")

if bmi  < 18.5:
    print ("Keterangan : perlu tambah berat badan")
elif bmi < 25: 
    print ("keterangan : pertahankan gaya hidup sehat")
elif bmi < 30:
    print ("keterangan : perlu olahraga lebih")
elif bmi:
    print ("keterangan : konsultasi tokter")