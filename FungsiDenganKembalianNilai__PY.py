#Fungsi Dengan Return Value Dengan 1 Argument
def VolumeKubus(Sisi):
    Hasil = Sisi * Sisi * Sisi
    print("Nilai Sisi     = ", Sisi, "cm")
    print("Volume Kubus   = ", Hasil, "cm3")
    print("Penyelesaian   : ", Sisi , 'cm x', Sisi, 'cm x', Sisi, 'cm\n')
    return Hasil

#Fungsi Dengan Return Value Dengan Banyak Argument
def KelilingSegitigaSembarang(SisiKiri, SisiKanan, SisiBawah):
    Hasil = SisiKiri + SisiKanan + SisiBawah
    print("Nilai Sisi Kiri              = ", SisiKiri, "cm")
    print("Nilai Sisi Kanan             = ", SisiKanan, "cm")
    print("Nilai Sisi Bawah             = ", SisiBawah, "cm")
    print("Keliling Segitiga Sembarang  = ", Hasil, "cm")
    print("Penyelesaian                 : ", SisiKiri , 'cm +', SisiKanan, 'cm +', SisiBawah, 'cm\n')
    return Hasil 

print("=" * 7, "Fungsi Dengan Return Value (Dengan 1 Argument)", "=" * 7, '\n')
X = VolumeKubus(12)
# print('\n', X)

print("=" * 7, "Fungsi Dengan Return Value Dengan Banyak Argument", "=" * 7, '\n')
X = KelilingSegitigaSembarang(13, 28, 44)
# print('\n', X)

