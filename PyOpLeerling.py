def leerling():
    naam = input("Wat is de naam van de leerling ")
    leerlingnr = input("leerlingnr ")
    adres = input("adres leerling ")
    woonplaats = input("woonplaats leerling ")
    if len(naam) < 255:
        naam = naam
    if len(adres) < 255:
        adres = adres
    if len(woonplaats) < 255:
        woonplaats = woonplaats
        volledig = leerlingnr + "  -  " + naam + "  -  " + adres + "  -  " + woonplaats
        with open("leerling_tabletext", "a") as f:
            f.write(volledig)
    else:
        print("karakters zijn te groot begin opnieuw")
    return print("Het is gelukt")

print(leerling())