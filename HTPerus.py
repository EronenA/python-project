######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Aki Eronen
# Opiskelijanumero: 614554
# Päivämäärä: 15.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTPerus.py

import HTPerusKirjasto

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("4) Analysoi viikonpäivittäiset keskiarvot")
    print("0) Lopeta")
    Syote = int(input("Anna valintasi: "))
    return Syote

def paaohjelma():
    Rivit = []
    TilastoTiedot = None
    PvmTiedot = []
    Tulosteet = []
    while (True):
        Valinta = valikko()
        if (Valinta == 1):
            LueTiedosto = HTPerusKirjasto.kysyNimi("Anna luettavan tiedoston nimi: ")
            Rivit = HTPerusKirjasto.tiedostoLue(LueTiedosto, Rivit)
            print()
        elif (Valinta == 2):
            if (len(Rivit) == 0):
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                TilastoTiedot = HTPerusKirjasto.analysoiHinta(Rivit)
                PvmTiedot = HTPerusKirjasto.analysoiPvm(Rivit, PvmTiedot)
                Tulosteet = HTPerusKirjasto.muotoile(TilastoTiedot, PvmTiedot, Tulosteet)
            print()
        elif (Valinta == 3):
            if (len(Tulosteet) == 0):
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")
            else:
                KirjoitaTiedosto = HTPerusKirjasto.kysyNimi("Anna kirjoitettavan tiedoston nimi: ")
                HTPerusKirjasto.tiedostoKirjoita(KirjoitaTiedosto, Tulosteet)
            print()
        elif (Valinta == 4):
            if (len(Rivit) == 0):
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                KirjoitaTiedosto = HTPerusKirjasto.kysyNimi("Anna kirjoitettavan tiedoston nimi: ")
                Tulosteet = HTPerusKirjasto.analysoiViikonpv(Rivit, Tulosteet)
                HTPerusKirjasto.tiedostoKirjoita(KirjoitaTiedosto, Tulosteet)
            print()
        elif (Valinta == 0):
            print("Lopetetaan.")
            PvmTiedot.clear()
            Rivit.clear()
            Tulosteet.clear()
            print()
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()


######################################################################
# eof
