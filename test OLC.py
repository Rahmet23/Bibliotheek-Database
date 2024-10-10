def OLCtest():
    id = input("Wat is het idnummer ")
    naam = input("Wat is het naam ")
    email = input("Wat is het email ")
    boek = input(("Naam van het boek "))
    auteur = input("Naam van de auteur ")
    volledig = id + " , " + naam + " , " + email + " , " + boek + " , " + auteur + "\n"
    with open("OLCtest_tabletext", "a") as f:
        f.write(str(volledig))
    return print("Het is gelukt")

print(OLCtest())

