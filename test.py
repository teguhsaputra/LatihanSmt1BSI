
def test1():
    mapel = ['matematika', 'fisika', 'kimia']
    for i in range(len(mapel)) : 
        print("Saya suka", mapel[i])

def test2():
    count = 0
    while (count < 5) :
        print('The count is :', count)
        count = count + 1
    print('Good Bye!')

def test3():
    nilai = 20
    while(nilai >= 0):
        print("Ini adalah angka : ",nilai)
        nilai = nilai-2

def test4():
    nilai = 10

def test5():
    ulang = 2
    for i in range(ulang):
        nim = input("Masukan NIM Anda : ")
        uts = int(input("Masukan Nilai UTS Anda : "))
        uas = int(input("Masukan Nilai UAS Anda : "))
        # print("Nim Anda adalah %s nilai UTS Anda %i nilai UAS Anda %i" %(nim,uts,uas))
        print("nim anda adalah",nim,"nilai uts anda",uts,"nilai uas anda",uas)

def test6():
    print("=====================")
    print("Gerobak Fried Chicken")
    print("=====================")
    print("Kode JenisPotong Harga")
    print("D    Dada    Rp. 2500")
    print("P    Paha    Rp. 2000")
    print("S    Sayap   Rp. 1500")
    print("======================")

    banyakjenis = int(input("Banyak Jenis : "))
    kodepotong = input("Kode Potong [D/P/S] : ")
    print("Banyak Jenis : ", x)
    banyakpotong = int(input("Banyak Potong : "))

    if(kodepotong == "D"):
        jenispotong = "Dada"
        harga = 2500
    elif(kodepotong == "P"):
        jenispotong = "Paha"
        harga = 2000
    else:
        jenispotong = "Sayap"
        harga = 1500
    
    cetak = f'''

        for x in range(banyakjenis):
            x = x + 1
            jumlahharga = harga*banyakpotong
            jumlahbayar = jumlahharga + jumlahbayar
            print(x,"      ",jenispotong,"     ",harga,"      ",banyakpotong,"      ",jumlahharga)

'''
    print("==========================================================================")
    print("                         Gerobak Fried Chicken                            ")
    print("==========================================================================")
    print("No.      Jenis Potong      Harga Satuan      Banyak Beli      Jumlah Harga")
    print("==========================================================================")
    
    print("==========================================================================")
    pajak = 0.1*jumlahbayar
    print("                                            Jumlah Bayar Rp. ", jumlahbayar)
    print("                                               Pajak 10% Rp. ", pajak)
    totalbayar = jumlahbayar - pajak
    print("                                             Total Bayar Rp. ", totalbayar)


test6()
# test5()
# test3()
# test1()

