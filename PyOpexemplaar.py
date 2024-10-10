def exemplaar():
    exemplaarnr = input("Wat is het exemplaarnummer ")
    boeknr = input("Wat is het boeknummer ")
    volledig = exemplaarnr + "  -  " + boeknr
    with open("exemplaar_tabletext", "a") as f:
        f.write(volledig)
    return print("Het is gelukt")

print(exemplaar())