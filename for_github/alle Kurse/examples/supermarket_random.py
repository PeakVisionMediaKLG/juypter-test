import random

#supermarket = { "Mehl":{"anzahl":10, "preis":3.49},  
#                "Brot":{"anzahl":20, "preis":2.79},
#                "Käse":{"anzahl":8, "preis":1.89}}


moegliche_artikel = ["Mehl", "Butter", "Käse", "Brot", "Wurst", "Honig", "Salat"]

supermarket = {}
for artikel in moegliche_artikel:
    anzahl_fuer_artikel = random.randint(1, 10)
    preis = round(random.random()*100, 2)
    supermarket[artikel] = {"anzahl":anzahl_fuer_artikel,
                            "preis":preis}

print(supermarket)

anzahl_auswahl = random.randint(3, len(moegliche_artikel))

ausgewaehlte_artikel = random.sample(moegliche_artikel, anzahl_auswahl) 

#print("Ausgewählte Artikel: ", ausgewaehlte_artikel)

einkaufsliste = []
for artikelname in ausgewaehlte_artikel:
    anzahl_fuer_artikel = random.randint(1, 10)
    einkaufsliste.append( (artikelname, anzahl_fuer_artikel))

print(einkaufsliste)
#einkaufsliste = [ ("Mehl", 4), 
#                  ("Wurst", 3), 
#                  ("Käse", 12)]


einkaufswagen = []
for name, anzahl in einkaufsliste:
    #print(anzahl, name)
    if name in supermarket:
        if supermarket[name]["anzahl"] < anzahl:
            anzahl = supermarket[name]["anzahl"]
        supermarket[name]["anzahl"] -= anzahl
        einkaufswagen.append((name, anzahl))
    else:
        print("warning: " + name + " leider nicht im Sortiment!")

# checkout

total = 0
for name, anzahl in einkaufswagen:
    preis = supermarket[name]["preis"]
    total += anzahl * preis
    #print(f"{anzahl:3d} {name:10s} {preis:8.2f} {preis*anzahl:8.2f}")
    print("{anzahl:3d} {name:10s} {preis:8.2f} {subtotal:8.2f}".format(anzahl=anzahl, name=name, preis=preis, subtotal=preis*anzahl))

print("Gesamtsumme: " + str(total))
print("Vielen Dank für Ihren Einkauf!")



