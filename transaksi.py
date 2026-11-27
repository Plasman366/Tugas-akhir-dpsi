from datetime import datetime

from stok import ubah_stok
from storage import baca_barang, baca_transaksi, cari_barang_by_id, simpan_transaksi
from validasi import input_jumlah, input_pilihan_menu, input_ya_tidak


def buat_id_transaksi(daftar_transaksi):
    nomor_baru = len(daftar_transaksi) + 1
    teks = str(nomor_baru)
    while len(teks) < 3:
        teks = "0" + teks
    return "TRX" + teks


def cari_di_keranjang(keranjang, id_barang):
    for item in keranjang:
        if item["id"] == id_barang:
            return item
    return {}          


def cetak_struk(data_transaksi):
    print("====================================")
    print("          STRUK PEMBAYARAN          ")
    print("====================================")
    print("ID Transaksi :", data_transaksi["id"])
    print("Tanggal      :", data_transaksi["tanggal"])
    print("====================================")
    for item in data_transaksi["items"]:
        print("-", item["nama"], ":", item["jumlah"], "x Rp" + str(item["harga"]), "= Rp" + str(item["total"]))
    print("====================================")
    print("Total        : Rp" + str(data_transaksi["total"]))
    print("Bayar        : Rp" + str(data_transaksi["bayar"]))
    print("Kembalian    : Rp" + str(data_transaksi["kembalian"]))
    print("====================================")
    print("   TERIMA KASIH TELAH BERBELANJA    ")



def isi_keranjang(daftar_barang):
    keranjang = []

    while True:
        teks = input("Masukkan ID barang (contoh B001, atau 'selesai' untuk lanjut): ").strip()
        if teks.lower() == "selesai":
            break
        id_barang = teks.upper()

        barang = cari_barang_by_id(daftar_barang, id_barang)
        if barang == {}:
            print("Barang tidak ditemukan.")
            continue

        if barang["stok"] <= 0:
            print("Stok barang habis. Silakan pilih barang lain.")
            continue

        
        item = cari_di_keranjang(keranjang, id_barang)
        sudah_di_keranjang = 0
        if item != {}:
            sudah_di_keranjang = item["jumlah"]
        sisa_tersedia = barang["stok"] - sudah_di_keranjang

        if sisa_tersedia <= 0:
            print("Stok", barang["nama"], "di keranjang sudah mencapai batas stok tersedia.")
            continue

        jumlah = input_jumlah("Masukkan jumlah untuk " + barang["nama"] + " (tersedia: " + str(sisa_tersedia) + "): ")
        if jumlah > sisa_tersedia:
            print("Stok tidak cukup. Maksimal bisa ditambah:", sisa_tersedia)
            continue

        if item != {}:
            item["jumlah"] += jumlah
            item["total"] = item["jumlah"] * item["harga"]
        else:
            keranjang.append({
                "id": barang["id"],
                "nama": barang["nama"],
                "jumlah": jumlah,
                "harga": barang["harga"],
                "total": jumlah * barang["harga"],
            })

        print("Berhasil menambahkan", jumlah, barang["nama"], "ke keranjang.")

        if not input_ya_tidak("Tambah barang lain?"):
            break

    return keranjang



def minta_pembayaran(total_belanja):
    while True:
        uang_bayar = input_jumlah("Masukkan jumlah uang yang dibayarkan: Rp")
        if uang_bayar < total_belanja:
            kurang = total_belanja - uang_bayar
            print("Uang yang dibayarkan kurang Rp" + str(kurang) + ". Silakan masukkan jumlah yang cukup.")
        else:
            return uang_bayar


def proses_transaksi():
    daftar_barang = baca_barang()
    if len(daftar_barang) == 0:
        print("Belum ada data barang. Silakan isi data barang terlebih dahulu.")
        return


    keranjang = isi_keranjang(daftar_barang)
    if len(keranjang) == 0:
        print("Transaksi dibatalkan karena tidak ada barang di keranjang.")
        return

    
    total_belanja = 0
    for item in keranjang:
        total_belanja += item["total"]

    print("--- RINGKASAN BELANJA ---")
    for item in keranjang:
        print(item["nama"], "- Jumlah:", item["jumlah"], ", Total: Rp" + str(item["total"]))
    print("Total Transaksi: Rp" + str(total_belanja))

    uang_bayar = minta_pembayaran(total_belanja)
    kembalian = uang_bayar - total_belanja

    
    for item in keranjang:
        berhasil_kurang = ubah_stok(item["id"], -item["jumlah"])
        if not berhasil_kurang:
            print("Peringatan: gagal memperbarui stok untuk", item["nama"])

    
    daftar_transaksi = baca_transaksi()
    data_transaksi_baru = {
        "id": buat_id_transaksi(daftar_transaksi),
        "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "items": keranjang,
        "total": total_belanja,
        "bayar": uang_bayar,
        "kembalian": kembalian,
    }
    daftar_transaksi.append(data_transaksi_baru)
    if not simpan_transaksi(daftar_transaksi):
        print("Peringatan: riwayat transaksi gagal disimpan ke file.")

    
    cetak_struk(data_transaksi_baru)



def menu_transaksi():
    while True:
        print("=== MENU TRANSAKSI PENJUALAN ===")
        print("1. Buat Transaksi Baru")
        print("0. Kembali ke Menu Utama")
        pilihan = input_pilihan_menu("Pilih menu: ", 0, 1)

        if pilihan == 1:
            proses_transaksi()
        else:
            break