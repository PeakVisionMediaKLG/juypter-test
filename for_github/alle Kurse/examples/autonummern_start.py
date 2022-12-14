# -*- coding: utf-8 -*-
"""
Lesen Sie die Dateien "autonummern1.txt"
bis "autonummern5.txt" ein, die von fünf verschiedenen
Beobachtungsposten gemachte Aufzeichnungen von
Autokennzeichen enthalten (daneben auch weiteren Text)

Speichern Sie die enthaltenen Autonummern mit
Hilfe eines regulären Ausdrucks

r"\b[A-Z]{1,3} [A-Z]{1,2} [0-9]{2,4}\b"

in einem dict "observations" (Schlüssel: 
Beobachtungspunkt "autonummern1" - "autonummern5",
Werte: set aller beobachteten Autonummern

Versorgen Sie die dicts "numbers_observed_by" und
"count_numbers_observed_by" mit den Schlüsseln: Autonummer
und den Werten: Liste der Nummern der Beobachtungspunkte (1-5), 
wo die entsprechende Nummer gesichtet wurde sowie der Anzahl
alller Sichtungen

@author: stephan
"""
import re

observations={}
for i in range(1,6):
    fbasename = "autonummern" + str(i)
    fname = r"..\texts\\" + fbasename + ".txt"
    print(fname) 
    fh = open(fname)
    txt = fh.read()
# your code here
		print("observations[%s]: " % fbasename, observations[fbasename])
    fh.close()

all_num = set()
#print(len(all_num))
for k in observations:
# your code here

print(all_num)


numbers_observed_by = {}
count_numbers_observed_by = {}
for num in all_num:
    for k in observations: 
# your code here



       