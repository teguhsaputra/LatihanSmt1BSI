# def faktorial(a):
#     if a == 1:
#         return(a)
#     else:
#         return(a*faktorial(a-1))

# bil = int(input("Masukan Bilangan : "))

def test(a):
    if a == 1:
        return(a)
    else:
        return(a+test(a-1))

test(5)

# print("%d!= %d" % (bil,faktorial(bil)))