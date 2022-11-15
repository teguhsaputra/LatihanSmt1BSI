def  cetak_matriks(matriks):
    for row in matriks:
        print(row)

def panjang_matriks(matriks):
    return len(matriks[0])

def lebar_matriks(matriks):
    return len(matriks)

def hitung_matriks(mat_a, mat_b):
    temp_row = []
    temp_mat = []
    for i in range(0, lebar_matriks(mat_a)):
        for j in range(0, panjang_matriks(mat_a)):
            temp_row.append(mat_a[i][j] + mat_b[i][j])
        temp_mat.append(temp_row)
        temp_row  = []
    return temp_mat

matriks_a = [[1,2,3],[3,2,1],[2,2,2]]
matriks_b = [[2,3,4],[5,4,2],[4,1,2]]

print("Kelompok 5 : ")
print("Teguh Saputra nim(19220747)")
print("Aditya Dwicahya nim(19220038")
print("========================")

print("Matriks A : ")
cetak_matriks(matriks_a)

print("Matriks B : ")
cetak_matriks(matriks_b)

print("Hasil Penjumlahan Matriks : ")
hasil = hitung_matriks(matriks_a, matriks_b)
cetak_matriks(hasil)