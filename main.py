import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

from zad_lab_2_lib import dylatacja, erozja, otwarcie_morf, domkniecie_morf, splot

obraz = Image.open("/Users/mateuszfaltyn/Desktop/studia/ModDysk/lab_02/Screenshot 2026-10-25 at 12.16.51.png").convert("L")
obraz = np.array(obraz, dtype=np.uint8)

r = 100

kernel = np.ones((2*r+1, 2*r+1))/(2*r+1)**2

wyniki = [
    ("Oryginal", obraz),
    ("Dylatacja", dylatacja(obraz,r)),
    ("Erozja", erozja(obraz,r)),
    ("Otwarcie", otwarcie_morf(obraz,r)),
    ("Domkniecie", domkniecie_morf(obraz,r)),
    ("Splot", splot(obraz, kernel, r))
]

plt.figure(figsize = (12,8))

for i, (nazwa,wynik) in enumerate(wyniki):
    plt.subplot(2,3,i+1)
    plt.imshow(wynik, cmap="gray", vmin=0, vmax=255)
    plt.title(nazwa)

plt.tight_layout()
plt.show()
