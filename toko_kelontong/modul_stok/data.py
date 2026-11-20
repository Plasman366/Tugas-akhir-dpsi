"""Modul untuk membaca dan menyimpan data barang ke file JSON."""
import json
import os

# lokasi file: toko_kelontong/data/barang.json
FOLDER_PROYEK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_BARANG = os.path.join(FOLDER_PROYEK, "data", "barang.json")


def baca_data():
    """Membaca data barang dari file. Mengembalikan list of dictionary."""
    try:
        with open(PATH_BARANG, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File data belum ada, dimulai dengan data kosong.")
        return []
    except json.JSONDecodeError:
        print("Isi file data rusak, dimulai dengan data kosong.")
        return []
    except OSError as e:
        print(f"Gagal membaca file: {e}")
        return []


def simpan_data(data):
    """Menyimpan list barang ke file JSON."""
    try:
        os.makedirs(os.path.dirname(PATH_BARANG), exist_ok=True)
        with open(PATH_BARANG, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return True
    except OSError as e:
        print(f"Gagal menyimpan file: {e}")
        return False
