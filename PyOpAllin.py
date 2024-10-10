import datetime

def boek_tabel():
    boeknr = input(str("wat is het boeknummer "))
    titel = input("Wat is het titel van het boek ").lower()
    auteur = input("Wie is het auteur van dit boek ").lower()
    uitgever = input("wie zijn de uitgevers van dit boek ").lower()
    isbn = input(str("Wat is het isbn nummer van dit boek "))
    if len(titel) < 255:
        titel = titel
    if len(auteur) < 255:
        auteur = auteur
    if len(uitgever) < 60:
        uitgever = uitgever
    if len(isbn) < 30:
        isbn = isbn
        volledig = str(boeknr) + " , " + titel + " , " + auteur + " , " + uitgever + " , " + isbn + "\n"
        with open("boek_tabletext", "a") as f:
            f.write(volledig)
    else:
        print("Karakters zij over maximaal opnieuw")
    return print("Het is gelukt")
def exemplaar():
    exemplaarnr = input("Wat is het exemplaarnummer ")
    boeknr = input("Wat is het boeknummer ")
    volledig = exemplaarnr + " , " + boeknr + "\n"
    with open("exemplaar_tabletext", "a") as f:
        f.write(volledig)
    return print("Het is gelukt")

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
        volledig = leerlingnr + " , " + naam + " , " + adres + " , " + woonplaats + "\n"
        with open("leerling_tabletext", "a") as f:
            f.write(volledig)
    else:
        print("karakters zijn te groot begin opnieuw")
    return print("Het is gelukt")

def reservering():
    leerlingnr = input("Wat is het leerlingnummer ")
    boeknr = input("Wat is het boeknr ")
    reserveringsdatum = print("Datum van de reservering is " , (datetime.date.today()))
    print(reserveringsdatum)
    datum = str(datetime.date.today())
    volledig = leerlingnr + " , " + boeknr + " , " + datum + "\n"

    with open("reservering_tabletext", "a") as f:
        f.write(volledig)
    return print("Het is gelukt")

def uitlening():
    uitleningnr = input("Wat is het uitlenernummer ")
    leerlingnr = input("Wat is het leerlingnummer ")
    exemplaarnr = input("Wat is het exemplaarnummer ")
    begindatum = str(datetime.date.today())
    einddatum = str(datetime.date.today() + datetime.timedelta(+14))
    volledig = uitleningnr + " , " + leerlingnr + " , " + exemplaarnr + " , " + begindatum + " , " + einddatum + "\n"
    with open("uitlening_tabletext", "a") as f:
        f.write(volledig)
    return print("Het is gelukt")



print(boek_tabel())
print(exemplaar())
print(leerling())
print(reservering())
print(uitlening())
