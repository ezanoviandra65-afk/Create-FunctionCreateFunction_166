# Task 1: Fungsi konversi suhu
def konversi_suhu(suhu, satuan):
    if satuan.upper() == "C":
        return (suhu * 9/5) + 32
    elif satuan.upper() == "F":
        return (suhu - 32) * 5/9
    else:
        return "Satuan tidak valid"