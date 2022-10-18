border = 41*"="
print(border)
print("{:<10}{:^10}{:>10}".format("=","Gerobak Fried Chicken","="))
print(border)
print("Kode Potong\t Jenis Potong\t Harga")
d = "Rp. 2500"
p = "Rp. 2000"
s = "Rp. 1500"
D = "Dada"
P = "Paha"
S = "Sayap"
print(
"""D\t\t {D}\t\t {d}
P\t\t {P}\t\t {p}
S\t\t {S}\t\t {s}
{b}
""".format(d = d,D = D,p = p,P = P,s = s,S = S,b = border))

listkodePotong = []
listbanyakPotong = []
listhargaSatuan = []
listjenisPotong = []
listtotalHarga = []

banyakJenis = int(input("Banyak Jenis : "))
for i in range(banyakJenis):
    print()
    print("Jenis Ke : ",i+1)
    listkodePotong.append(input("Kode Potong [D/P/S] : "))
    listbanyakPotong.append(int(input("Banyak Potong : ")))
    if listkodePotong[i] == "d" or listkodePotong[i] == "D":
        listhargaSatuan.append(2500)
        listjenisPotong.append("Dada")
    elif listkodePotong[i] == "p" or listkodePotong[i] == "P":
        listhargaSatuan.append(2000)
        listjenisPotong.append("Paha")
    elif listkodePotong[i] == "s" or listkodePotong[i] == "S":
        listhargaSatuan.append(1500)
        listjenisPotong.append("Sayap")
    else:
        listhargaSatuan.append(0)
        listjenisPotong.append("Null")

border2 = 93*"="
print(border2)
print("{:<36}{:^0}{:>36}".format("=","Gerobak Fried Chicken","="))
print(border2)
print(
"""No.\t Jenis Potong\t\t Harga Satuan\t\t Banyak Beli\t\t Jumlah Harga\n{border2}""".format(border2 = border2))
for x in range(banyakJenis):
    listtotalHarga.append(listhargaSatuan[x]*listbanyakPotong[x])
    print("""{no}\t {jp}\t\t\t {hs}\t\t\t {bl}\t\t\t {jh}""".format(no = x+1,jp = listjenisPotong[x], hs = listhargaSatuan[x], bl = listbanyakPotong[x],jh = listtotalHarga[x]))
    # print(""" %i """.format(listjenisPotong[x]))
print(border2)
JB = sum(listtotalHarga)
PJ = sum(listtotalHarga)*0.1
TB = JB-PJ
print(8*"\t","Jumlah Bayar\t {jb}".format(jb = JB))
print(8*"\t","Pajak 10%\t {pj}".format(pj = PJ))
print(8*"\t","Total Bayar\t {tb}".format(tb = TB))