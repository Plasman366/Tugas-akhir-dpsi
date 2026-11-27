from storage import baca_barang, cari_barang_by_id, simpan_barang
from validasi import input_jumlah, input_pilihan_menu, valid_format_id

BATAS_MENIPIS = 5


def minta_id():
    while True:
        id_barang = input("Masukkan ID barang (contoh B001, ketik 0 untuk batal): ")
        id_barang = id_barang.strip()
        if id_barang == "0":
            return None
        if valid_format_id(id_barang):
            return id_barang
        print("Format ID salah! Contoh: B001 (huruf B kapital)")


def ubah_stok(id_barang, jumlah):
    daftar = baca_barang()
    barang = cari_barang_by_id(daftar, id_barang)
    if barang == {}:                     
        return False

        return False
    if barang["stok"] + jumlah < 0:      
        return False

    barang["stok"] += jumlah
    return simpan_barang(daftar)        


def tampil_stok():
    daftar = baca_barang()

    if len(daftar) == 0:
        print("Belum ada data barang.")
        return

    print("DAFTAR STOK BARANG")
    print("=" * 50)
    for x in daftar:
        ket = ""
        if x["stok"] <= BATAS_MENIPIS:
            ket = "(HAMPIR HABIS)"
        print(x["id"], "|", x["nama"], "|", x["kategori"], "| stok:", x["stok"], ket)


def tampil_stok_menipis():
    daftar = baca_barang()

    menipis = []
    for x in daftar:
        if x["stok"] <= BATAS_MENIPIS:
            menipis.append(x)

    if len(menipis) == 0:
        print("Tidak ada barang yang hampir habis.")
        return

    print("=== BARANG HAMPIR HABIS (stok <= " + str(BATAS_MENIPIS) + ") ===")
    for x in menipis:
        print("-", x["id"], "|", x["nama"], "| sisa", x["stok"])

    kategori_terdampak = []
    for x in menipis:
        if x["kategori"] not in kategori_terdampak:
            kategori_terdampak.append(x["kategori"])

    print("Kategori yang terdampak:")
    for kategori in kategori_terdampak:
        print("-", kategori)


def tambah_stok():
    id_barang = minta_id()
    if id_barang is None:
        print("Dibatalkan.")
        return

    barang = cari_barang_by_id(baca_barang(), id_barang)
    if barang == {}:
        print("Barang dengan ID tersebut tidak ditemukan.")
        return

    print("Barang:", barang["nama"], "(stok saat ini: " + str(barang["stok"]) + ")")
    jumlah = input_jumlah("Jumlah stok yang ditambahkan: ")

    if ubah_stok(id_barang, jumlah):
        print("Berhasil! Stok", barang["nama"], "sekarang:", barang["stok"] + jumlah)
    else:
        print("Gagal menambah stok.")


def kurangi_stok():
    id_barang = minta_id()
    if id_barang is None:
        print("Dibatalkan.")
        return

    barang = cari_barang_by_id(baca_barang(), id_barang)
    if barang == {}:
        print("Barang dengan ID tersebut tidak ditemukan.")
        return

    print("Barang:", barang["nama"], "(stok saat ini: " + str(barang["stok"]) + ")")
    jumlah = input_jumlah("Jumlah stok yang dikurangi: ")

    if jumlah > barang["stok"]:
        print("Gagal! Jumlah pengurangan melebihi stok yang ada.")
        return

    if ubah_stok(id_barang, -jumlah):
        print("Berhasil! Stok", barang["nama"], "sekarang:", barang["stok"] - jumlah)
    else:
        print("Gagal mengurangi stok.")


def menu_stok():
    opsi = (
        "1. Tampilkan stok semua barang",
        "2. Tambah stok",
        "3. Kurangi stok",
        "4. Tampilkan barang hampir habis",
        "0. Kembali ke menu utama",
    )

    while True:
        print("=== MANAJEMEN STOK ===")
        for baris in opsi:
            print(baris)
        pilihan = input_pilihan_menu("Pilih menu: ", 0, 4)

        if pilihan == 1:
            tampil_stok()
        elif pilihan == 2:
            tambah_stok()
        elif pilihan == 3:
            kurangi_stok()
        elif pilihan == 4:
            tampil_stok_menipis()
        else:
            break