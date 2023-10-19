from collections import Counter
import os

aztertzeko_testua =  input("Idatzi analizatuko den testua: ")
hutsune_testua = ""
prosz_testua = ""
luzera_testua = 0

for c in aztertzeko_testua:
    if c == " " or c == "." or c == ",":
        hutsune_testua = hutsune_testua + c
    elif c.isdigit():
        hutsune_testua = hutsune_testua + c
    else:
        hutsune_testua = hutsune_testua + "_"
        prosz_testua = prosz_testua + c
        luzera_testua = luzera_testua + 1


def inprimatu():
    print("Testuaren karaktere kopurua: ", luzera_testua)
    letters = Counter(prosz_testua)
    print(letters)
    print("\n")
    print(hutsune_testua)
    print("\n")
    print(aztertzeko_testua)
    print("\n")


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def ordezkatu(a, b):
    mut_hutsune_testua = list(hutsune_testua)

    for i, char in enumerate(aztertzeko_testua):
        if char == a:
            mut_hutsune_testua[i] = b
    
    berria = ''.join(mut_hutsune_testua)
    return berria

jarraitu = True
inprimatu()
while jarraitu == True:
    a = input("Ordezkatzeko letra: ")
    b = input("Zeren ordez? ")
    if a == "exit" or b == "exit":
        jarraitu = False
    elif len(a) == 1 and len(b) == 1 and a.isalpha() and b.isalpha():
        hutsune_testua = ordezkatu(a, b)
        clear()
        inprimatu()
