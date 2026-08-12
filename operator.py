#Operator 
olahraga = 30
nilai = int(input("Masaukkan nilai anda"))
alpha = 5
hadir = 30
tugas = 20

#Aritmatik
nilai_akhir = olahraga + nilai 
data_hadir = alpha - hadir 
print ("Jumlah_nilai_akhir:", nilai_akhir) 
print ("jumlah_data_hadir:", data_hadir)

#Lulus jika nilai >= 75 DAN hadir 
lulus =nilai >=75 and hadir >=30
print ("Lulus?", lulus)


#Mendapat beasiswa jika nilai .=90 Atau juara lomba 
beasiswa= nilai >=85 or olahraga > 20 
print ("Dapat beasiswa?", beasiswa)
