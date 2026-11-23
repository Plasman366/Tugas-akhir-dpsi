from datetime import datetime

from stok import ubah_stok
from storage import (
    baca_barang,
    baca_transaksi,
    cari_barang_by_id,
    simpan_transaksi,
)
from validasi import input_jumlah, input_pilihan_menu, input_ya_tidak


def buat_id_transaksi(daftar_transaksi):
    terbesar = 0
    for transaksi in daftar_transaksi:
        id_trx = str(transaksi.get("id", ""))
        if id_trx.startswith("TRX"):
            try:
                nomor = int(id_trx[3:])
                if nomor > terbesar:
                    terbesar = nomor
            except ValueError:
                pass
    nomor_baru = terbesar + 1
    return f"TRX{nomor_baru:03d}"


def cetak_struk(data_transaksi):
    print("\n====================================")
    print("          STRUK PEMBAYARAN          ")
    print("====================================")
    print(f"ID Transaksi : {data_transaksi['id']}")
    print(f"Tanggal      : {data_transaksi['tanggal']}")
    print("====================================")
    for item in data_transaksi["items"]:
        print(
            f"- {item['nama']}: {item['jumlah']} x Rp{item['harga']} = Rp{item['total']}"
        )
    print("====================================")
    print(f"Total        : Rp{data_transaksi['total']}")
    print(f"Bayar        : Rp{data_transaksi['bayar']}")
    print(f"Kembalian    : Rp{data_transaksi['kembalian']}")
    print("====================================")
    print("  TERIMA KASIH TELAH BERBELANJA    ")


def proses_transaksi():
    daftar_barang = baca_barang()
    if len(daftar_barang) == 0:
        print("Belum ada data barang. Silakan isi data barang terlebih dahulu.")
        return

    keranjang = []

    # 1. Tahap input barang yang dibeli
    while True:
        id_barang = input("Masukkan ID barang (contoh B001, atau 'selesai' untuk lanjut): ").strip()
        if id_barang.lower() == "selesai":
            break

        barang = cari_barang_by_id(daftar_barang, id_barang)
        if barang == {}:
            print("Barang tidak ditemukan.")
            continue

        if barang["stok"] <= 0:
            print("Stok barang habis. Silakan pilih barang lain.")
            continue

        sudah_di_keranjang = 0
        for item in keranjang:
            if item["id"] == barang["id"]:
                sudah_di_keranjang = item["jumlah"]
                break

        sisa_tersedia = barang["stok"] - sudah_di_keranjang
        if sisa_tersedia <= 0:
            print(f"Stok {barang['nama']} di keranjang sudah mencapai batas stok tersedia ({barang['stok']}).")
            continue

        jumlah = input_jumlah(f"Masukkan jumlah untuk {barang['nama']} (tersedia: {sisa_tersedia}): ")
        if jumlah > sisa_tersedia:
            print(f"Stok tidak cukup. Maksimal bisa ditambah: {sisa_tersedia}")
            continue

        item_ada = None
        for item in keranjang:
            if item["id"] == barang["id"]:
                item_ada = item
                break

        if item_ada is not None:
            item_ada["jumlah"] += jumlah
            item_ada["total"] = item_ada["jumlah"] * item_ada["harga"]
        else:
            keranjang.append(
                {
                    "id": barang["id"],
                    "nama": barang["nama"],
                    "jumlah": jumlah,
                    "harga": barang["harga"],
                    "total": jumlah * barang["harga"],
                }
            )

        print(f"Berhasil menambahkan {jumlah} {barang['nama']} ke keranjang.")

        if not input_ya_tidak("Tambah barang lain?"):
            break

    if len(keranjang) == 0:
        print("Transaksi dibatalkan karena tidak ada barang di keranjang.")
        return

    # 2. Tahap hitung total & pembayaran
    total_belanja = sum(item["total"] for item in keranjang)

    print("\n--- RINGKASAN BELANJA ---")
    for item in keranjang:
        print(f"{item['nama']} - Jumlah: {item['jumlah']}, Total: Rp{item['total']}")
    print(f"Total Transaksi: Rp{total_belanja}")

    while True:
        uang_bayar = input_jumlah("Masukkan jumlah uang yang dibayarkan: Rp")
        if uang_bayar < total_belanja:
            kurang = total_belanja - uang_bayar
            print(f"Uang yang dibayarkan kurang Rp{kurang}. Silakan masukkan jumlah yang cukup.")
        else:
            break

    kembalian = uang_bayar - total_belanja

    # 3. Tahap kurangi stok otomatis
    for item in keranjang:
        berhasil_kurang = ubah_stok(item["id"], -item["jumlah"])
        if not berhasil_kurang:
            print(f"Peringatan: gagal memperbarui stok untuk {item['nama']}.")

    # 4. Tahap simpan riwayat transaksi ke JSON
    daftar_transaksi = baca_transaksi()
    id_trx_baru = buat_id_transaksi(daftar_transaksi)

    data_transaksi_baru = {
        "id": id_trx_baru,
        "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "items": keranjang,
        "total": total_belanja,
        "bayar": uang_bayar,
        "kembalian": kembalian,
    }

    daftar_transaksi.append(data_transaksi_baru)
    if not simpan_transaksi(daftar_transaksi):
        print("Peringatan: riwayat transaksi gagal disimpan ke file.")

    # 5. Cetak struk
    cetak_struk(data_transaksi_baru)


def riwayat_transaksi():
    daftar_transaksi = baca_transaksi()
    if len(daftar_transaksi) == 0:
        print("Belum ada riwayat transaksi.")
        return

    print("\n=== RIWAYAT TRANSAKSI ===")
    for trx in daftar_transaksi:
        print(
            f"{trx['id']} | {trx['tanggal']} | Total: Rp{trx['total']} | Kembalian: Rp{trx['kembalian']}"
        )


def menu_transaksi():
    while True:
        print("\n=== MENU TRANSAKSI PENJUALAN ===")
        print("1. Buat Transaksi Baru")
        print("2. Lihat Riwayat Transaksi")
        print("0. Kembali ke Menu Utama")
        pilihan = input_pilihan_menu("Pilih menu: ", 0, 2)

        if pilihan == 1:
            proses_transaksi()
        elif pilihan == 2:
            riwayat_transaksi()
        else:
            break