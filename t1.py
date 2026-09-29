def convert_temperature(value, unit):
    if unit.upper() == 'C':
        return (value * 9/5) + 32
    elif unit.upper() == 'F':
        return (value - 32) * 5/9
    else:
        print("Unit harus 'C' atau 'F'")


print("======== KONVERSI SUHU ========")


input_suhu = float(input("Masukkan nilai suhu: "))
unit = input("Masukkan satuan suhu 'C' untuk Celsius atau 'F' untuk Fahrenheit: ")
konversi = convert_temperature(input_suhu, unit)

if unit.upper() == 'C':
    print(f"{input_suhu}°C = {konversi:.2f}°F")
elif unit.upper() == 'F':
    print(f"{input_suhu}°F = {konversi:.2f}°C")
else:
    print("Satuan tidak dikenal.")

# Task 1: Fungsi konversi suhu
def konversi_suhu(suhu, satuan):
    if satuan.upper() == "C":
        return (suhu * 9/5) + 32
    elif satuan.upper() == "F":
        return (suhu - 32) * 5/9
    else:
        return "Satuan tidak valid"

# Task 2: Lambda untuk luas lingkaran
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