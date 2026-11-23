from storage import baca_transaksi
from validasi import input_pilihan_menu, input_teks


def cari_transaksi_by_id(daftar_transaksi, id_transaksi):
    for trx in daftar_transaksi:
        if trx["id"].upper() == id_transaksi.upper():
            return trx
    return {}


def tampil_semua_riwayat():
    daftar = baca_transaksi()

    if len(daftar) == 0:
        print("Belum ada riwayat transaksi penjualan.")
        return

    print("\n" + "=" * 65)
    print("                  DAFTAR RIWAYAT PENJUALAN")
    print("=" * 65)
    for trx in daftar:
        jumlah_item = sum(item["jumlah"] for item in trx["items"])
        print(
            f"{trx['id']} | {trx['tanggal']} | {jumlah_item} item | "
            f"Total: Rp{trx['total']:,}"
        )
    print("=" * 65)


def detail_transaksi():
    daftar = baca_transaksi()

    if len(daftar) == 0:
        print("Belum ada riwayat transaksi penjualan.")
        return

    id_trx = input_teks("Masukkan ID Transaksi (contoh TRX001): ").strip().upper()
    trx = cari_transaksi_by_id(daftar, id_trx)

    if trx == {}:
        print(f"Transaksi dengan ID '{id_trx}' tidak ditemukan.")
        return

    print("\n" + "=" * 50)
    print(f"DETAIL TRANSAKSI : {trx['id']}")
    print(f"Tanggal          : {trx['tanggal']}")
    print("=" * 50)
    for item in trx["items"]:
        print(
            f"- {item['id']} | {item['nama']} | "
            f"{item['jumlah']} x Rp{item['harga']:,} = Rp{item['total']:,}"
        )
    print("-" * 50)
    print(f"Total Belanja    : Rp{trx['total']:,}")
    print(f"Tunai / Bayar    : Rp{trx['bayar']:,}")
    print(f"Kembalian        : Rp{trx['kembalian']:,}")
    print("=" * 50)


def filter_riwayat_tanggal():
    daftar = baca_transaksi()

    if len(daftar) == 0:
        print("Belum ada riwayat transaksi penjualan.")
        return

    tanggal_cari = input_teks("Masukkan tanggal (format YYYY-MM-DD, contoh 2026-11-23): ").strip()
    hasil = [trx for trx in daftar if trx["tanggal"].startswith(tanggal_cari)]

    if len(hasil) == 0:
        print(f"Tidak ada transaksi pada tanggal {tanggal_cari}.")
        return

    total_harian = sum(trx["total"] for trx in hasil)
    print(f"\n=== TRANSAKSI TANGGAL {tanggal_cari} ===")
    for trx in hasil:
        print(f"- {trx['id']} | {trx['tanggal']} | Total: Rp{trx['total']:,}")
    print(f"Total Omzet ({len(hasil)} transaksi): Rp{total_harian:,}")


def rekap_penjualan():
    daftar = baca_transaksi()

    if len(daftar) == 0:
        print("Belum ada data penjualan untuk direkap.")
        return

    total_transaksi = len(daftar)
    total_pendapatan = sum(trx["total"] for trx in daftar)
    total_unit_terjual = 0
    rekap_barang = {}

    for trx in daftar:
        for item in trx["items"]:
            total_unit_terjual += item["jumlah"]
            nama = item["nama"]
            if nama not in rekap_barang:
                rekap_barang[nama] = {"jumlah": 0, "omzet": 0}
            rekap_barang[nama]["jumlah"] += item["jumlah"]
            rekap_barang[nama]["omzet"] += item["total"]

    barang_terlaris = max(
        rekap_barang.items(), key=lambda x: x[1]["jumlah"]
    )

    print("\n" + "=" * 50)
    print("            REKAPITULASI PENJUALAN")
    print("=" * 50)
    print(f"Total Transaksi     : {total_transaksi} transaksi")
    print(f"Total Unit Terjual  : {total_unit_terjual} pcs")
    print(f"Total Pendapatan    : Rp{total_pendapatan:,}")
    print(
        f"Barang Terlaris     : {barang_terlaris[0]} "
        f"({barang_terlaris[1]['jumlah']} terjual)"
    )
    print("-" * 50)
    print("Rincian Penjualan per Barang:")
    for nama, info in sorted(
        rekap_barang.items(), key=lambda x: x[1]["jumlah"], reverse=True
    ):
        print(f"- {nama}: {info['jumlah']} terjual | Rp{info['omzet']:,}")
    print("=" * 50)


def menu_riwayat():
    opsi = (
        "1. Tampilkan semua riwayat penjualan",
        "2. Lihat detail transaksi (by ID)",
        "3. Filter riwayat berdasarkan tanggal",
        "4. Rekapitulasi & barang terlaris",
        "0. Kembali ke menu utama",
    )

    while True:
        print("\n=== RIWAYAT & LAPORAN PENJUALAN ===")
        for baris in opsi:
            print(baris)
        pilihan = input_pilihan_menu("Pilih menu: ", 0, 4)

        if pilihan == 1:
            tampil_semua_riwayat()
        elif pilihan == 2:
            detail_transaksi()
        elif pilihan == 3:
            filter_riwayat_tanggal()
        elif pilihan == 4:
            rekap_penjualan()
        else:
            break