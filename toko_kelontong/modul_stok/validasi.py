"""Modul untuk validasi input pengguna."""


def input_angka_positif(pesan):
    """Terus meminta input sampai pengguna memasukkan bilangan bulat > 0."""
    while True:
        try:
            nilai = int(input(pesan))
            if nilai <= 0:
                print("Jumlah harus lebih dari 0!")
                continue
            return nilai
        except ValueError:
            print("Input tidak valid, masukkan angka bulat.")


def input_id(pesan):
    """Meminta ID barang, tidak boleh kosong, otomatis huruf besar."""
    while True:
        id_barang = input(pesan).strip().upper()
        if id_barang == "":
            print("ID barang tidak boleh kosong!")
        else:
            return id_barang


def input_pilihan(pesan, pilihan_valid):
    """Meminta pilihan menu, harus ada di dalam set pilihan_valid."""
    while True:
        pilihan = input(pesan).strip()
        if pilihan in pilihan_valid:
            return pilihan
        print("Pilihan tidak tersedia, coba lagi.")
