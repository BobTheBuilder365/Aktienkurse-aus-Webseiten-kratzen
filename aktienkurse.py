# Aktienwerte

from urllib.request import urlopen   # Internet Seiten lesen
import re                            # Reguläre Ausdrücke
import datetime                      # Datum


# ein dictionary mit meinen Aktien

heute = datetime.date.today()
print("\nMein Aktienbestand am " + str(heute.day) + '.' + str(heute.month) +'.'+str(heute.year)+"\n")

# Anzahl Aktien müssen  manuell angepasst werden:
meineAktien = {'Daimler':200,'BASF':10,'Siemens':10,'SAP':15, 'Fresenius':30, 'Volkswagen':10}

# Basisseite:
webseite = "http://www.finanzen.net/aktien/"

# Muster für einen Kurswert, (z.B. 546,78 EUR) der direkt auf den Text 
# 'Kurs</td><td class="textRight" colspan="2">' folgt:

# Neu : äusserest HTML Element : <div class="col-xs-5 col-sm-4 text-sm-right text-nowrap">52,21<span>EUR</span></div>
# Neu : inneres HTML Element 52,21<span>EUR</span>
beginn = 'Kurs</td><td class="textRight" colspan="2">'
pattern = re.compile('(?<='+beginn+')([0-9]+\,[0-9]{1,2}) EUR')

depotwert = 0

for aktie in meineAktien:
    xml = urlopen(webseite + aktie + '-Aktie')
    for bline in xml:
        findVal = re.findall(pattern,str(bline))
        
        if findVal != []:                           # z.B.  ['546,78 EUR']
            preis       = findVal[0].split()[0]     #       ['546,78']
            euro,cent   = preis.split(',')          #       ['546','78']
            kurs        = int(euro)+int(cent)/100.0 #   546.78
            wert        = kurs*meineAktien[aktie]

            print("%10s \t %8.2f \t%10.2f" %(aktie,kurs,wert))

            depotwert  += wert
            
print("\t\t\t\t-----------")
print("\tGesamtwert des Depots  : ","%7.2f Euro"%depotwert)
            
