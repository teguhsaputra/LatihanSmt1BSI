from ast import arg
import os

total = int()

def clear_screen():
    _ = os.system('cls')

def materi1(nama):
    print("Materi 1")
    print("Hi, "+ nama +". Apa Kabar ?")
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi2(str):
    print("Materi 2")
    print(str)
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi3(nama,usia):
    print("Materi 3")
    print("Nama: ", nama)
    print("Usia: ", usia)
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi4(nama, usia = 17):
    print("Materi 4")
    print("Nama: ", nama)
    print("Usia: ", usia)
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi5(arg1, *vartuple):
    print("Materi 5")
    print("Outputnya adalah: ")
    print(arg1)
    for var in vartuple:
        print(var)
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi6(arg1, arg2):
    print("Materi 6")
    total = arg1 + arg2
    print("Di dalam fungsi nilai total : ", total)
    return total

materi1("Umar")
materi2(str = "Hello Python")
materi3(usia = 25, nama = "Budi")
materi4(usia = 29, nama = "Galih")
materi4(nama = "Galih")
materi5(10)
materi5(10, 30, 50, 70)
materi6(10,20)
print("Di luar fungsi, nilai total : ", total)

