import numpy as np
import matplotlib.pyplot as mpl


fréquence_initiale = 5000000     # 5 MHz
vitesse_initiale = 0.5      # 0,5 m/s
vitesse_son = 1500      # m/s
dispersion = np.linspace(0.01, 0.5, 50)     # dispersion des viteses en pourcentage
temps = np.linspace(2 * np.pi, 100 * np.pi, 100000)   # 100 temps entre 0 et 20 s

champ_des_vitesses = np.linspace(-1, 1, 100) * vitesse_initiale   # 100 valeurs entre -v et v, à multiplier avec la dispersion en %


champ_des_vitesses *= 0.4   # disperion de la vitesse
champ_des_vitesses += vitesse_initiale     # 100 vitesses entre -sigma et sigma
champ_des__delta_fréquences = champ_des_vitesses * ((2/vitesse_son)*fréquence_initiale)     # delta w pour les différentes vitesses
champ_des_fréquences = champ_des__delta_fréquences + (np.ones((1,100)) * fréquence_initiale)    # w pour les différentes vitesses

liste_abs = []
liste = []
for moment in temps:
    champ_des_fréquences_backup = np.copy(champ_des_fréquences)
    champ_des_fréquences *= moment
    champ_des_fréquences = np.cos(champ_des_fréquences)
    somme = np.sum(champ_des_fréquences)
    liste_abs.append(abs(somme))
    liste.append(somme)
    champ_des_fréquences = champ_des_fréquences_backup

print(max(liste))

mpl.plot(liste)
mpl.show()
