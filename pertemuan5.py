from fileinput import filename
from time import sleep
import os
# from os import path
import numpy as np
import json
import pandas as pd
from pandas.io.json import json_normalize 


def clear_screen():
    _ = os.system('cls')

def materi1():
    clear_screen()
    print("Materi 1 :")
    numbers = [7,5,9,8,9,9,0,8,4,0]
    sum = 0
    for each in numbers:
        sum = sum + each
    print("Jumlah Semuanya : ", sum)
    print("")
    input("Enter Untuk Lanjut ...")

def materi2():
    clear_screen()
    print("Materi 2 :")
    print(range(10))
    print(list(range(2,8)))
    print(list(range(2,20,3)))
    print("")
    input("Enter Untuk Lanjut ...")

def materi3():
    clear_screen()
    print("Materi 3 :")
    mapel = ['matematika','fisika','kimia']
    
    for i in range(len(mapel)):
        print("Saya Suka", mapel[i])
    print("")
    input("Enter Untuk Lanjut ...")

def materi4():
    clear_screen()
    print("Materi 4 :")
    count = 0
    while count < 5:
        print('The count is : ', count)
        count = count + 1
    print('Good Bye!')
    print("")
    input("Enter Untuk Lanjut ...")

def materi5():
    clear_screen()
    print("Materi 5 :")
    for letter in "PythonProgramming":
        if letter == "g":
            break
        print("Huruf sekarang : ", letter)
    print("Good Bye!")
    print("")
    input("Enter Untuk Lanjut ...")

def materi6():
    clear_screen()
    print("Materi 6 :")
    for letter in "PythonProgramming":
        if letter == "g":
            continue
        print("Huruf sekarang : ", letter)
    print("Good Bye!")
    print("")
    input("Enter Untuk Lanjut ...")

def materi7():
    clear_screen()
    print("Materi 7 :")
    count = 0
    while count < 8:
        print(count, "Kurang dari 8")
        count = count + 1
    else:
        print(count, "Tidak kurang dari 8")
    print("")
    input("Enter Untuk Lanjut ...")

def materi8():
    clear_screen()
    print("Materi 8 :")

def write_json(new_data, filename='datapertemuan5.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["tmp_data"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
    file.close

def delete_json():
    print("a")
    # new_data = {}
    # with open('datapertemuan5.json','w+') as file:
    #     file_data = json.load(file)
    #     # file_data["tmp_data"].append(new_data)
    #     # file.seek(0)
    #     json.dump(new_data, file, indent = 4)
    # file.close
    # with open(filename,'r+') as file:
    #     # file_data = json.load(file)
    #     dictionary = {
    #         "jenispotong": "",
    #         "harga": 1,
    #         "banyakpotong": 1,
    #         "jumlahharga": 1
    #     }
    #     json.dumps(dictionary, file, indent = 21)
    # file.close
    # with open(filename,'r+') as file:
    #     file_data = json.load(file)
    #     i = 0
    #     for entry in file_data["tmp_data"]:
    #         new_data.append(entry)
    #         i = i + 1
    #     # file_data["tmp_data"].append(new_data)
    #     json.dump(new_data, file, indent = 2)
    # file.close

def latihan1(i):
    clear_screen()
    print("Latihan 1 :")
    for x in range(i):
        x = x + 1
        print("===============================")
        print("Data %i : Looping" % (x))
        print("===============================")
        nim = input("Masukan NIM Anda : ")
        uts = int(input("Masukan Nilai UTS Anda : "))
        uas = int(input("Masukan Nilai UAS Anda : "))
        print("NIM Anda adalah %s nilai UTS Anda adalah %i nilai UAS Anda adalah %i " % (nim, uts, uas))
        print("========================================================================================")
    print("")
    input("Enter Untuk Lanjut ...")

def latihan2():
    clear_screen()
    print("Latihan 2 :")
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

        listobj = {
            "jenispotong": jenispotong,
            "harga": harga,
            "banyakpotong": banyakpotong,
            "jumlahharga": jumlahharga
        }
        write_json(listobj)
    print("==========================================================")
    print("GEROBAK FRIED CHICKEN")
    print("==========================================================")
    f = open("datapertemuan5.json", 'r')
    data = f.read()
    f.close()
    obj = json.loads(data)
    dataframe = pd.DataFrame(obj["tmp_data"])
    print(dataframe.head(100))
    print("==========================================================")
    jumlahharga = int(dataframe.jumlahharga.sum())
    pajak = jumlahharga*0.1
    totalbayar = jumlahharga-pajak
    print("{:>45}{:>0}".format("Jumlah Bayar Rp.",jumlahharga))
    print("{:>45}{:>0}".format("Pajak 10% Rp.",pajak))
    print("{:>45}{:>0}".format("Total Bayar Rp.",totalbayar))
    # delete_json()

# materi1()
# materi2()
# materi3()
# materi4()
# materi5()
# materi6()
# materi7()
# materi8()
# latihan1(2)
latihan2()