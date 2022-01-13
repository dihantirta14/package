import model.daftar_nilai

from os import system

d_nama = []
d_nim = []
d_kelas = []
d_jurusan = []
d_hadir = []
d_tugas = []
d_uts = []
d_uas = []
d_akhir = []
def judul():
    print('=====================================')
    print('|    PROGRAM NILAI DATA MAHASISWA   |')
    print('=====================================')

def tambah():
    system('cls')
    judul()
    print('Tambah Data'.center(40))
    print('=====================================')
    jurusan = input ('Prodi [TI/SI] : ')
    if jurusan == 'TI' or jurusan == 'ti':
        j = 'Teknik Infomatika'
        d_jurusan.append(j)
    elif jurusan == 'SI' or jurusan == 'si':
        j = 'Sistem Informasi'
        d_jurusan.append(j)
    else:
        kembali = input('Pilihan Tidak Ada')
        tambah()
    nama = input('Nama  : ')
    d_nama.append(nama)
    nim = input('Nim   : ')
    d_nim.append(nim)
    kelas = input('Kelas :')
    d_kelas.append(kelas)

    system('cls')
    judul()
    print('Tambah Data'.center(40))
    print('=====================================')
    hadir = float(input('Jumlah Hadir : '))
    j_hadir = ((hadir/16)*20/100)*100
    d_hadir.append(j_hadir)

    tugas = float(input('Nilai Tugas  :'))
    j_tugas = tugas*(25/100)
    d_tugas.append(j_tugas)

    uts = float(input('Nilai UTS  :'))
    j_uts = uts*(25/100)
    d_uts.append(j_uts)

    uas = float(input('Nilai UAS  : '))
    j_uas = uas*(30/100)
    d_uas.append(j_uas)

    total = j_hadir+j_tugas+j_uts+j_uas
    d_akhir.append(total)
    print ('Data Tersimpan'.center(40))
    kembali = input('Kembali [enter]')

    model.daftar_nilai.menu_dosen()


