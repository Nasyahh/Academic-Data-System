from os import system

list_nim = []
list_nama = []
list_sem = []
list_tugas = []
list_uts = []
list_uas = []

def head():
    print('''SELAMAT DATANG DI SISTEM AKADEMIK MAHASISWA
        UNIVERSITAS XYZ 2022''')

def menu():
    system('cls')
    head()
    print('1. Tampilkan Data Mahasiswa')
    print('2. Tambahkan Data Mahasiswa')
    print('3. Perbarui Data Mahasiswa')
    print('4. Hapus Data Mahasiswa')
    print('5. Keluar Aplikasi')
    pilih_menu = input('Pilih Menu: ')
    if pilih_menu == '1':
        baca()
    elif pilih_menu == '2':
        tambah()
    elif pilih_menu == '3':
        ubah()
    elif pilih_menu == '4':
        hapus()
    elif pilih_menu == '5':
        keluar()
    else:
        lain = input('Maaf, Menu yang Anda masukkan tidak ada')
        system('cls')
        menu()

def baca():
    system('cls')
    head()
    print('Menu Daftar Nilai Mahasiswa')
    print('1. Tampilkan Semua Data Mahasiswa')
    print('2. Periksa Data Mahasiswa dengan NIM')
    print('3. Kembali ke Menu Utama')
    pilih_menu = input('Pilih Menu: ')
    if pilih_menu == '1':
        print('NIM\t | Nama Mahasiswa\t | Semester\t |Nilai Tugas\t | Nilai UTS\t | Nilai UAS\t |')
        if len(list_nim) != 0:
            for i in range(len(list_nim)):
                print(list_nim[i],'\t |',list_nama[i],'\t \t |',list_sem[i],'\t \t |',list_tugas[i],'\t \t |',list_uts[i],'\t \t |',list_uas[i],'\t\t |')
            selesai = input('Semua Data Telah Ditampilkan')
            baca()
        else:
            selesai = input('Tidak Ada Data Mahasiswa')
            baca()
    elif pilih_menu == '2':
        pilih_nim = input('Masukkan NIM: ')
        if pilih_nim in list_nim:
            i = list_nim.index(pilih_nim)
            print('NIM\t | Nama Mahasiswa\t | Semester\t |Nilai Tugas\t | Nilai UTS\t | Nilai UAS\t |')
            print(list_nim[i],'\t |',list_nama[i],'\t \t |',list_sem[i],'\t \t |',list_tugas[i],'\t \t |',list_uts[i],'\t \t |',list_uas[i],'\t\t |')
            selesai = input('Data Sudah Ditampilkan')
            baca()
        else:
            selesai = input('Tidak Ada Data Mahasiswa')
            baca()
    elif pilih_menu == '3':
        menu()
    else:
        selesai = input('Maaf, input yang Anda masukkan salah')
        baca()

def tambah():
    system('cls')
    head()
    print('1. Tambah Data Mahasiswa')
    print('2. Kembali ke Menu Utama')
    pilih_menu = input('Pilih Menu: ')
    if pilih_menu == '1':
        nim = input('NIM: ')
        if nim in list_nim:
            selesai = input('Data Sudah Ada')
            tambah()
        else:
            nama = input('Nama: ')
            semester = input('Semester: ')
            tugas = input('Nilai Tugas: ')
            uts = input('Nilai UTS : ')
            uas = input('Nilai UAS : ')
            opsi = input('Apakah Anda Akan Menyimpan Data ini? (Y/N): ')
            if opsi == 'Y' or opsi == 'y':
                list_nim.append(nim)
                list_nama.append(nama)
                list_sem.append(semester)
                list_tugas.append(tugas)
                list_uts.append(uts)
                list_uas.append(uas)
                selesai = input('Data Tersimpan')
                tambah()
            elif opsi == 'N' or opsi == 'n':
                selesai = input('Data Tidak Tersimpan')
                tambah()
            else:
                selesai = input('Maaf, input yang Anda masukkan salah')
                menu()
    elif pilih_menu == '2':
        menu()
    else:
        selesai = input('Menu Yang Anda Masukkan Salah, Kembali Ke Menu Utama')
        menu()


def ubah():
    system('cls')
    head()
    print('1. Ubah Data Mahasiswa')
    print('2. Kembali ke Menu Utama')
    pilih_menu = input('Pilih Menu: ')
    if pilih_menu == '1':
        print('Anda akan memperbarui Data Nilai Mahasiswa')
        nim = input('Masukkan NIM: ')
        if nim in list_nim:
            i = list_nim.index(nim)
            print('Memperbarui Data Mahasiswa')
            print('''1. Nama
2. Semester
3. Nilai Tugas
4. Nilai UTS
5. Nilai UAS''')
            opsi = input('Pilih Data: ')
            if opsi == '1':
                nama = input('Nama: ')
                list_nama[i] = nama
            elif opsi == '2':
                semester = input('Semester: ')
                list_sem[i] = semester
            elif opsi == '3':
                tugas = input('Nilai Tugas: ')
                list_tugas[i] = tugas
            elif opsi == '4':
                uts = input('Nilai UTS : ')
                list_uts[i] = uts
            elif opsi == '5':
                uas = input('Nilai UAS : ')
                list_uas[i] = uas
            else:
                selesai = input('Maaf, input yang Anda masukkan salah')
                ubah()
            selesai = input('Data Tersimpan')
            ubah()
        else:
            selesai = input('NIM belum terdaftar')
            ubah()
    elif pilih_menu == '2':
        menu()
    else:
        selesai = input('Maaf, input yang Anda masukkan salah')
        ubah()



def hapus():            
    system('cls')
    head()
    print('1. Hapus Data Mahasiswa')
    print('2. Kembali ke Menu Utama')
    pilih_menu = input('Pilih Menu: ')
    if pilih_menu == '1':
        print('Anda akan menghapus Data Mahasiswa')
        nim = input('Masukkan NIM: ')
        if nim in list_nim:
            i = list_nim.index(nim)
            del list_nim[i]
            del list_nama[i]
            del list_sem[i]
            del list_tugas[i]
            del list_uts[i]
            del list_uas[i]
            selesai = input('Data Sudah Terhapus')
            hapus()

        else:
            selesai = input('NIM tidak terdaftar')
            hapus()

    elif pilih_menu == '2':
        menu()
    else:
        selesai = input('Maaf, input yang Anda masukkan salah')
        hapus()

def keluar():
    selesai = input('Terima Kasih, Salam Sukses!')
    system('cls')

menu()