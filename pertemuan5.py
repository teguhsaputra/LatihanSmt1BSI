from time import sleep
import os
import numpy as np


def clear_screen():
    _ = os.system('cls')

def latihan(i):
    i = i + 1
    print("===============================")
    print("Data %i : Looping" % (i))
    print("===============================")
    nim = input("Masukan NIM Anda : ")
    uts = int(input("Masukan Nilai UTS Anda : "))
    uas = int(input("Masukan Nilai UAS Anda : "))
    print("NIM Anda adalah %s nilai UTS Anda adalah %i nilai UAS Anda adalah %i " % (nim, uts, uas))
    print("========================================================================================")

def tugas():
    print("==================================")
    print("GEROBAK FRIED CHICKEN")
    print("==================================")
    print("Kode     Jenis Potong     Harga")
    print("D        Dada             Rp. 2500")
    print("P        Paha             Rp. 2000")
    print("S        Sayap            Rp. 1500")
    print("==================================")
    banyakjenis = int(input("Banyak Jenis : "))
    print("==================================")
    for x in range(banyakjenis):
        x = x+1
        print("Jenis Ke : ",x )
        kodepotong = input("Kode Potong [D/P/S] : ")
        banyakpotong = int(input("Banyak Potong : "))
        if x == 1 : 
            print("GEROBAK FRIED CHICKEN")
            print("======================================================================")
            print("No.     Jenis Potong     Harga Satuan     Banyak Beli     Jumlah Harga")
            print("----------------------------------------------------------------------")
        if kodepotong == "D" :
            jenispotong = "Dada"
            harga = 2500
        elif kodepotong == "P" :
            jenispotong = "Paha"
            harga = 2000
        else:
            jenispotong = "Sayap"
            harga = 1500
        jumlahharga = banyakpotong * harga
        print("%i     %s     %i     %i     %i" % (x, jenispotong, harga, banyakpotong, jumlahharga))
    
# for i in range(2) :
#     latihan(i)

tugas()

# jumlahdata = 3
# for i in range(jumlahdata)
#     i = i + 1
#     np[]    

# a = np.array([[],[],[]])
# a = np.insert(a,0,["ayang","goreng"])
# a = np.append([["test1","test2"]])
# print(a)