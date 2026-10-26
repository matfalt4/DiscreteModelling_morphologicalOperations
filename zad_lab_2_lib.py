import numpy as np


##########################################################################################

def dylatacja(obraz, promien_s=0):

    po_dylatacji = np.zeros_like(obraz)
    promien_sasiedztwa = 0

    if promien_s==0:
        promien_sasiedztwa = int(input("Podaj wymiar promienia sasiedztwa: "))
    else:
        promien_sasiedztwa = promien_s

    obraz_padded = np.pad(obraz, promien_sasiedztwa, mode="constant", constant_values=0)

    for x in range(obraz.shape[0]):
        for y in range(obraz.shape[1]):

            sasiedztwo = obraz_padded[x:x+2*promien_sasiedztwa+1,
                                      y:y+2*promien_sasiedztwa+1]

            po_dylatacji[x,y] = np.max(sasiedztwo)

    return po_dylatacji

##########################################################################################

def erozja(obraz, promien_s=0):

    po_erozji = np.zeros_like(obraz)
    promien_sasiedztwa = 0

    if promien_s == 0:
        promien_sasiedztwa = int(input("Podaj rozmiar promienia sasiedztwa: "))
    else:
        promien_sasiedztwa = promien_s

    obraz_padded = np.pad(obraz, promien_sasiedztwa, mode="constant", constant_values=0)

    for x in range(obraz.shape[0]):
        for y in range(obraz.shape[1]):

            sasiedztwo = obraz_padded[x:x+2*promien_sasiedztwa+1,
                                      y:y+2*promien_sasiedztwa+1]

            po_erozji[x,y] = np.min(sasiedztwo)

    return po_erozji

##########################################################################################

def otwarcie_morf(obraz, promien_s=0):

    promien_sasiedztwa = 0

    if promien_s==0:
        promien_sasiedztwa = int(input("Podaj promien sasiedztwa: "))
    else:
        promien_sasiedztwa = promien_s

    obraz_po_erozji = erozja(obraz, promien_sasiedztwa)
    obraz_po_dylatacji = dylatacja(obraz_po_erozji, promien_sasiedztwa)

    return obraz_po_dylatacji

##########################################################################################

def domkniecie_morf(obraz, promien_s=0):

    promien_sasiedztwa = 0

    if promien_s == 0:
        promien_sasiedztwa = int(input("Podaj promien sasiedztwa: "))
    else:
        promien_sasiedztwa = promien_s

    obraz_po_dylatacji = dylatacja(obraz, promien_sasiedztwa)
    obraz_po_erozji = erozja(obraz_po_dylatacji, promien_sasiedztwa)

    return obraz_po_erozji

##########################################################################################

def splot(obraz, maska, promien_s=0):

    promien_sasiedztwa = 0
    wynik = np.zeros_like(obraz, dtype=float)

    if promien_s==0:
        promien_sasiedztwa = int(input("Podaj promien sasiedztwa: "))
    else:
        promien_sasiedztwa = promien_s

    obraz_padded = np.pad(obraz,
                          promien_sasiedztwa,
                          mode="constant",
                          constant_values=0)

    for x in range(obraz.shape[0]):
        for y in range(obraz.shape[1]):

            sasiedztwo = obraz_padded[x:x+2*promien_sasiedztwa+1,
                                      y:y+2*promien_sasiedztwa+1]

            wynik[x,y] = np.sum(sasiedztwo*maska)

    return wynik

##########################################################################################
