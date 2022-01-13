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

def lihat():
    system('cls')
    judul()

    for i in range (len(d_nim)):

        print('%d. Nama        : %s'%(i+0, d_nama[i]))
        print('    Nim         : %s'%d_nim[i])
        print('    Kelas       : %s'%d_kelas[i])
        print('    Prodi       : %s'%d_jurusan[i])
        print('    Kehadiran   : %.2f'%d_hadir[i])
        print('    Tugas       : %.2f'%d_tugas[i])
        print('    UTS         : %.2f'%d_uts[i])
        print('    UAS         : %.2f'%d_uas[i])
        print('    Nilai Akhir : %.2f'%d_akhir[i])
        print('---------------------------')
    kembali = input('Kembali Tekan [enter]')
    model.daftar_nilai.menu_dosen()