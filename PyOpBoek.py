


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
        volledig = str(boeknr) + "  -  " + titel + "  -  " + auteur + "  -  " + uitgever + "  -  " + isbn + "\n"
        with open("boek_tabletext", "a") as f:
            f.write(volledig)
    else:
        print("Karakters zij over maximaal opnieuw")
    return print("Het is gelukt")


print(boek_tabel())

