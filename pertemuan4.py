from time import sleep
import os

def clear_screen():
    _ = os.system('cls')

def materi1() :
    angka = 5
    if angka > 0:
        print(angka, "adalah bilangan positif.")
    angka = -1
    if angka > 0:
        print(angka, "adalah bilangan positif.")
    sleep(2)
    clear_screen()

def materi2() :
    bilangan = 8
    if bilangan >= 0:
        print("Positif atau Nol")
    else : 
        print("Bilangan Negatif")
    sleep(2)
    clear_screen()

def materi3() : 
    '''Di sini kita menguji apakah sebuah bilangan adalah bilangan positif, nol, atau negatif - dan menampilkan hasilnya ke layar '''
    bilangan = 5.5

    '''Coba juga mengganti bilangan jadi 
        bilangan = 0
        bilangan = -5.5'''
    if bilangan > 0:
        print("Bilangan positif")
    elif bilangan == 0:
        print("Nol")
    else:
        print("Bilangan Negatif")
    sleep(2)
    clear_screen()

def penjualanbaju():
    print("===============================")
    print("      Penjualan Baju")
    print("===============================")
    kode_baju = input("Masukan Kode Baju [SP/AD] : ")
    ukuran = input("Masukan Ukuran Baju [S/M] : ")
    if kode_baju == "SP" or kode_baju == "sp" :
        merk = "SuperDry"
        if ukuran == "S" or ukuran == "s":
            harga = 450000
        elif ukuran == "M" or ukuran == "m":
            harga = 500000
        else:
            harga = 0
    elif kode_baju == "AD" or kode_baju == "ad" :
        merk = "Adidas"
        if ukuran == "s" or ukuran == "S":
            harga = 650000
        elif ukuran == "M" or ukuran == "m" :
            harga = 700000
        else:
            harga = 0
    else:
        merk = "Anda Salah Input Kode Merk"
        harga = 0
    print("================================")
    print("Merk Baju : ", merk)
    print("Harga Baju : Rp.", harga)
    sleep(2)
    clear_screen()


def pejualantiket():
    print("===============================")
    print("      Penjualan Tiket Bus")
    print("             XYZ")
    print("===============================")
    namapembeli    = input("Masukan Nama Pembeli                      : ")
    nohp           = input("Masukan No. Handphone                     : ")
    kodejurusan    = input("Masukan Jurusan Yang Dipilih [SBY/BL/LMP] : ")
    if kodejurusan == "SBY" :
        namakotatujuan = "Surabaya"
        harga = 300000
    elif kodejurusan == "BL" :
        namakotatujuan = "Bali"
        harga = 350000
    else :
        namakotatujuan = "Lampung"
        harga = 500000
    print("Nama Kota Tujuan                          :",namakotatujuan)
    print("Harga                                     : Rp.",harga)
    jumlahbeli = int(input("Jumlah Beli                               : "))
    if jumlahbeli >=3 :
        potongan = (jumlahbeli*harga)*0.1
    else :
        potongan = 0    
    total = (jumlahbeli*harga)-potongan
    print("===============================")
    print("Potongan harga yang didapat  : Rp.",potongan)
    print("Total Bayar                  : Rp.",total)
    uangbayar = int(input("Masukan Uang Bayar : "))
    uangkembali = uangbayar-total
    print("Uang Kembali : Rp.",uangkembali)
    sleep(2)
    clear_screen()

def pendaftaranmaba():
    print("=================================")
    print("   Pendaftaran Mahasiswa Baru")
    print("===============================")
    nis     = input("Masukan NIS                   : ")
    nama    = input("Masukan Nama                  : ")
    jurusan = input("Masukan Kode Jurusan [SI/SIA] : ")
    print("=================================")
    if jurusan == "SI" :
        prodi = "Sistem Informasi"
        harga = 2400000
    else:
        prodi = "SIstem Informasi Akuntansi"
        harga = 2000000
    print("Prodi : ",prodi)
    print("harga : ",harga)
    sleep(2)
    clear_screen()

def gajikaryawan():
    print("=================================")
    print("   Program Hitung Gaji Karyawan  ")
    print("=================================")
    nama        = input("Masukan Nama Karyawan                : ")
    golongan    = int(input("Masukan Golongan Jabatan [1/2/3] : "))
    pendidikan  = input("Masukan Pendidikan [SMA/D1/D3/S1]    : ")
    jamkerja    = int(input("Masukan Jumlah Jam Kerja         : "))
    print("=================================")
    honor = 300000
    if golongan == 1 :
        tunja = 300000*0.05
    elif golongan == 2 :
        tunja = 300000*0.1
    else:
        tunja = 300000*0.15

    if pendidikan == "SMA" :
        tunpen = 300000*0.025
    elif pendidikan == "D1" :
        tunpen = 300000*0.05
    elif pendidikan == "D3" :
        tunpen = 300000*0.2
    else:
        tunpen = 300000*0.3 

    if jamkerja > 8 :
        lembur = jamkerja - 8
        uanglembur = lembur*3500
    else : 
        uanglembur = 0

    print("Karyawan Yang Bernama    : ",nama)
    print("Honor Yang Di Terima     : ",honor)
    print("Tunjangan Jabatan        : ",tunja)
    print("Tunjangan Pendidikan     : ",tunpen)
    print("Honor Lembur             : ",uanglembur)
    totalgaji = honor+tunja+tunpen+uanglembur
    print("---------------------------------- +")
    print("Total Gaji Rp.",totalgaji)
    sleep(2)
    clear_screen()


materi1()
materi2()
materi3()
penjualanbaju()
pejualantiket()
pendaftaranmaba()
gajikaryawan()