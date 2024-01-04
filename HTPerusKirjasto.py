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
# Tehtävä HTPerusKirjasto.py

import datetime

import sys

class TIEDOT:
    Pvm = None
    Hinta = None

class HINTATIEDOT:
    Lkm = None
    Keskiarvo = None
    Kallein = None
    PvmKallein = None
    Halvin = None
    PvmHalvin = None

def kysyNimi(Kehote):
    Nimi = input(Kehote)
    return Nimi

def tiedostoLue(Nimi, RiviLista):
    RiviLista.clear()
    try:
        Tiedosto = open(Nimi, "r", encoding="UTF-8")
        Rivi = Tiedosto.readline()
        Rivi = Tiedosto.readline()
        while (len(Rivi) > 0):
            Tiedot = TIEDOT()
            Rivi = Rivi[:-1]
            Alkio = Rivi.split(';')
            Tiedot.Pvm = Alkio[0]
            Tiedot.Hinta = float(Alkio[1])
            RiviLista.append(Tiedot)
            Rivi = Tiedosto.readline()
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Tiedosto '" + Nimi + "' luettu.")
    return RiviLista

def analysoiHinta(RiviLista):
    HintaTiedot = HINTATIEDOT()
    Summa = 0
    for Alkio in RiviLista:
        if (HintaTiedot.Halvin == None) or (Alkio.Hinta < HintaTiedot.Halvin):
            HintaTiedot.Halvin = Alkio.Hinta
            Paiva = datetime.datetime.strptime(Alkio.Pvm, '"%Y-%m-%d %H:%M:%S"')
            HintaTiedot.PvmHalvin = datetime.datetime.strftime(Paiva, "%d.%m.%Y %H:%M")
        if (HintaTiedot.Kallein == None) or (Alkio.Hinta > HintaTiedot.Kallein):
            HintaTiedot.Kallein = Alkio.Hinta
            Paiva = datetime.datetime.strptime(Alkio.Pvm, '"%Y-%m-%d %H:%M:%S"')
            HintaTiedot.PvmKallein = datetime.datetime.strftime(Paiva, "%d.%m.%Y %H:%M")
        if (HintaTiedot.Lkm == None):
            HintaTiedot.Lkm = 0
        HintaTiedot.Lkm = HintaTiedot.Lkm + 1
        Summa = Summa + Alkio.Hinta
    HintaTiedot.Keskiarvo = Summa / HintaTiedot.Lkm
    print("Tilastotietojen analyysi suoritettu", HintaTiedot.Lkm, "alkiolle.")
    return HintaTiedot

def analysoiPvm(RiviLista, PvmLista):
    PvmLista.clear()
    Summa = 0
    Lkm = 0
    PvmEdellinen = datetime.datetime.strptime(RiviLista[0].Pvm, '"%Y-%m-%d %H:%M:%S"')
    PaivamaaraEdellinen = datetime.datetime.strftime(PvmEdellinen, "%d.%m.%Y")
    PaivaEdellinen = datetime.datetime.strftime(PvmEdellinen, "%d")
    for Alkio in RiviLista:
        PvmNyt = datetime.datetime.strptime(Alkio.Pvm, '"%Y-%m-%d %H:%M:%S"')
        PaivamaaraNyt = datetime.datetime.strftime(PvmNyt, "%d.%m.%Y")
        Paiva = datetime.datetime.strftime(PvmNyt, "%d")
        Data = Alkio.Hinta
        if (Paiva == PaivaEdellinen):
            Summa = Summa + Data
            Lkm = Lkm + 1
        else:
            Tiedot = TIEDOT()
            Tiedot.Pvm = PaivamaaraEdellinen
            Tiedot.Hinta = Summa / Lkm
            PvmLista.append(Tiedot)
            PaivaEdellinen = Paiva
            PaivamaaraEdellinen = PaivamaaraNyt
            Summa = Data
            Lkm = 1
    Tiedot = TIEDOT()
    Tiedot.Pvm = PaivamaaraEdellinen
    Tiedot.Hinta = Summa / Lkm
    PvmLista.append(Tiedot)
    print("Päivittäiset keskiarvot laskettu", len(PvmLista), "päivälle.")
    return PvmLista

def muotoile(TilastoTiedot, PvmTiedot, Tuloste):
    Tuloste.clear()
    Tuloste.append("Analyysin tulokset " + str(TilastoTiedot.Lkm) + " tunnilta ovat seuraavat:")
    Tuloste.append("Sähkön keskihinta oli " + str(round(TilastoTiedot.Keskiarvo,1)) + " snt/kWh.")
    Tuloste.append("Halvimmillaan sähkö oli " + str(TilastoTiedot.Halvin) + " snt/kWh, " + TilastoTiedot.PvmHalvin + ".")
    Tuloste.append("Kalleimmillaan sähkö oli " + str(TilastoTiedot.Kallein) + " snt/kWh, " + TilastoTiedot.PvmKallein + ".")
    Tuloste.append("\n" + "Päivittäiset keskiarvot (Pvm;snt/kWh):")
    for Alkio in PvmTiedot:
        Tuloste.append("{0:s};{1:.1f}".format(Alkio.Pvm, Alkio.Hinta))
    return Tuloste

def tiedostoKirjoita(Nimi, TulosteLista):
    try:
        Tiedosto = open(Nimi, "w", encoding="UTF-8")
        for i in range(len(TulosteLista)):
            Tiedosto.write(TulosteLista[i] + '\n')
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Tiedosto '" + Nimi + "' kirjoitettu.")
    return None

def analysoiViikonpv(RiviLista, Tuloste):
    Tuloste.clear()
    Lkm = [0, 0, 0, 0, 0, 0, 0]
    Summa = [0, 0, 0, 0, 0, 0, 0]
    Paivat = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]
    for Alkio in RiviLista:
        Pvm = datetime.datetime.strptime(Alkio.Pvm, '"%Y-%m-%d %H:%M:%S"')
        Paiva = datetime.datetime.strftime(Pvm, "%a")
        if (Paiva == "Mon"):
            Lkm[0] = Lkm[0] + 1
            Summa[0] = Summa[0] + Alkio.Hinta
        elif (Paiva == "Tue"):
            Lkm[1] = Lkm[1] + 1
            Summa[1] = Summa[1] + Alkio.Hinta
        elif (Paiva == "Wed"):
            Lkm[2] = Lkm[2] + 1
            Summa[2] = Summa[2] + Alkio.Hinta
        elif (Paiva == "Thu"):
            Lkm[3] = Lkm[3] + 1
            Summa[3] = Summa[3] + Alkio.Hinta
        elif (Paiva == "Fri"):
            Lkm[4] = Lkm[4] + 1
            Summa[4] = Summa[4] + Alkio.Hinta
        elif (Paiva == "Sat"):
            Lkm[5] = Lkm[5] + 1
            Summa[5] = Summa[5] + Alkio.Hinta
        elif (Paiva == "Sun"):
            Lkm[6] = Lkm[6] + 1
            Summa[6] = Summa[6] + Alkio.Hinta
    Tuloste.append("Viikonpäivä;Keskimääräinen hinta snt/kWh")
    for i in range(7):
        if (Lkm[i] == 0):
            Lkm[i] = 1
        Tuloste.append(Paivat[i] + ";" + str(round((Summa[i] / Lkm[i]),1)))
    Lkm.clear()
    Summa.clear()
    Paivat.clear()
    return Tuloste


######################################################################
# eof
