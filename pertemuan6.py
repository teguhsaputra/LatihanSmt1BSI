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
    print("Materi 6 : ")
    genap = [2,4,6]
    print(genap+[8,10,12])
    print(['p','y'] * 2)
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi7():
    print("Materi 7 : ")
    ganjil = [5,7,11,13,15]
    ganjil.insert(2,9)
    print(ganjil)
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi8():
    print("Materi 8 : ")
    my_list = ['p','y','t','h','o','n','i','n','d','o']
    my_list.remove('p')
    print(my_list)
    my_list.remove('n')
    print(my_list.pop(1))
    del my_list[2]
    print(my_list)
    my_list.clear()
    print(my_list)
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi9():
    print("Materi 9 : ")
    alfabet = ['a','b','d','f','e','c','h','g','j','i']
    alfabet.sort()
    print(alfabet)
    alfabet.sort(reverse=True)
    print(alfabet)
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi10():
    print("Materi 10 : ")
    alfabet = ['a','c','d','e','b']
    alfabet.reverse()
    print(alfabet)
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi11():
    print("Materi 11 : ")
    my_tuple = ()
    print(my_tuple)
    my_tuple = (1,)
    print(my_tuple)
    my_tuple = (1,2,3)
    print(my_tuple)
    my_tuple = ("hello",[1,2,3],(4,5,6))
    print(my_tuple)
    my_tuple = 1,2,3
    a,b,c = my_tuple
    print(a,b,c)
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi12():
    print("Materi 12 : ")
    my_tuple = ('p','r','o','g','r','a','m','m','i','n','g')
    print(my_tuple[:3])
    print(my_tuple[2:6])
    print(my_tuple[3:])
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi13():
    print("Materi 13 : ")
    my_tuple = (2,3,4,[5,6])
    my_tuple[3][0] = 7
    print(my_tuple)
    my_tuple = ('p','y','t','h','o','n')
    print(my_tuple)
    del my_tuple
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi14():
    print("Materi 14 : ")
    my_tuple = (1,2,3,'a','b','c')
    print('3' in my_tuple)
    print('e' in my_tuple)
    print('k' not in my_tuple)
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi15():
    print("Materi 15 : ")
    nama = ('Galih','Ratna')
    for name in nama:
        print('Hi', name)
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi16():
    print("Materi 16 : ")
    my_tuple = ('p','y','t','o','n','i','n','d','o')
    print(my_tuple.count('n'))
    print(my_tuple.index('n'))
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def materi17():
    print("Materi 17 : ")
    arr2d = (1,[4,7,0],2,[5,8],3,[6,9])
    print(arr2d[0])
    print(arr2d[2])
    print(arr2d[4])
    print(arr2d[5][1])
    print(arr2d[1][2])
    input("Tekan Enter Untuk Lanjut ...")
    clear_screen()

def latihan():
    print("Latihan : ")
    list_nim = []
    list_uts = []
    list_uas = []
    list_total = []

    ulang = 2
    for i in range(ulang):
        print("data Ke -" + str(i+1))
        list_nim.append(input("Masukkan Nim Anda : "))
        list_uts.append(int(input("Masukkan Nilai UTS Anda : ")))
        list_uas.append(int(input("Masukkan Nilai UAS Anda : ")))
    
    for i in range(ulang):
        list_total.append((list_uas[i] + list_uts[i])/2)
    
    print("=====================================================")
    print("Nim\t Nilai UTS\t Nilai UAS\t Total\t")
    print("=====================================================")
    for i in range(ulang):
        print("%s\t %i\t\t %i\t\t %i" % (list_nim[i],list_uts[i],list_uas[i],list_total[i]))
    print("=====================================================")  

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
latihan()