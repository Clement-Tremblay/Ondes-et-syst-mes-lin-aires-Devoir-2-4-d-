Ce programme produit un graphique de l'amplitude de l'onde reçue par le détecteur. L'axe est un pourcentage de l'amplitude maximale (ie le max sur les y = amplitude max) et l'axe des x donne le nombre d'intervalles de temps (j'étais trop paresseux pour mettre le nombre de périodes).
Le programme prend une centaine de vitesses entre -sigma\*v_0 + v_0 et sigma\*v_0 + v_0, trouve la fréquence pour chacune d'entre elles et fait la somme de cos(wt) pour plusieurs intervalles de temps.
Finalement, le programme produit un graphique à l'aide de matplotlib
