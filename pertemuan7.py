import os
import pandas as pd

from numpy import mat, matrix

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
    
    print("Materi 1.2 : ")
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

def materi2():
    
    mat1 = [
        [9,0],
        [3,6],
    ]
    mat2 = [
        [6,2],
        [7,2],
    ]

    for x in range(0, len(mat1)):
        for y in range(0, len(mat1[0])):
            print(mat1[x][y] + mat2[x][y], end=' '),
        print()
    clear_screen()

def materi3():
    print("Materi 3 : ")
    mat1 = [
        [9, 0],
        [3, 6],
    ]

    mat2 = [
        [6, 0],
        [7, 2],
    ]

    for x in range(0, len(mat1)):
        for y in range(0, len(mat1[0])):
            print (mat1[x][y] - mat2[x][y], end=' ')
    clear_screen()

def materi4():
    print("Materi 4 : ")
    mat1= [
        [9,0],
        [3,6]
    ]
    mat2= [
        [6,0],
        [7,2],
    ]
    mat3 = []
    for x in range(0, len(mat1)):
        row = []
        for y in range(0, len(mat1)):
            total = 0
            for z in range(0, len(mat1[0])):
                total = total + (mat1[x][z] * mat2[z][y])
            row.append(total)
        mat3.append(row)

    for x in range(0, len(mat3)):
        for y in range(0, len(mat3[0])):
            print(mat3[x][y], end=' ')
        print()

def materi5():
    print("Materi 5 : ")

    clear_screen()

def modulPandas():
    list_nim = []
    list_nama = []
    list_uts = []
    list_uas = []
    list_total = []

    ulang=5
    for i in range(ulang):
        print("Data ke - " + str(i+1))
        list_nim.append(input("Nim : "))
        list_nama.append(input("Nama : "))
        list_uts.append(int(input("Nilai UTS : ")))
        list_uas.append(int(input("Nilai UAS : ")))
    for i in range(ulang):
        list_total.append((list_uas[i] + list_uts[i]) / 2)

    tamu = {
        "NIM" : list_nim,
        "Nama Lengkap" : list_nama,
        "Nilai UTS" : list_uts,
        "Nilai UAS" : list_uas,
        "Rata-rata" : list_total
    }

    data_tamu = pd.DataFrame(tamu)

    print("="*20)
    print(data_tamu)
    print("="*20)

# materi1() 
# materi2() 
# materi3()
# materi4()
modulPandas()