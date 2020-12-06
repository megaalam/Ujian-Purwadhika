#Ujian Modul 1
#JCDSAH
#Mega Alam


A = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

def counterClockwise(x) :
    tambah = lambda x, y : x + y

    def duplikat(j) :
        duplikat =[]
        for k in range(0,len(A)) :
            k = k
            duplikat.append(j)
        return duplikat

    pola = [3, 6]
    final = []
    for i in range(len(A), 0, -1) :
        jumlah_list = list(map(tambah, duplikat(i), pola))
        hasil = [i] + jumlah_list
        final.append(hasil)

    return final

# Use the Function
print(counterClockwise(A))

# print(duplikat(1))

# def jumlah(x,y):
#     hasil = x+y
#     return hasil

# C = []
# for i in range(0,3) :
#     hasil = jumlah(K[i],L[i])
#     C.append(hasil)

# print(C)