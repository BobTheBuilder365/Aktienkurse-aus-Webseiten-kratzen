from urllib.request import urlopen

# suche den aktuellen WErt einer Reihe von Aktien.
# BASF, Daimler, Fresenius, SAP
# Finde zuerst die WKN
#
WKN = { "Bayer" : "BAY001",
        "Daimler" : "710000",
        "BASF" : "BASF11",
        "SAP" : "716460"
      }

x = "Bayer"
url = "http://www.finanzen.net/aktien/"+x+"-Aktie"
htmltext = urlopen(url)
for x in range(10):
    text = htmltext.readline().decode("utf-8")
    print(text)
    
print()