import modul_pertemuan10 as aritmatika
import os
from math import*
import sys

def clear_screen():
    _ = os.system('cls') 

def materi1(a,b):
    print("Materi 1")
    print("============================")
    print(aritmatika.penjumlahan(a,b))
    input("Tekan Enter Untuk Lanjut ... ")
    clear_screen()

def materi2(a,b):
    print("Materi 2")
    print("============================")
    pangkat_bilangan = pow(a,b)
    print("Hasil dari pemangkatan bilangan adalah : ", pangkat_bilangan)
    input("Tekan Enter Untuk Lanjut ... ")
    clear_screen()

def materi3():
    print("Materi 3")
    print("============================")
    bil = int(input("Masukan sebuah bilangan positif : "))
    faktorial_bil = factorial(bil)
    print("Bilangan faktorial dari bil adalah : ", faktorial_bil)    
    input("Tekan Enter Untuk Lanjut ... ")
    clear_screen()

def materi4(a,b):
    print("Materi 4")
    print("============================")
    pangkat_bilangan = pow(a,b)
    print("Hasil dari pemangkatan bilangan adalah : ", pangkat_bilangan)

    bil = int(input("Masukan sebuah bilangan positif : "))
    faktorial_bil = factorial(bil)
    print("Bilangan faktorial dari bil adalah : ", faktorial_bil)    
    input("Tekan Enter Untuk Lanjut ... ")
    clear_screen()

def materi5():
    print("Materi 5")
    print("===========================")
    lists = ['a',0,4]
    for each in lists:
        try:
            print("Masukan : ", each)
            r = 1/int(each)
            break
        except:
            print("Upps!", sys.exc_info()[0], " terjadi.")
            print("Masukan berikutnya.")
            print()
    print("Kebaikan dari ", each, " =", r)
    input("Tekan Enter Untuk Lanjut ... ")
    clear_screen()

def materi6():
    print("Materi 6")
    print("===========================")
    try:
        a = int(input("Masukkan sebuah bilangan positif : "))
        if a <= 0 : 
            raise ValueError("Itu bukan bilangan positif!")
    except ValueError as ve: 
        print(ve)
    input("Tekan Enter Untuk Lanjut ... ")
    clear_screen()

materi1(10,20)
materi2(3,3) 
materi3()  
materi4(3,3)
materi5()
materi6()