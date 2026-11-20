"""Program utama - Sistem Manajemen Toko Kelontong (Bagian: Manajemen Stok)."""
from modul_stok import stok
from modul_stok.validasi import input_pilihan


def menu_stok():
    """Submenu Manajemen Stok."""
    while True:
        print("\n===== MANAJEMEN STOK =====")
        print("1. Tambah stok barang")
        print("2. Kurangi stok barang")
        print("3. Tampilkan stok setiap barang")
        print("4. Tampilkan barang hampir habis")
        print("0. Kembali")
        pilihan = input_pilihan("Pilih menu: ", {"0", "1", "2", "3", "4"})

        if pilihan == "1":
            stok.tambah_stok()
        elif pilihan == "2":
            stok.kurangi_stok()
        elif pilihan == "3":
            stok.tampilkan_stok()
        elif pilihan == "4":
            stok.tampilkan_hampir_habis()
        else:
            break


def main():
    """Menu utama. Menu lain (barang, transaksi, riwayat) dari anggota lain."""
    while True:
        print("\n===== TOKO KELONTONG =====")
        print("1. Manajemen Stok")
        print("0. Keluar")
        pilihan = input_pilihan("Pilih menu: ", {"0", "1"})

        if pilihan == "1":
            menu_stok()
        else:
            print("Terima kasih, program selesai.")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh pengguna.")
