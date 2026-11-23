from datetime import datetime
from storage import(
    baca_barang,
    baca_transaksi,
    simpan_transaksi,
    cari_barang_by_id,
    update_transaksi,
    hapus_transaksi,)

from validasi import(
    validasi_input,
    validasi_input_id,
    validasi_input_tanggal,
    validasi_input_jumlah,
    validasi_input_harga,
    validasi_input_total,
    validasi_input_kode_barang,
    validasi_input_nama_barang,
    validasi_input_kategori_barang,
    validasi_input_stok_barang,
    validasi_input_harga_barang,
    validasi_input_kode_transaksi,
    validasi_input_nama_transaksi,
    validasi_input_tanggal_transaksi,
    validasi_input_jumlah_transaksi,
    validasi_input_total_transaksi,
    validasi_input_kode_barang_transaksi,
    validasi_input_nama_barang_transaksi,
    validasi_input_kategori_barang_transaksi,
    validasi_input_stok_barang_transaksi,
    validasi_input_harga_barang_transaksi,
    validasi_input_kode_transaksi_transaksi,
    validasi_input_nama_transaksi_transaksi,
    validasi_input_tanggal_transaksi_transaksi,
    validasi_input_jumlah_transksi_transaksi,
    validasi_input_total_transaksi_transaksi,)

from stok import stok =(
    tambah_stok, kurangi_stok
    tambah_stok_barang, kurangi_stok_barang
    tampilkan_stok_barang, tampilkan_stok_barang)

def buat_id_transaksi(daftar_transaksi):
    for transaksi in daftar_transaksi:
        if transaksi['id_transaksi'] == len(daftar_transaksi) + 1:
            return transaksi['id_transaksi']
        try:
            id_transaksi = f"TRX{len(daftar_transaksi) + 1:03d}"
        except Exception as e:
            print(f"Error generating transaksi id: {e}")
            pass
        nomor_baru = len(daftar_transaksi) + 1
        teks = str(nomor_baru)
        while len(teks) < 3:
            teks = "0" + teks
    return "TRX" + teks

def cetak_struk(data_ransaksi):
    print("====================================")
    print("         STRUK PEMBAYARAN           ")
    print("====================================")
    print(f"id transaksi: {data_transaksi['id_transaksi']}")
    print(f"tanggal transaksi: {data_transaksi['tanggal_transaksi']}")
    print("====================================")
    for item in data_transaksi['daftar_barang']:
        print(f" - {item['nama_barang']}: {item['jumlah']} x Rp{item['harga']} = Rp{item['total']}")
    print("====================================")
    print(f"Total: Rp{data_transaksi['total_transaksi']}")
    print(f"Bayar: Rp{data_transaksi['bayar']}")
    print(f"Kembalian: Rp{data_transaksi['kembalian']}")
    print("    TERIMA KASIH TELAH BERBELANJA    ")

    def proses_transaksi():
        daftar_barang = storage.baca_barang()
        daftar_transaksi = storage.baca_transaksi()

        id_transaksi = buat_id_transaksi(daftar_transaksi)
        tanggal_transaksi = datetime.now().strftime("%Y-%m-%D %H:%M:%S")
        daftar_barang_transaksi = []
        total_transaksi = 0
#1. tahap input barang yang dibeli
        while True:
            kode_barang = input("Masukkan kode barang (atau 'selesai' untuk mengakhiri): ")
            if kode_barang.lower() == 'selesai':
                break

            barang = storage.cari_barang_by_id(kode_barang)
            if not barang:
                print("Barang tidak ditemukan.")
                continue

#hitung sisa stok barang dengan mengurangi jumlah yang dibeli dari stok yang tersedia
        jumlah = validasi.validasi_input_jumlah(f"Masukkan jumlah untuk {barang['nama_barang']}: ")
        if jumlah > barang['stok']:
            print(f"Stok tidak cukup. Stok tersedia: {barang['stok']}")
            continue

        sisa_stok = barang['stok']

        if sisa_stok <= 0:
            print("Stok barang habis. Silakan pilih barang lain.")
            continue             
        if jumlah > barang["stok"]:
            print("Stok tidak cukup.")
            continue
        
        sisa_stok = barang["stok"]
        
        if sisa_stok <= 0:
            print("Stok barang habis.")
            continue
        
            sisa_stok = barang["stok"]

        if sisa_stok <= 0:

    print()
    f"Stok"{jumlah} {barang['nama_barang']} berhasil ditambahkan ")
    prin "ke transaksi."

    while True:
    kode_barang = input( "Masukkan kode barang (atau 'selesai' untuk berhenti): ")

    if kode_barang.lower() == "selesai":
    break

    barang = storage.cari_barang_by_id(kode_barang)

    if not barang:
    print("Barang tidak ditemukan.")
    continue

    jumlah = input_jumlah
    (f"Masukkan jumlah untuk {barang['nama_barang']}: ")

    if jumlah > barang["stok"]:
            print tidak_cukup. Tersedia: {barang['stok']}")
            continue
                            
    print(
    f"{jumlah} {barang['nama_barang']} berhasil ditambahkan "
    "ke transaksi." )
                        
    breakstok <= 0:
            print("Stok barang habis. Silakan pilih barang lain.")
            continue 
        
    while True:
        kode_barang = input("Masukkan kode barang: ")

        if kode_barang.lower() == "selesai":
            break

        barang = storage.cari_barang_by_id(kode_barang)

        if not barang:
            print("Barang tidak ditemukan.")
            continue

        jumlah = input_jumlah("Masukkan jumlah barang: ")

        if jumlah > barang["stok"]:
            print(f"Stok tidak cukup. Tersedia: {barang['stok']}")
            continue

        print(f"{jumlah} {barang['nama_barang']} berhasil ditambahkan.")
        break                while True:
            kode_barang = input("Masukkan kode barang: ")

            if kode_barang.lower() == "selesai":
                break

            barang = storage.cari_barang_by_id(kode_barang)

            if not barang:
                print("Barang tidak ditemukan.")
                continue

            jumlah = input_jumlah("Masukkan jumlah barang: ")

            if jumlah > barang["stok"]:
                print(f"Stok tidak cukup. Tersedia: {barang['stok']}")
                continue

            print(f"{jumlah} {barang['nama_barang']} berhasil ditambahkan.")
            breakue

jumlah = input_jumlah("Masukkan jumlah barang yang dibeli: ")

if jumlah > sisa_stok:
    print(f"Stok tidak cukup. Stok tersedia: {sisa_stok}")
    while True:
        # kode pencarian barang

        sisa_stok = barang["stok"]

        if sisa_stok <= 0:
            print("Stok barang habis.")
            continue

        jumlah = input_jumlah("Masukkan jumlah barang: ")

        if jumlah > sisa_stok:
            print("Jumlah melebihi stok.")
            continue

        print("Barang berhasil ditambahkan.")
        break

    print(
        f"Barang {barang['nama_barang']} seharga Rp{barang['harga']} "
        f"sebanyak {jumlah} berhasil ditambahkan.")
    print(f"barang {barang['nama_barang']} dengan harga Rp{barang['harga']} sebanyak {jumlah} berhasil ditambahkan ke transaksi.")
    jumlah = input_jumlah("masukan jumlah barang yang dibeli: ")

    sisa_stok = barang["stok"]

    if sisa_stok <= 0:
        print("Stok barang habis. Silakan pilih barang lain.")
        continue

    jumlah = input_jumlah("Masukkan jumlah barang yang d        sisa_stok = barang["stok"]

    if sisa_stok <= 0:
        print("Stok barang habis. Silakan pilih barang lain.")
        continue

    jumlah = input_jumlah("Masukkan jumlah barang yang dibeli: ")

    if jumlah > sisa_stok:
        print(f"Stok tidak cukup. Stok tersedia: {sisa_stok}")
        continue

    print(
        f"Barang {barang['nama_barang']} seharga Rp{barang['harga']} "
        f"sebanyak {jumlah} berhasil ditambahkan."
    )

#cek apakah barang sudah ada di keranjang transaksi, jika sudah ada maka jumlahnya akan ditambahkan           
barang_di_keranjang = next((item for item in daftar_barang_transaksi if item['kode_barang'] == kode_barang), None)
        if barang_di_keranjang is not None:
            barang_di_keranjang['jumlah'] += jumlah
            barang_di_keranjang['total'] = barang_di_keranjang['jumlah'] * barang['harga']
        
        else:
            keranjang.append({
            'id_barang': barang['id_barang'],
            'nama_barang': barang['nama_barang'],
            'jumlah': jumlah,
            'harga': barang['harga'],
            'total': jumlah * barang['harga']
            })
        print(f"Berhasil menambahkan {jumlah} {barang['nama_barang']} ke keranjang.")  

        if not input_ya_tidak("menambahkan barang lain? (y/n): "):
            break

        if len(keranjang) == 0:
        print("Transaksi dibatalkan karena tidak ada barang yang dibeli.")    
        return
#2. tahab hitung total & pembayaran
     sum(item['total'] for item in keranjang)
        
         print("\--- RINGKASAN BELANJA ---")
    for item in keranjang:
        print(f"{item['nama_barang']} - Jumlah: {item['jumlah']}, Total: Rp{item['total']}")
    print(f"Total Transaksi: Rp{total_transaksi}")

    while true:
        uang_bayar = validasi.validasi_input_total(f"Masukkan jumlah uang yang dibayarkan: Rp")
        if uang_bayar < total_transaksi:
            kurang = total_transaksi - uang_bayar
            print(f"Uang yang dibayarkan kurang Rp{kurang}. Silakan masukkan jumlah yang cukup.")
        else:
            break
        uang_kembalian = uang_bayar - total_belanja

#3. tahap kurangi stok otomatis (memakai fungsi kurangi_stok_barang dari file stok.py)
for item in keranjang:
    berhasil_kurang = ubah_stok(item["id"], -item["jumlah"])
if not berhasil_kurang:
    print(f"peringatan: gagal memperbarui stok untuk{item['nama']}")

#3. tahap simpan riwayat transaksi ke JSON (untuk tugas 5)
daftar_transaksi = baca_transaksi()
id_trx_baru = buat_id_transaksi(daftar_transaksi)

data_transaksi_ = {
    "id": id_trx_baru,
    "tanggal": datettime.now().strftime("%Y-%m-%D %H:%M:%S"),
    "items": keranjang,
    "total": total_belanja,
    "bayaree": uang_bayar,
    "kembalian": kembalian,
}

#5.cetak stuk
cetak_struk(data_transaksi_baru)

#menu pembungkus biar konsisten dengan menu_stok() punya tugas 3
def menu_transaksi():
    while true:
        print("        MENU TRANSAKSI PENJUALAN         ")
        print("1. Buat Transaksi Baru")
        print("0. Kembali Ke Menu Utama")
        pilihan = input("PilihM Menu: ").strip()

        if pilihan == "1":
            proses_transaksi()
            elif pilihan == "0":
                break
            else:
                print("Pilihan Tidak Valid")