'''
# Function Initialization :
def urai(x):
    total_kata = ""
    banyak = len(x)
    sub_kata = ""

    for i in range(0,banyak) :
        for j in range(i,i+1) :
            kata = x[j]
            sub_kata = sub_kata + kata
        total_kata = total_kata + sub_kata
    return total_kata
 '''

# def rajut(y):
    
x = 'CCoCodCode'
list_x = list(x)
banyak = len(x)
total_kata = ""
sub_kata = ""

count = 0
baris=0
for j in range(0, banyak):
    baris= baris + j
    banyak = banyak - baris
    if banyak >0 :
        count +=1
print(count)


for i in range(0,banyak):
    for j in range(i-1,-1,-1):
        kata = list_x.pop(j)

        print(list_x)


            


# l = list_x[1]
# print(l)
# k = list_x.pop(1)
# print(list_x)



# # Use the function
# print(urai('Code'))
# print(urai('Python'))
# print(urai('Purwadhika'))
