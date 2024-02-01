import random
import os

def loe_failist(f):
    fail = open(f, 'r', encoding="utf-8-sig")
    mas = []
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def kirjuta_failisse(f, mas):
    fail = open(f, 'w', encoding="utf-8-sig")
    for element in mas:
        fail.write(element + '\n')
    fail.close()

def tõlgi(eesti, vene, tekst):
    if tekst in eesti:
        index = eesti.index(tekst)
        return f"{tekst} - {vene[index]}"
    elif tekst in vene:
        index = vene.index(tekst)
        return f"{tekst} - {eesti[index]}"
    else:
        return "Sõna ei leitud. Kas soovid seda lisada?"

def lisa_sõna(eesti, vene):
    uus_sõna = input("Sisesta uus sõna: ")
    uus_tõlge = input(f"Sisesta {uus_sõna} tõlge: ")
    eesti.append(uus_sõna)
    vene.append(uus_tõlge)
    print("Sõna on lisatud edukalt!")

def paranda_viga(eesti, vene):
    viga = input("Sisesta sõna, mille tõlget soovid parandada: ")
    if viga in eesti:
        index = eesti.index(viga)
        uus_tõlge = input(f"Õige tõlge {viga} kohta: ")
        vene[index] = uus_tõlge
        print("Viga on parandatud!")
    else:
        print("Seda sõna ei leitud.")

def kontrolli_teadmised(eesti, vene):
    õigeid = 0
    küsimusi = 10
    for _ in range(küsimusi):
        suvaline_indeks = random.randint(0, küsimusi - 1)
        küsimus = eesti[suvaline_indeks]
        õige_vastus = vene[suvaline_indeks]
        vastus = input(f"{küsimus}: ")
        if vastus == õige_vastus:
            print("Õige!")
            õigeid += 1
        else:
            print(f"Vale! Õige vastus on: {õige_vastus}")
    
    protsent = õigeid / küsimusi * 100
    print(f"Sinu tulemus: {õigeid}/{küsimusi} õiget. {protsent}%")

rus = loe_failist("rus.txt")
est = loe_failist("est.txt")

while True:
    print("\n1. Tõlgi sõna")
    print("2. Lisa sõna")
    print("3. Paranda viga")
    print("4. Kontrolli sõnavara")
    print("0. Välju")
    valik = input("Vali tegevus (0-4): ")

    if valik == "0":
        break
    elif valik == "1":
        sõna = input("Sisesta sõna, mida soovid tõlkida: ")
        print(tõlgi(est, rus, sõna))
    elif valik == "2":
        lisa_sõna(est, rus)
        kirjuta_failisse("est.txt", est)
        kirjuta_failisse("rus.txt", rus)
    elif valik == "3":
        paranda_viga(est, rus)
        kirjuta_failisse("est.txt", est)
        kirjuta_failisse("rus.txt", rus)
    elif valik == "4":
        kontrolli_teadmised(est, rus)

