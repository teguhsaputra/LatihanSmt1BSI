from time import sleep
import os

def clear_screen():
    _ = os.system('cls')

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



pejualantiket()
pendaftaranmaba()
gajikaryawan()