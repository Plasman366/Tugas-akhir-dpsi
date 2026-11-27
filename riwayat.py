from storage import baca_transaksi
from validasi import input_pilihan_menu, input_teks


def format_rupiah(angka):
    return "Rp" + "{:,}".format(angka)


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

    print("")
    print("=" * 65)
    print("                  DAFTAR RIWAYAT PENJUALAN")
    print("=" * 65)
    for trx in daftar:
        jumlah_item = 0
        for item in trx["items"]:
            jumlah_item = jumlah_item + item["jumlah"]

        print(trx["id"] + " | " + trx["tanggal"] + " | " + str(jumlah_item) + " item | Total: " + format_rupiah(trx["total"]))
    print("=" * 65)


def detail_transaksi():
    daftar = baca_transaksi()

    if len(daftar) == 0:
        print("Belum ada riwayat transaksi penjualan.")
        return

    id_trx = input_teks("Masukkan ID Transaksi (contoh TRX001): ").strip().upper()
    trx = cari_transaksi_by_id(daftar, id_trx)

    if trx == {}:
        print("Transaksi dengan ID '" + id_trx + "' tidak ditemukan.")
        return

    print("")
    print("=" * 50)
    print("DETAIL TRANSAKSI : " + trx["id"])
    print("Tanggal          : " + trx["tanggal"])
    print("=" * 50)
    for item in trx["items"]:
        print("- " + item["id"] + " | " + item["nama"] + " | " + str(item["jumlah"]) + " x " + format_rupiah(item["harga"]) + " = " + format_rupiah(item["total"]))
    print("-" * 50)
    print("Total Belanja    : " + format_rupiah(trx["total"]))
    print("Tunai / Bayar    : " + format_rupiah(trx["bayar"]))
    print("Kembalian        : " + format_rupiah(trx["kembalian"]))
    print("=" * 50)


def filter_riwayat_tanggal():
    daftar = baca_transaksi()

    if len(daftar) == 0:
        print("Belum ada riwayat transaksi penjualan.")
        return

    tanggal_cari = input_teks("Masukkan tanggal (format YYYY-MM-DD, contoh 2026-11-23): ").strip()

    hasil = []
    for trx in daftar:
        if trx["tanggal"].startswith(tanggal_cari):
            hasil.append(trx)

    if len(hasil) == 0:
        print("Tidak ada transaksi pada tanggal " + tanggal_cari + ".")
        return

    total_harian = 0
    print("")
    print("=== TRANSAKSI TANGGAL " + tanggal_cari + " ===")
    for trx in hasil:
        total_harian = total_harian + trx["total"]
        print("- " + trx["id"] + " | " + trx["tanggal"] + " | Total: " + format_rupiah(trx["total"]))
    print("Total Omzet (" + str(len(hasil)) + " transaksi): " + format_rupiah(total_harian))


def rekap_penjualan():
    daftar = baca_transaksi()

    if len(daftar) == 0:
        print("Belum ada data penjualan untuk direkap.")
        return

    total_transaksi = len(daftar)
    total_pendapatan = 0
    total_unit_terjual = 0
    rekap_barang = {}

    for trx in daftar:
        total_pendapatan = total_pendapatan + trx["total"]
        for item in trx["items"]:
            total_unit_terjual = total_unit_terjual + item["jumlah"]
            nama = item["nama"]
            if nama not in rekap_barang:
                rekap_barang[nama] = {"jumlah": 0, "omzet": 0}
            rekap_barang[nama]["jumlah"] = rekap_barang[nama]["jumlah"] + item["jumlah"]
            rekap_barang[nama]["omzet"] = rekap_barang[nama]["omzet"] + item["total"]

    # cari barang terlaris
    nama_terlaris = ""
    jumlah_terlaris = 0
    for nama in rekap_barang:
        if rekap_barang[nama]["jumlah"] > jumlah_terlaris:
            jumlah_terlaris = rekap_barang[nama]["jumlah"]
            nama_terlaris = nama

    # urutkan nama barang dari yang paling banyak terjual
    daftar_nama = list(rekap_barang.keys())
    for i in range(len(daftar_nama)):
        for j in range(i + 1, len(daftar_nama)):
            if rekap_barang[daftar_nama[j]]["jumlah"] > rekap_barang[daftar_nama[i]]["jumlah"]:
                sementara = daftar_nama[i]
                daftar_nama[i] = daftar_nama[j]
                daftar_nama[j] = sementara

    print("")
    print("=" * 50)
    print("            REKAPITULASI PENJUALAN")
    print("=" * 50)
    print("Total Transaksi     : " + str(total_transaksi) + " transaksi")
    print("Total Unit Terjual  : " + str(total_unit_terjual) + " pcs")
    print("Total Pendapatan    : " + format_rupiah(total_pendapatan))
    print("Barang Terlaris     : " + nama_terlaris + " (" + str(jumlah_terlaris) + " terjual)")
    print("-" * 50)
    print("Rincian Penjualan per Barang:")
    for nama in daftar_nama:
        print("- " + nama + ": " + str(rekap_barang[nama]["jumlah"]) + " terjual | " + format_rupiah(rekap_barang[nama]["omzet"]))
    print("=" * 50)


def menu_riwayat():
    while True:
        print("")
        print("=== RIWAYAT & LAPORAN PENJUALAN ===")
        print("1. Tampilkan semua riwayat penjualan")
        print("2. Lihat detail transaksi (by ID)")
        print("3. Filter riwayat berdasarkan tanggal")
        print("4. Rekapitulasi & barang terlaris")
        print("0. Kembali ke menu utama")
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