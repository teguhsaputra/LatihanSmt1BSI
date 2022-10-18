import os

def clear_screen():
    _ = os.system('cls')

def materi1():
    print("Materi 1 : ")
    my_list = ["I","love","python","programming",2017]
    my_list[0]
    my_list[2]
    your_list = ["hello", [1, 2, 3], "python"]
    print(your_list[1][0])
    print(your_list[1][2])
    my_list[4]
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi2():
    print("Materi 2 : ")
    my_list = ['p','y','t','h','o','n']
    print(my_list[-1])
    print(my_list[-3])
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi3():
    print("Materi 3 : ")
    my_list = ['p','y','t','h','o','n','i','n','d','o']
    print(my_list[3:6])
    print(my_list[4:])
    print(my_list[:5])
    print(my_list[-1:-5])
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi4():
    print("Materi 4 : ")
    ganjil = [1,3,4,7,9]
    ganjil[2] = 5
    print(ganjil)
    ganjil[2:5] = [11,13,15]
    print(ganjil)
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi5():
    print("Materi 5 : ")
    ganjil = [1,3,5,7]
    ganjil.append(9)
    print(ganjil)
    ganjil.extend([11,13,15])
    print(ganjil)
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi6():
    print("Materi 5 : ")
    genap = [2,4,6]
    print[2,4,6]
    clear_screen()


materi1()
materi2()
materi3()
materi4()
materi5()