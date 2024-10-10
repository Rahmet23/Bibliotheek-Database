def reservering():
    leerlingnr = input("Wat is het leerlingnummer ")
    boeknr = input("Wat is het leerlingnummer ")
    reserveringsdatum = input("Wat is het datum van reservering ")
    volledig = leerlingnr + "  -  " + boeknr + "  -  " + reserveringsdatum

    with open("reservering_tabletext", "a") as f:
        f.write(volledig)
    return print("Het is gelukt")

print(reservering())