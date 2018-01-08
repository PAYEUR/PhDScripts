#controller_cesar.py
# -*-coding:Utf-8 -*-
import sys
sys.path.append("/home/PAYEUR/fonctions+programmes")

import fonctions_cesar as f_c
nom_executable_cesar="CESAR-avr2015.exe"
nom_etude="kbsc"
noms_modeles=["M32", "M33", "M34"]


for nom_modele in noms_modeles:
    f_c.run_cesar(nom_executable_cesar, nom_etude, nom_modele)

#import fonctions_resupov4 as f_r
#nom_executable_resupo="resupov4.exe"
#liste_numero_grandeurs=[1, 2, 3, 11, 12, 13]
#liste_points=[[10, 1, 2], [10, 4, 2]]
#pdt_min=1
#pdt_max=1
#f_r.run_resupov4(nom_executable_resupo, nom_etude, nom_modele, liste_numero_grandeurs, liste_points, pdt_min, pdt_max, unique=True)
