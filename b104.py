str = input()
mas = str.split(" ")
str_1 = input()
mas_1 = str_1.split(" ")
str_2 = input()
mas_2 = str_2.split(" ")
k = 0
for i in range(len(mas_1)):
    for j in range(len(mas_2)):
        if mas_1[i] == mas_2[j]:
            k = 1
if k == 0 :
    print("0")
else :
    print("1")
    
