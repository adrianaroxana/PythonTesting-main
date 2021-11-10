'''
# mostenire -> Proprietate prin care o clasa poate sa reutilizeze material din alta clasa

#Encapsulare -> modalitate prin care putem sa atribuim un anumit nivel de acces unor variabile sau metode
# niveluri de acces:
# - public -> Sunt vizibile de oriunde din program
# - private (__)-> Se pot folosi doar in interiorul clasei curente
# - protected  (_)-> Se pot folosi doar in aceeasi clasa sau si in clasa copil

#Abstractizare -> modalitate prin care putem sa creem anumite template-uri pentru alte clase.
# Adica daca vrem sa definim o clasa test case cu metoda setup sau execute,
# atunci toate clasele care vor extinde modelul asta vor fi obligate sa aiba mapate metodele respective
# Un alt avantaj e faptul ca avem suficient de bine documentata folosirea altor clase


# Polimorfism -> Se refera la o abilitate prin care un obiect poate avea mai multe forme.
# Ex: avem o metoda calculateArea, prin care se poate calcula diferit aria pentru un triunghi, patrat etc.
# Am folosit polimorfismul deja in functia print (unde putem sa punem atat numere cat si stringuri, boolean sau alt tip de data)
'''


# print("mesaj")
# print(7)
# print(7,3,5)
# print(7,3,5,sep = ":", end = "*")
# print(7,3,5,sep = ":", end = "*")
# print("........................")
# a = ["masina", 10, "avion", True, 15]
# b = "complex"
#
# print(len(a))
# print(len(b))


# we use addition to calculate the sum if the variables are numbers or concatenate if the variables are strings

def addition(a, b, c=0, dataType='str'):

    if dataType == 'float':
        return float(a) + float(b) + float(c)
    elif dataType == 'int':
        return int(a) + int(b) + int(c)
    else:
        return a + b + c


a = input("Enter first element: ")
b = input("Enter second element: ")
c = input("Enter third element: ")

print(addition(a, b, c, 'int'))
# print(addition(a,b))
# print(addition(a,b,c,'float'))
