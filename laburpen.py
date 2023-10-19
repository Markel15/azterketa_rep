import hashlib
import os

def aurkitu(fitxategi):
    with open(fitxategi, "rb") as f:
        info = f.read()
        kode = hashlib.new("md5")
        kode.update(info)
        return kode.hexdigest()

ruta = input("Idatzi analizatuko den fitxategiaren path-a: ")
bilatutako_hash = input("Idatzi bilatu nahi den hash balioa: ")

fitx_lista = os.listdir(ruta)
aurk = False
ind = 0

while aurk == False and ind < len(fitx_lista):
    fitx = fitx_lista[ind]
    fitx = ruta + os.sep + fitx
    if os.path.isfile(fitx):
        hashbalioa = aurkitu(fitx)
        if(hashbalioa == bilatutako_hash):
            aurk = True
            print("Hash balioa duen fitxategia honako hau da: " + fitx)
    ind += 1

if aurk == False:
    print("Ez da aurkitu hash hori duen fitxategirik.")
