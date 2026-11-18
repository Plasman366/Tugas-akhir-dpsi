def valid_tidak_kosong(teks):
    for huruf in teks:
        if huruf != " ":
            return True
    return False

def valid_format_id(id_barang):
    if len(id_barang) != 4:
        return False
    if id_barang[0] != "B":
        return False
    for i in range(1, 4):
        if id_barang[i] not in "0123456789":
            return False
    return True

def valid_harga(harga):
    if harga > 0:
        return True
    return False

def valid_stok(stok):
    if stok >= 0:
        return True
    return False

def valid_jumlah(jumlah):
    if jumlah > 0:
        return True
    return False

def valid_id_unik(daftar_barang, id_barang):
    for barang in daftar_barang:
        if barang["id"] == id_barang:
            return False
    return True


# ---------- Fungsi input ----------

def input_teks(pesan):
    while True:
        teks = input(pesan)
        if valid_tidak_kosong(teks):
            return teks
        print("Input tidak boleh kosong!")

def input_bilangan_bulat(pesan):
    while True:
        try:
            angka = int(input(pesan))
            return angka
        except ValueError:
            print("Input harus berupa angka bulat!")

def input_harga(pesan):
    while True:
        angka = input_bilangan_bulat(pesan)
        if valid_harga(angka):
            return angka
        print("Harga harus lebih dari 0!")

def input_stok(pesan):
    while True:
        angka = input_bilangan_bulat(pesan)
        if valid_stok(angka):
            return angka
        print("Stok tidak boleh negatif!")

def input_jumlah(pesan):
    while True:
        angka = input_bilangan_bulat(pesan)
        if valid_jumlah(angka):
            return angka
        print("Jumlah harus lebih dari 0!")

def input_pilihan_menu(pesan, minimal, maksimal):
    while True:
        angka = input_bilangan_bulat(pesan)
        if angka >= minimal and angka <= maksimal:
            return angka
        print("Pilihan harus antara", minimal, "sampai", maksimal)

def input_ya_tidak(pesan):
    while True:
        jawaban = input(pesan + " (y/n): ")
        if jawaban == "y" or jawaban == "Y":
            return True
        if jawaban == "n" or jawaban == "N":
            return False
        print("Jawab dengan y atau n saja!")

def input_id_baru(daftar_barang, pesan):
    while True:
        id_barang = input(pesan)

        if not valid_format_id(id_barang):
            print("Format ID salah! Contoh: B001 (huruf B kapital)")
        elif not valid_id_unik(daftar_barang, id_barang):
            print("ID sudah dipakai, gunakan ID lain!")
        else:
            return id_barang