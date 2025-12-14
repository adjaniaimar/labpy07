data_mahasiswa = {}

def look_data():
    print("Program Input Nilai")
    print("=" * 65)
    print(f"| {'NO':^2} | {'NIM':^9} | {'NAMA':^10} | {'TUGAS':^5} | {'UTS':^4} | {'UAS':^4} | {'AKHIR':^9} |")
    print("=" * 65)

    if not data_mahasiswa:
        print("|                         TIDAK ADA DATA                        |")
        print("="*65)
        return

    for no,(nim, mhs) in enumerate(data_mahasiswa.items(), start=1):
        print(f"| {no:>2} | {nim:^8} | {mhs['nama']:^10} | {mhs['tugas']:^5} | {mhs['uts']:^3} | {mhs['uas']:^3} | {mhs['akhir']:^9.1f} |")
    print("="*65)


def plus_data():
    print("\nTambah Data Mahasiswa")
    nim = input("NIM           : ")

    if nim in data_mahasiswa:
        print("NIM sudah ada nihhh:) ")
        return

    nama = input("Nama          : ")
    tugas = float(input("Nilai Tugas   : "))
    uts = float(input("Nilai UTS     : "))
    uas = float(input("Nilai UAS     : "))
    akhir = (tugas*0.3) + (uts*0.35) + (uas*0.35)

    data_mahasiswa[nim] = {
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": akhir
    }
    print("Yeay data berhasil ditambah:) ")

def change_data():
    nim = input("\nMasukkan NIM untuk mengubah data: ")
    if nim not in data_mahasiswa:
        print("Yah data tidak ditemukan:( ")
        return

    print("Yeay data ditemukan, Ayo masukkan data baru:")
    nama = input("Nama baru    : ")
    tugas = float(input("Tugas baru   : "))
    uts = float(input("UTS baru     : "))
    uas = float(input("UAS baru     : "))
    akhir = (tugas*0.3)+(uts*0.35)+(uas*0.35)

    data_mahasiswa[nim] = {
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": akhir
    }
    print("Yeay data berhasil diubah:) ")

def delete_data():
    nim = input("\nMasukkan NIM yang mau dihapus: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Yeay data berhasil dihapus:) ")
    else:
        print("Yah data tidak ditemukan:( ")

def find_data():
    nim = input("\nMasukkan NIM yang mau dicari: ")

    if nim not in data_mahasiswa:
        print("Yah data tidak ditemukan:( ")
        return

    mhs = data_mahasiswa[nim]
    print("\nData ditemukan:")
    print(f"NIM   : {nim}")
    print(f"Nama  : {mhs['nama']}")
    print(f"Tugas : {mhs['tugas']}")
    print(f"UTS   : {mhs['uts']}")
    print(f"UAS   : {mhs['uas']}")
    print(f"Akhir : {mhs['akhir']:.1f}")

while True:
    print("\nProgram Input Nilai")
    print("====================")
    pilihan = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]: ").lower()

    if pilihan == "l":
        look_data()
    elif pilihan == "t":
        plus_data()
    elif pilihan == "u":
        change_data()
    elif pilihan == "h":
        delete_data()
    elif pilihan == "c":
        find_data()
    elif pilihan == "k":
        print("Terimakasih sudah menggunakan program ini by Nevillaz:) ")
        break
    else:
        print("Yah pilihan tidak sesuai:( ")