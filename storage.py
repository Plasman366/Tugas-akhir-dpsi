import json

FILE_BARANG = "barang.json"
FILE_TRANSAKSI = "transaksi.json"


def baca_data(nama_file):
    try:
        file = open(nama_file, "r")
        data = json.load(file)
        file.close()
        return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def simpan_data(nama_file, data):
    try:
        file = open(nama_file, "w")
        json.dump(data, file, indent=4)
        file.close()
        return True
    except IOError:
        print("Data gagal disimpan ke file.")
        return False

def baca_barang():
    return baca_data(FILE_BARANG)

def simpan_barang(daftar_barang):
    return simpan_data(FILE_BARANG, daftar_barang)

def baca_transaksi():
    return baca_data(FILE_TRANSAKSI)

def simpan_transaksi(daftar_transaksi):
    return simpan_data(FILE_TRANSAKSI, daftar_transaksi)

def cari_barang_by_id(daftar_barang, id_barang):
    for barang in daftar_barang:
        if barang["id"] == id_barang:
            return barang
    return {}

def id_sudah_ada(daftar_barang, id_barang):
    for barang in daftar_barang:
        if barang["id"] == id_barang:
            return True
    return False

def buat_id_baru(daftar_barang):
    terbesar = 0

    for barang in daftar_barang:
        id_barang = barang["id"]
        try:
            nomor = int(id_barang[1:])
            if nomor > terbesar:
                terbesar = nomor
        except ValueError:
            pass

    nomor_baru = terbesar + 1

    teks = str(nomor_baru)
    while len(teks) < 3:
        teks = "0" + teks

    return "B" + teks