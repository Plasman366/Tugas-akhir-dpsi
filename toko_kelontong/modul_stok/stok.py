"""Modul fitur Manajemen Stok."""
from modul_stok.data import baca_data, simpan_data
from modul_stok.validasi import input_angka_positif, input_id

BATAS_MINIMUM = 5  # stok <= 5 dianggap hampir habis
KOLOM = ("ID", "Nama Barang", "Kategori", "Stok")  # tuple judul tabel


def cari_barang(data, id_barang):
    """Mencari barang berdasarkan ID. Mengembalikan dictionary atau None."""
    for barang in data:
        if barang["id"] == id_barang:
            return barang
    return None


def cetak_tabel(daftar_barang):
    """Mencetak tabel barang beserta stoknya."""
    print("-" * 56)
    print(f"{KOLOM[0]:<9}{KOLOM[1]:<25}{KOLOM[2]:<14}{KOLOM[3]:>6}")
    print("-" * 56)
    for b in daftar_barang:
        print(f"{b['id']:<9}{b['nama']:<25}{b['kategori']:<14}{b['stok']:>6}")
    print("-" * 56)


def tampilkan_stok():
    """Menampilkan jumlah stok setiap barang."""
    data = baca_data()
    if len(data) == 0:
        print("Belum ada data barang.")
        return
    print("\n=== DAFTAR STOK BARANG ===")
    cetak_tabel(data)
    total = sum(b["stok"] for b in data)
    print(f"Jumlah jenis barang : {len(data)}")
    print(f"Total seluruh stok  : {total}")


def tambah_stok():
    """Menambah stok barang yang sudah terdaftar."""
    data = baca_data()
    if len(data) == 0:
        print("Belum ada data barang.")
        return
    print("\n=== TAMBAH STOK ===")
    cetak_tabel(data)
    barang = cari_barang(data, input_id("Masukkan ID barang: "))
    if barang is None:
        print("Barang dengan ID tersebut tidak ditemukan!")
        return

    jumlah = input_angka_positif(f"Jumlah stok {barang['nama']} yang ditambah: ")
    stok_lama = barang["stok"]
    barang["stok"] += jumlah
    if simpan_data(data):
        print(f"Berhasil! Stok {barang['nama']}: {stok_lama} -> {barang['stok']}")


def kurangi_stok():
    """Mengurangi stok barang (stok tidak boleh negatif)."""
    data = baca_data()
    if len(data) == 0:
        print("Belum ada data barang.")
        return
    print("\n=== KURANGI STOK ===")
    cetak_tabel(data)
    barang = cari_barang(data, input_id("Masukkan ID barang: "))
    if barang is None:
        print("Barang dengan ID tersebut tidak ditemukan!")
        return
    if barang["stok"] == 0:
        print(f"Stok {barang['nama']} sudah habis (0).")
        return

    jumlah = input_angka_positif(f"Jumlah stok {barang['nama']} yang dikurangi: ")
    if jumlah > barang["stok"]:
        print(f"Gagal! Stok tersedia hanya {barang['stok']}, stok tidak boleh negatif.")
        return

    stok_lama = barang["stok"]
    barang["stok"] -= jumlah
    if simpan_data(data):
        print(f"Berhasil! Stok {barang['nama']}: {stok_lama} -> {barang['stok']}")


def kurangi_stok_transaksi(data, id_barang, jumlah):
    """
    Dipakai oleh fitur Transaksi Penjualan (bagian teman satu kelompok)
    untuk mengurangi stok otomatis setelah pembayaran berhasil.
    Melempar ValueError kalau barang tidak ada atau stok tidak cukup.
    """
    barang = cari_barang(data, id_barang)
    if barang is None:
        raise ValueError(f"Barang {id_barang} tidak ditemukan")
    if jumlah > barang["stok"]:
        raise ValueError(f"Stok {barang['nama']} tidak cukup")
    barang["stok"] -= jumlah
    return barang


def tampilkan_hampir_habis():
    """Menampilkan barang yang stoknya <= batas minimum."""
    data = baca_data()
    if len(data) == 0:
        print("Belum ada data barang.")
        return

    batas = BATAS_MINIMUM
    masukan = input(f"Batas stok minimum (Enter = {BATAS_MINIMUM}): ").strip()
    if masukan != "":
        try:
            batas = int(masukan)
            if batas < 0:
                print("Batas tidak boleh negatif, pakai batas bawaan.")
                batas = BATAS_MINIMUM
        except ValueError:
            print("Input bukan angka, pakai batas bawaan.")

    hampir_habis = [b for b in data if b["stok"] <= batas]
    print(f"\n=== BARANG HAMPIR HABIS (stok <= {batas}) ===")
    if len(hampir_habis) == 0:
        print("Semua barang stoknya masih aman.")
        return

    cetak_tabel(hampir_habis)
    kategori_terdampak = {b["kategori"] for b in hampir_habis}  # set
    print(f"Jumlah barang   : {len(hampir_habis)}")
    print(f"Kategori terkait: {', '.join(sorted(kategori_terdampak))}")
    print("Segera lakukan restok untuk barang di atas!")



print("update data")

print("hello world")