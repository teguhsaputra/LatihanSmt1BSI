from time import sleep
import os

def clear_screen():
    _ = os.system('cls')

def penugasan():
    print("===============================")
    print("Latihan 1 : Operator Penugasan")
    print("===============================")
    nilai_a = int(input("Masukan A : "))
    nilai_b = int(input("Masukan B : "))
    print("C = A + B")
    print("C = ",nilai_a+nilai_b)
    sleep(2)
    clear_screen()

def logika():
    print("===============================")
    print("Latihan 1 : Operator Logika")
    print("===============================")
    print("C = 10")
    nilai_a = int(input("Masukan Nilai A : "))
    nilai_b = int(input("Masukan Nilai B : "))
    nilai_c = 10
    if nilai_a and nilai_b == nilai_c:
        print("True : Nilai A & B == C")
    else:
        print("False : Nilai A & B != C")
    sleep(2)
    clear_screen()

def bitwise():
    print("===============================")
    print("Latihan 1 : Operator Bitwise")
    print("===============================")
    nilai_a = int(input("Masukan Nilai A : "))
    nilai_b = int(input("Masukan Nilai B : "))
    print("A & B = ", nilai_a & nilai_b)
    sleep(2)
    clear_screen()

def bitwise():
    print("===============================")
    print("Latihan 1 : Operator Bitwise")
    print("===============================")
    nilai_a = int(input("Masukan Nilai A : "))
    nilai_b = int(input("Masukan Nilai B : "))
    print("A & B = ", nilai_a & nilai_b)
    sleep(2)
    clear_screen()

def identitas():
    print("===============================")
    print("Latihan 1 : Operator Identitas")
    print("===============================")
    nilai_a = int(input("Masukan Nilai A : "))
    nilai_b = int(input("Masukan Nilai B : "))
    nilai_c = nilai_a is nilai_b
    # print("A & B = ", nilai_a & nilai_b)
    print(nilai_c)
    sleep(2)
    clear_screen()

def keanggotaan():
    print("===============================")
    print("Latihan 1 : Operator Keangotaan")
    print("===============================")
    print('x = ["kuliah", "bsiaja"]')
    x = ["kuliah","bsiaja"]
    nilai_a = input("Masukan Kata : ")
    print(nilai_a in x)
    sleep(2)
    clear_screen()

def tokomainananak():
    print("===============================")
    print("Latihan 2 : Toko Mainan Anak")
    print("===============================")
    namapembeli = input("Masukan Nama Pembeli : ")
    kodemainan = input("Masukan Kode Mainan : ")
    harga = int(input("Masukan Harga : "))
    jumlahbeli = int(input("Masukan Jumlah Beli : "))
    print("===============================")
    print("Nama Pembeli = ", namapembeli)
    print("Kode Mainan  = ", kodemainan)
    print("Harga        = ", harga)
    print("Jumlah Beli  = ", jumlahbeli)
    total = harga * jumlahbeli
    print("Total        = ", total)


penugasan()
logika()
bitwise()
identitas()
keanggotaan()
tokomainananak()