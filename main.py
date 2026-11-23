from barang import DATA_AWAL_BARANG
from riwayat import menu_riwayat
from stok import menu_stok
from storage import baca_barang, simpan_barang
from transaksi import menu_transaksi
from validasi import input_pilihan_menu


def inisialisasi_data():
    if len(baca_barang()) == 0:
        simpan_barang(DATA_AWAL_BARANG)


def main():
    inisialisasi_data()

    while True:
        print("\n" + "=" * 50)
        print("Toko Klontong Jaya Makmur")
        print("=" * 50)
        print("1. Manajemen Stok")
        print("2. Transaksi Penjualan")
        print("3. Riwayat & Laporan Penjualan")
        print("0. Keluar")
        pilihan = input_pilihan_menu("Pilih menu: ", 0, 3)

        if pilihan == 1:
            menu_stok()
        elif pilihan == 2:
            menu_transaksi()
        elif pilihan == 3:
            menu_riwayat()
        else:
            print("Terima kasih telah menggunakan aplikasi.")
            break


if __name__ == "__main__":
    main()