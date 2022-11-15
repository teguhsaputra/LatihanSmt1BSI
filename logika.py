# def faktorial(a):
#     if a == 1:
#         return(a)
#     else:
#         return(a*faktorial(a-1))

# bil = int(input("Masukan Bilangan : "))

# def test(a):
#     if a == 1:
#         return(a)
#     else:
#         return(a+test(a-1))

# test(5)


# jum = 0
# x = 0
# while x < 9:
#     x = x+1
#     jum = jum + x
# print(jum)

totalbelanja = 90000
diskon = 0
if totalbelanja > 100000:
    diskon = totalbelanja * 0.05
bayar = totalbelanja-diskon
print(bayar) 

# print("%d!= %d" % (bil,faktorial(bil)))