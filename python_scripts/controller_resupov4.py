# -*- coding: utf-8 -*-
"""
Created on Tue Nov 04 15:23:05 2014

@author: admin-payeur
"""
import sys
sys.path.append("/home/PAYEUR/fonctions+programmes")

import fonctions_moyenne as f_m
import fonctions_resupov4 as f_r
import re
import os

nom_executable_resupo = "resupov4.exe"
nom_etude = "kbsc"
noms_modeles = ["M19"]
Y_debut_barre = 0.05
Y_fin_barre = 5
Xs_barres = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
Zs_barres = [3.8, 3.15]

# ces deux listes exactement dans le même ordre!!
liste_numero_grandeurs = [1, 2, 3, 7, 11, 13, 4]
liste_grandeurs = ["u", "v", "w", "szz", "Fi", "Cr", "T"]


for nom_modele in noms_modeles:
    for (z, Z) in enumerate(Zs_barres):

        # premiere boucle pour faire le calcul resupov4
        for (x, X) in enumerate(Xs_barres):
            point_debut = [X, Y_debut_barre, Z]
            point_fin = [X, Y_fin_barre, Z]
            points_barre = f_m.liste_points_barre(point_debut, point_fin, 20)
            nom_fichier_sortie = nom_modele + "barre_X" + str(x) + "_Z" + str(z)

            f_r.run_resupov4(nom_executable_resupo, nom_etude, nom_modele,
                             liste_numero_grandeurs, points_barre, 1, 1,
                             nom_fichier_sortie)

        # seconde boucle pour avoir les matrices de grandeur
        for i, grandeur in enumerate(liste_grandeurs):
            indice_colonne = i+5
            matrice = []
            for (x, X) in enumerate(Xs_barres):
                nom_fichier_sortie = nom_modele + "barre_X" + str(x) + "_Z" + str(z)
                with open(nom_fichier_sortie, 'r') as entree:
                    lignes = [re.sub(r'[ \t\r\f\v]+', ";", line) for line in entree.readlines()]
                    # vire les 3 premieres lignes et garde l'entete
                    del lignes[0]
                    del lignes[1]
                    entete = lignes[0]
                    del lignes[0]
                    # cette ligne ajoute directement la colonne d'indice incice_colonne
                    matrice.append([line.split(";")[indice_colonne] for line in lignes])
                    matrice.append("\n")

            # on vide la matrice de chaque grandeur dans le fichier correspondant
            nom_fichier_grandeur = nom_modele + "_Z" + str(z) + "_" + grandeur
            with open(nom_fichier_grandeur, "w") as fichier_grandeur:
                for line in matrice:
                    fichier_grandeur.write(";".join(line))

os.system("rm *barre*")
