from ast import operator
from time import sleep
import os
import decimal
import fractions
import math

def clear_screen():
    _ = os.system('cls')

def materi1() :
    var1 = "Hello Python"
    var2 = "Programming With Python"
    print(var1)
    print(var2)
    sleep(2)
    clear_screen()

def materi2() :
    var1 = "Hello Python!"
    var2 = "I Love Python"
    print("Var1[0]:", var1[0])
    print("Var2[2:6]:", var2[2:6])
    sleep(2)
    clear_screen()

def materi3() :
    var1 = "Hello Python!"
    var2 = var1[:6]
    print(var1)
    print("String Update: - ", var1[:6] + "World")
    sleep(2)
    clear_screen()

def materi4() :
    str1 = "Hello"
    str2 = "Python"
    print("str1 + str2 = ", str1 + str2)
    print("str1 * 3 =",str1 * 3)
    sleep(2)
    clear_screen()

def materi5() :
    string = "I Love Python"
    print(len(string))
    sleep(2)
    clear_screen()

def materi6() :
    print('''"He Said, What's there?"''')
    print('He Said, "What\'s there?"')
    print("He Said, \"What\'s there?\"")
    sleep(2)
    clear_screen()

def materi7() :
    print("Ini adalah baris pertama\nDan ini baris dua")
    print("Ini adalah \x48\x45\x58")
    sleep(2)
    clear_screen()

def materi8() : 
    print("This is \x61 \ngood example")
    print(r"This is \x61 \ngood example")
    sleep(2)
    clear_screen()

def materi9() :
    default_order = "{}, {} dan {}".format("Budi", "Galih", "Ratna")
    print('\n--- Urutan Default ---')
    print(default_order)
    sleep(2)
    clear_screen()

    positional_order = "{1}, {0} dan {2}".format("Budi", "Galih", "Ratna")
    print('\n--- Urutan berdasarkan posisi ---')
    print(positional_order)
    sleep(2)
    clear_screen()

def materi10() :
    print("{0} bila diubah jadi biner menjadi {0:b}".format(12))
    print("Format eksponensial: {0:e}".format(1566.345))
    print("Sepertiga sama dengan: {0:.3f}".format(1/3))
    print("|{:<10}|{:^10}|{:>10}|".format('beras','gula','garam'))
    sleep(2)
    clear_screen()

def materi11() :
    x = 12.3456789
    print('Nilai x = %3.2f' %x)
    print('Nilai x = %3.4f' %x)
    sleep(2)
    clear_screen()

def materi12() :
    print("Universitas Bina Sarana Informatika".lower())
    print("Universitas Bina Sarana Informatika".upper())
    print("I love programming in Python".split())
    print("I Love Python".startswith("I"))
    print("Saya Belajar Python".endswith("on"))
    print(' - '.join(['I','Love','you']))
    print("Belajar java di BSI".replace('Java','Python'))
    sleep(2)
    clear_screen()

def materi13() :
    print(int(2.5))
    print(int(3.8))
    print(float(5))
    sleep(2)
    clear_screen()

def materi14() :
    print((1.1 + 2.2) == 3.3)
    print(1.1 + 2.2)
    sleep(2)
    clear_screen()

def materi15() :
    print(0.1)
    print(decimal.Decimal(0.1))
    sleep(2)
    clear_screen()

def materi16() :
    print(fractions.Fraction(1.5))
    print(fractions.Fraction(1,3))
    sleep(2)
    clear_screen()

def materi17() :
    print(fractions.Fraction(1,3) + fractions.Fraction(1,3))
    print(1 + fractions.Fraction(5,6))
    print(fractions.Fraction(-3,10) < 0)
    sleep(2)
    clear_screen()

def materi18() :
    print(math.pi)
    print(math.cos(math.pi))
    print(math.exp(5))
    print(math.log10(100))
    print(math.factorial(5))
    sleep(2)
    clear_screen()

def materi19() :
    nilai1 = 10
    nilai2 = 8
    penjumlahan = nilai1 + nilai2
    print(nilai1, "+", nilai2, "= ", penjumlahan)
    pengurangan = nilai1 - nilai2
    print(nilai1, "-", nilai2, "= ", pengurangan)
    perkalian = nilai1 * nilai2
    print(nilai1, "*", nilai2, "= ", perkalian)
    pembagian = nilai1/nilai2
    print(nilai1, "/", nilai2, "= ", pembagian)
    pemangkatan = nilai1 ** nilai2
    print(nilai1, "**", nilai2, "= ", pemangkatan)
    pembagian_bulat = nilai1//nilai2
    print(nilai1, "//", nilai2, "= ", pembagian_bulat)
    sleep(2)
    clear_screen()

def materi20() :
    nama = input("Masukan Nama Anda : ")
    print("Hai " + nama + " Selamat Bergabung di UKM Mapasika")
    sleep(2)
    clear_screen()

def materi21() :
    nilai1 = int(input("Masukan Nilai Pertama : "))
    nilai2 = int(input("Masukan Nilai Kedua : "))
    penjumlahan = nilai1 + nilai2
    print(nilai1, "+", nilai2, "= ", penjumlahan)
    pengurangan = nilai1 - nilai2
    print(nilai1, "-", nilai2, "= ", pengurangan)
    perkalian = nilai1 * nilai2
    print(nilai1, "*", nilai2, "= ", perkalian)
    pembagian = nilai1/nilai2
    print(nilai1, "/", nilai2, "= ", pembagian)
    pemangkatan = nilai1 ** nilai2
    print(nilai1, "**", nilai2, "= ", pemangkatan)
    pembagian_bulat = nilai1//nilai2
    print(nilai1, "//", nilai2, "= ", pembagian_bulat)
    sleep(2)
    clear_screen()

def materi22() :
    nilai1 = int(input("Masukan Nilai Pertama : "))
    nilai2 = int(input("Masukan Nilai Kedua : "))
    operator_lebih_besar = nilai1 > nilai2
    print(nilai1, ">", nilai2, "adalah ", operator_lebih_besar)
    operator_lebih_kecil = nilai1 < nilai2
    print(nilai1, "<", nilai2, "adalah ", operator_lebih_kecil)
    operator_sama_dengan = nilai1 == nilai2
    print(nilai1, "==", nilai2, "adalah ", operator_sama_dengan)
    operator_tidak_sama_dengan = nilai1 != nilai2
    print(nilai1, "!=", nilai2, "adalah ", operator_tidak_sama_dengan)
    sleep(2)
    clear_screen()

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

materi1()
materi2()
materi3()
materi4()
materi5()
materi6()
materi7()
materi8()
materi9()
materi10()
materi11()
materi12()
materi13()
materi14()
materi15()
materi16()
materi17()
materi18()
materi19()
materi20()
materi21()
materi22()
penugasan()
logika()
bitwise()
identitas()
keanggotaan()
tokomainananak()