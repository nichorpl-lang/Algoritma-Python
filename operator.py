# operator
IPAS = 38
Nilai = int(input("Masukan nilai anda:"))
alpha = 3
hadir = 40
tugas = 25

# Aritmatika
nilai_akhir = IPAS + Nilai
kehadiran = hadir - alpha
print ("Jumlah_nilai_akhir:", nilai_akhir)
print ("jumlah_kehadiran:", kehadiran)

#Lulus Jika Nilai >= DAN Hadir
lulus = Nilai >=75 and hadir >=30
print ("Lulus?", lulus)
print ()
keringanan = Nilai >=70 or tugas <=20
print ("Dapat keringanan?:",keringanan)