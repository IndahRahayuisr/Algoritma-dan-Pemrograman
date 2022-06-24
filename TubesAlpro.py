from ast import Return

print("||>>>=======================================================>>>||")
print("<<|||>>=======SELAMAT DATANG DI PERPUSTAKAAN INDAH<<|||>>>=======")
print("||>>>=======================================================>>>||")
print("\n")
print("|||>>>==== SILAHKAN MENGISI DATA DIRI TERLEBIH DAHULU =====<<<|||")
print("\n")
member = input("Apakah kamu adalah salah satu member dari perpustakaan? ")
if member == "ya":
    nama = input("Nama: ")
    alamat = input("Alamat: ")
    status = input("Status: ")
    if status == "pelajar":
        nama_sekolah = input("Masukkan nama sekolah: ")
        print()
    elif status == "mahasiswa":
        nama_universitas = input("Masukkan nama universitas: ")
        print()
    else:
        lainnya = input("Lainnya: ")
        print()
elif member == "tidak":
    print("SILAHKAN ISI DATA DIRI BERIKUT UNTUK DAPAT MENGGUNAKAN FASILITAS YANG DISEDIAKAN")
    nama = input("Masukkan nama lengkap: ")
    daftaralamat = input("Masukkan alamat lengkap: ")
    asal = input("Masukkan nama sekolah jika kamu pelajar, masukkan nama universitas jika kamu mahasiswa, masukkan nama instansi lain jika kamu bukan keduanya: ")
    print("KAMU SUDAH BISA MENGGUNAKAN FASILITAS YANG ADA DI PERPUSTAKAAN INDAH")
    print("==========================================================================================================================")
    print("\n")

def selamat_datang (nama):
    print(f"Halo {nama}, SELAMAT DATANG DI PERPUSTAKAAN INDAH!")
selamat_datang(nama)
print("\n")
print("=================================================================================")
print("||-------------------------------- MENU UTAMA ---------------------------------||")
print("||------------------------------ 1. PINJAM BUKU -------------------------------||")
print("||------------------------------ 2. PENGEMBALIAN BUKU -------------------------||")
print("||------------------------------ 3. PENAMBAHAN BUKU ---------------------------||")
print("||------------------------------ 4. STATISTIK ---------------------------------||")
print("||------------------------------ 5. KELUAR ------------------------------------||")
print("=================================================================================")
print("\n")

while True:
    try:
        menu = input("Masukkan menu: ")
        if menu == "1":
            print("\n")
            print("=====================================================================================================================")
            print("||--------------------MAKSIMAL JUMLAH BUKU YANG DIPINJAM ADALAH 10 BUKU DARI SEMUA JENIS BUKU----------------------||")
            print("||-----------------PEMILIHAN MASING-MASING JENIS BUKU HANYA BERLAKU SEKALI PADA SAAT PEMINJAMAN!-------------------||")
            print("||---------------SILAHKAN MENUJU MENU TAMBAH BUKU, APABILA ADA BUKU YANG TERLUPA UNTUK DIPINJAM!-------------------||")
            print("=====================================================================================================================")
            print("\n")
            def waktu ():
                print("Batas waktu peminjaman hanya selama 7 hari, silahkan mengembalikan buku sesuai waktu yang ditentukan")
                bulanmenuutama = {
                    1:"Januari", 2:"Februari", 3:"Maret", 4:"April", 5:"Mei", 6: "Juni", 
                    7:"Juli", 8: "Agustus", 9: "September", 10:"Oktober", 11: "November", 12: "Desember"}
                tanggal_pinjam = int(input("Masukkan tanggal hari ini: "))
                bulan_pinjam = int(input("Masukkan bulan: "))
                tahun_pinjam = int(input("Masukkan tahun: "))
                print("\n")
                tanggal_kembali =  int(input("Masukkan tanggal untuk pengembalian: "))
                bulan_kembali = int(input("Masukkan bulan untuk pengembalian: "))
                tahun_kembali = int(input("Masukkan tahun untuk pengembalian: "))
                tanggal = tanggal_kembali - tanggal_pinjam
                bulan = bulan_kembali - bulan_pinjam
                tahun = tahun_kembali - tahun_pinjam
                sebulan = bulan*30
                setahun = tahun*365
                jadi = setahun+sebulan+tanggal
                print("--------------------------------------------------------------------------------------------------------\n")
                print(f"Lama peminjaman {jadi} hari", "kembali pada tanggal", tanggal_kembali, "bulan", bulanmenuutama[bulan_kembali], "tahun", tahun_kembali)
                print("--------------------------------------------------------------------------------------------------------\n")
            waktu()
            print("==========================================================")
            print("|-----------------------JENIS BUKU-----------------------|")
            print("|-----------------------1. NOVEL-------------------------|")
            print("|-----------------------2. KOMIK-------------------------|")
            print("|-----------------------3. ENSIKLOPEDIA------------------|")
            print("|-----------------------4. LAINNYA-----------------------|")
            print("==========================================================")
            print("\n")
            jenis_buku = input("Pilih jenis buku: ")
            if jenis_buku == "1":
                jumlahnovel = int(input("Berapa novel yang ingin dipinjam?: "))
                for i in range(jumlahnovel):
                    judul_novel = input("Masukkan judul novel yang ingin dipinjam: ")
                    penulis = input("Masukkan nama penulis dari novel yang ingin dipinjam: ")
                    penerbit = input("Masukkan nama penerbit novel yang ingin dipinjam: ")
                    print(f"{nama} telah meminjam novel dengan judul {judul_novel} oleh {penulis} yang diterbitkan oleh {penerbit}")
                    print("--------------------------------------------------------------------------------------------------------\n")
            elif jenis_buku == "2":
                jumlahkomik = int(input("Berapa komik yang ingin dipinjam?: "))
                for i in range(jumlahkomik):
                    judul_komik = input("Masukkan judul komik yang ingin dipinjam: ")
                    penulis_komik = input("Masukkan penulis komik: ")
                    print(f"{nama} telah meminjam komik dengan judul {judul_komik} oleh {penulis_komik}")
                    print("---------------------------------------------------------------------------------------------------------\n")
            elif jenis_buku == "3":
                jumlahensiklopedia = int(input("Berapa ensiklopedia yang ingin dipinjam?: "))
                for i in range(jumlahensiklopedia):
                    judul_ensiklopedia = input("Masukkan judul ensiklopedia: ")
                    jenis_ensiklopedi = input("Masukkan jenis ensiklopedia: ")
                    print(f"{nama} telah meminjam ensiklopedia dengan judul {judul_ensiklopedia} dengan jenis {jenis_ensiklopedi}")
                    print("---------------------------------------------------------------------------------------------------------\n")
            elif jenis_buku == "4":
                jumlahbuku = int(input("Berapa buku yang ingin dipinjam?: "))
                for i in range(jumlahbuku):
                    judul_buku = input("Masukkan judul buku: ")
                    penerbit = input("Masukkan penerbit: ")
                    penulis = input("Masukkan penulis buku: ")
                    print(f"{nama} telah meminjam buku dengan judul {judul_buku} oleh {penulis} oleh penerbit {penerbit}")
                    print("---------------------------------------------------------------------------------------------------------\n")
        elif menu == "2":
            print("=============================================================================================================")
            print("||----------------------------------LAMA PEMINJAMAN BUKU HANYA 7 HARI--------------------------------------||")
            print("||---------------JIKA TERLAMBAT MENGEMBALIKANA KAN DIKENAKAN DENDA SESUAI DENGAN KETENTUAN!----------------||")
            print("=============================================================================================================")
            print("\n")
            print("==========================================================")
            print("|-----------------------JENIS BUKU-----------------------|")
            print("|-----------------------1. NOVEL-------------------------|")
            print("|-----------------------2. KOMIK-------------------------|")
            print("|-----------------------3. ENSIKLOPEDIA------------------|")
            print("|-----------------------4. LAINNYA-----------------------|")
            print("==========================================================")
            jumlahbuku = int(input("Jumlah buku yang dipinjam: "))
            for i in range(jumlahbuku):
                jenisbuku = input("Masukkan jenis buku: ")
                judulnya = input("Masukkan judul: ")
                penulisnya = input("Masukkan nama penulis: ")
                penerbitnya = input("Masukkan nama penerbitnya: ")
                Bulan = {
                    1:"Januari", 2:"Februari", 3:"Maret", 4:"April", 5:"Mei", 6: "Juni",
                    7:"Juli", 8: "Agustus", 9: "September", 10:"Oktober", 11: "November", 12: "Desember"}
                tanggalpinjam = int(input("Masukkan tanggal peminjaman: "))
                bulanpinjam = int(input("Masukkan bulan pinjam: "))
                tahunpinjam = int(input("Masukkan tahun pinjam: "))
                print("\n")
                tanggalkembali = int(input("Masukkan tanggal pengembalian: "))
                bulankembali = int(input("Masukkan bulan kembali: "))
                tahunkembali = int(input("Masukkan tahun kembali: "))
                tanggal = tanggalkembali-tanggalpinjam
                bulan = bulankembali-bulanpinjam
                tahun = tahunkembali-tahunpinjam
                sebulan = bulan*30
                setahun = tahun*365
                jadi = setahun+sebulan+tanggal
                print(f"Lama peminjaman {jadi} hari", "kembali pada tanggal", tanggalkembali, "bulan", Bulan[bulankembali], "tahun", tahunkembali)
                denda = jadi - 7
                if denda <=3 and denda != 0:
                    print(f"Kamu terlambat selama {denda} hari, dan harus membayar denda sebesar 10.000")
                elif denda <=7 and denda != 0:
                    print(f"kamu terlambat selama {denda} hari dan harus membayar denda sebesar 15.000")
                elif denda > 7 and denda <= 30 and denda != 0:
                    print(f"kamu terlambat selama {denda} hari, dan harus membayar denda sebesar 25.000")
                elif denda >= 31:
                    print(f"Kamu terlambat selama {denda} hari, sehingga kamu tidak dapat meminjam selama waktu yang telah ditetapkan oleh pihak perpustakaan serta denda dengan nominal lebih dari standar karena terlambat")
                elif denda == 0:
                    print("Kamu tidak membayar denda apa pun")
                else:
                    print()
            else:
                print()
        elif menu == "3":
            print("=============================================================================")
            print("-------------------PENAMBAHAN BUKU MAKSIMAL BERJUMLAH 2 BUAH-----------------")
            print("=============================================================================")
            tambahberapa = int(input("Hanya boleh menambah 2 buku, mau tambah berapa? : "))
            for i in range(tambahberapa):
                tambah = input("Masukkan judul buku: ")
                penulis = input("Masukkan nama penulis: ")
                penerbit = input("Masukkan nama penerbit: ")
                print(f"{nama} telah menambah buku dengan judul {tambah} oleh {penulis} yang diterbitkan oleh {penerbit}")
                print("---------------------------------------------------------------------------------------------------------------")
        elif menu == "4":
            novel = 0
            komik = 0
            ensiklopedia = 0
            lainnya = 0
            tambahan = 0

            #novel += int(jumlahnovel)
            #komik += int(jumlahkomik)
            #ensiklopedia += int(jumlahensiklopedia)
            #lainnya += int(jumlahbuku)
            #tambahan += int(tambahberapa) + int(jumlahbuku)
            daftar_novel = novel + jumlahnovel
            daftar_komik = komik + jumlahkomik
            daftar_ensiklopedia = ensiklopedia + jumlahensiklopedia
            daftar_awallainnya = lainnya + jumlahbuku
            daftar_lainnya = daftar_awallainnya + tambahberapa

            print("<<<||>>>======= INI ADALAH DAFTAR BUKU YANG BARU SAJA DIPINJAM =======<<<||>>>")
            print("\t\t\t-", daftar_novel, "NOVEL")
            print("\t\t\t-", daftar_komik, "KOMIK")
            print("\t\t\t-", daftar_ensiklopedia, "ENSIKLOPEDIA")
            print("\t\t\t-", daftar_lainnya, "LAINNYA")
            print("<<<||>>>==============================================================<<<||>>>")

            from matplotlib import pyplot as plt
            from matplotlib import style

            style.use('ggplot')

            x = [0, 1, 2, 3]
            y = [daftar_novel, daftar_komik, daftar_ensiklopedia, daftar_lainnya]

            fig, ax = plt.subplots()

            ax.bar(x, y, align='center', color = "orange")
            ax.set_title('Jenis buku paling banyak dipinjam')
            ax.set_ylabel('Peminjam')
            ax.set_xlabel('Jenis buku')

            ax.set_xticks(x)
            ax.set_xticklabels(("Novel", "Komik", "Ensiklopedia", "Lainnya"))
            plt.show()
        elif menu == "5":
            print("ANDA TELAH KELUAR DARI PROGRAM")
            print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI")
            break
    except ValueError:
        print("TANGGAL, BULAN, DAN TAHUN HARUS BERUPA ANGKA!")


