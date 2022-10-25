import os

from numpy import matrix

def clear_screen():
    _ = os.system('cls')

def materi1():
    print("Materi 1 : ")
    matriksA = [[1,0], [0,1]]
    print(matriksA)

    matriksB = [[1,0,1], [0,1,0], [1,0,1]]
    print(matriksB)

    matriksC = [[1,0,1,0], [0,1,0,1], [1,0,1,0], [0,1,0,1]]
    print(matriksC)

    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi2():
    print("Materi 2 : ")
    matrik = [
        [5,0],
        [2,6]
    ]
    print(matrik)
    matrik1 = [
        [5,0,8],
        [2,6,7],
        [1,3,4],
    ]
    print(matrik1)
    matrik2 = [
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1],
    ]
    print(matrik2)
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

materi1() 
materi2() 