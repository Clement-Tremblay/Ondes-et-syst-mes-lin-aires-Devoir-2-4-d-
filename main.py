import numpy as np
import matplotlib.pyplot as mpl


fréquence_initiale = 2000000     # Hz
vitesse_initiale = 0.5      # m/s
vitesse_son = 1500      # m/s, selon le numéro
temps = np.linspace(0, 1000 * np.pi, 536874)   # plusieurs (we do a little trolling) intervalles de temps entre 0 et x * pi

champ_des_vitesses = np.linspace(-1, 1, 100) * vitesse_initiale   # 100 valeurs entre -v et v, à multiplier avec la dispersion en %


champ_des_vitesses *= 1   # dispersion de la vitesse
champ_des_vitesses += vitesse_initiale     # 100 vitesses entre -sigma et sigma
champ_des__delta_fréquences = champ_des_vitesses * ((2/vitesse_son)*fréquence_initiale)     # delta w pour les différentes vitesses
champ_des_fréquences = champ_des__delta_fréquences + (np.ones((1,100)) * fréquence_initiale)    # w pour les différentes vitesses

liste = []  # création d'une liste vide
for moment in temps:
    champ_des_fréquences_backup = np.copy(champ_des_fréquences)
    champ_des_fréquences *= moment  # w * t
    champ_des_fréquences = np.cos(champ_des_fréquences)     # cos(wt)
    somme = np.sum(champ_des_fréquences)    # somme de toutes les fréquences (entre 0 et 100)
    liste.append(somme)
    champ_des_fréquences = champ_des_fréquences_backup

mpl.plot(liste)
mpl.show()
