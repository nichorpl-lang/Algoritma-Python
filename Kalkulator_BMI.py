berat = int(input("masukan berat anda (kg):" ))
tinggi = int(input("masukan tinggi badan anda (m):" ))
bmi = berat / tinggi ** 2


print ("Berat badan :", berat,"kg")
print ("Tinggi badan :", tinggi,"m")

if bmi < 18.5:
    print ("Keterangan : Berat badan kurang")
elif bmi < 25:
    print ("Keterangan : Berat badan normal")
elif bmi < 30:
    print ("Keterangan : Berat badan berlebih")
else:
    print ("Keterangan : Obesitas")