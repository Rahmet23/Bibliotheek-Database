import datetime

def uitlening():
    uitleningnr = input("Wat is het uitlenernummer ")
    leerlingnr = input("Wat is het leerlingnummer ")
    exemplaarnr = input("Wat is het exemplaarnummer ")
    begindatum = str(datetime.date.today())
    einddatum = str(datetime.date.today() + datetime.timedelta(+14))
    volledig = uitleningnr + "  -  " + leerlingnr + "  -  " + exemplaarnr + "  -  " + begindatum + "  -  " + einddatum
    with open("uitlening_tabletext", "a") as f:
        f.write(volledig)
    return print("Het is gelukt")

print(uitlening())