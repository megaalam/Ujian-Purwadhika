#Ujian Modul 1
#JCDSAH
#Mega Alam

try :
    n = int(input("Masukkan detik : "))
    if n < 359999 :
        x = n % 60 # sisa detik
        k = n // 60 # jumlah menit
        
        y = k % 60 # sisa menit
        z = k // 60 # jumlah jam

        # while len(str(z)) <= 1 or len(str(y)) <= 1 <= len(str(x)) == 1 :
        #     nol = "0"

        # if len(str(z)) == 1 or len(str(y)) == 1 or len(str(x)) == 1:
        #     nol = "0"
        # else :
        #     nol = ""
    
        print(f"{z} : {y} : {x}")
    
    else :
        print("Invalid Input!")

except :
    print("Invalid Input!")

