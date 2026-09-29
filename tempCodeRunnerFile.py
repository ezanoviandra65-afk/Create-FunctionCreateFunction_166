import math
luas_lingkaran = lambda r: math.pi * r ** 2

# Program utama
print("=== TASK 1: KONVERSI SUHU ===")

suhu = float(input("Masukkan suhu: "))
satuan = input("Masukkan satuan (C/F): ")

hasil_suhu = konversi_suhu(suhu, satuan)

print("Hasil konversi:", hasil_suhu)

print("\n=== TASK 2: LUAS LINGKARAN ===")

r = float(input("Masukkan jari-jari lingkaran: "))

hasil_luas = luas_lingkaran(r)

print("Luas lingkaran:", hasil_luas)