# fonctions_moyenne.py
# -*-coding:Utf-8 -*-
import decimal as d
from decimal import *


def translate(point, vector):
    """part des coordonnées d'un point et lui ajoute les coordonnées
    du vecteur"""
    nvo_point = []
    j = 0
    point = [d.Decimal(str(i)) for i in point]
    try:
        assert type(point[0]) == type(vector[0])
        while j < 3:
            nvo_point.append(float(point[j]+vector[j]))
            j += 1
        return(nvo_point)
    except:
        print("coordonnees des donnees d'entree pas de meme type")


def gradient(point_debut, point_fin, nombre_pas):
    """ donne le gradient entre deux points, avec un espacement constant
    pour chaque coordonnées"""
    try:
        assert len(point_debut) == len(point_fin)
        assert nombre_pas != 0
        point_debut = [d.Decimal(str(i)) for i in point_debut]
        point_fin = [d.Decimal(str(i)) for i in point_fin]
        nombre_pas = int(nombre_pas)
        i = 0
        gradient = []
        while i < len(point_debut):
            gradient.append(d.Decimal(
                str((point_fin[i]-point_debut[i])/nombre_pas)))
            i += 1
        return(gradient)
    except:
        print("les points doivent avoir même dimension et nombre_pas non nul")


def liste_points_barre(point_debut, point_fin, nombre_pas, compris=True):
    """ retourne une liste de points le long d'une coupe, pour les points
    situés entre point début et point fin, ces derniers étant ou pas
    pris en compte selon la valeur du bouléen"""
    point = [float(i) for i in point_debut]
    if compris is True:
        liste = [point]
        i = 0
        while i < nombre_pas:
            # on commance non pas au point du début, mais au 2e point
            # (on translate, pour eviter les effets de bord)
            point = translate(point,
                              gradient(point_debut, point_fin, nombre_pas))
            liste.append(point)
            i += 1
        return(liste)
    else:
        liste = []
        i = 0
        while i < nombre_pas-1:
            # on commance non pas au point du début, mais au 2e point
            # (on translate, pour eviter les effets de bord)
            point = translate(point,
                              gradient(point_debut, point_fin, nombre_pas))
            liste.append(point)
            i += 1
        return(liste)

    # a=liste_points_barres([1,1,1],[2,2,2],10)


def points_du_carre(point, espacement_carre):
    """ retourne une liste de  8 points (eux-même étants une liste de
    3 flottants) situés sur les sommet d'un carré de côté espacement et
    centrés sur point"""
    liste_points = []
    point = [d.Decimal(str(i)) for i in point]
    delta = d.Decimal(str(espacement_carre/2))

    liste_points.append(translate(point, [delta, delta, delta]))
    liste_points.append(translate(point, [delta, delta, -1*delta]))
    liste_points.append(translate(point, [-1*delta, delta, delta]))
    liste_points.append(translate(point, [-1*delta, -1*delta, delta]))
    liste_points.append(translate(point, [delta, -1*delta, delta]))
    liste_points.append(translate(point, [-1*delta, -1*delta, -1*delta]))
    liste_points.append(translate(point, [-1*delta, delta, -1*delta]))
    liste_points.append(translate(point, [delta, -1*delta, -1*delta]))
    return(liste_points)


def point_avant_et_apres(point, espacement, direction):
    """ retourne une liste de 2 points (eux-même étants une liste de 3
    flottants) espacés de espacement, et dans la direction
    num_direction (X=1, Y=2, Z=3).
    ATTENTION: l'ordre des points est important pour après avoir
    le signe correct de la différerence des N de chaque points"""

    liste_points = []
    point = [d.Decimal(str(i)) for i in point]
    delta = d.Decimal(str(espacement/2))
    zero = d.Decimal(str(0))
    if direction == 1:
        liste_points.append(translate(point, [delta, zero, zero]))
        liste_points.append(translate(point, [-1*delta, zero, zero]))
    elif direction == 2:
        liste_points.append(translate(point, [zero, delta, zero]))
        liste_points.append(translate(point, [zero, -1*delta, zero]))
    elif direction == 3:
        liste_points.append(translate(point, [zero, zero, delta]))
        liste_points.append(translate(point, [zero, zero, -1*delta]))
    else:
        print("direction mauvaise")
    return(liste_points)

    # point_avant_et_apres([1,1,1],0.1,1)


def moyenne_contraintes(fichier, nombre_points=8):
    """ lit les contraintes dans un fichier, par pas de temps
    et les sort dans une table en en faisant la moyenne"""
    import re

    # charge le fichier a lire
    with open(fichier, "r") as entree:
        fichier_en_memoire = entree.readlines()
        # lit les lignes du fichier
        i = 0
        lignes_moyennes = []
        while i < len(fichier_en_memoire)//nombre_points:
            j = 0
            valeurs_contraintes = []
            while j < int(nombre_points):
                ligne = re.sub(r'[ \t\r\f\v]+', ";",
                               fichier_en_memoire[nombre_points*i+j])
                valeurs_contraintes.append(float(ligne.split(";")[5]))
                j += 1

            # fait la moyenne de chaque capteur pour chaque pas de temps
            valeurs_contraintes = [d.Decimal(str(contrainte))
                                   for contrainte in valeurs_contraintes]
            lignes_moyennes.append(float(
                sum(valeurs_contraintes) /
                d.Decimal(str(len(valeurs_contraintes)))))
            i += 1
    return lignes_moyennes

    # print(moyenne_contraintes("res_M1_szz", 8))


def difference_contraintes(fichier):
    """ lit deux contraintes dans un fichier, par pas de temps
    et les sort en faisant la difference"""
    import re

    # charge le fichier a lire
    with open(fichier, "r") as entree:
        fichier_en_memoire = entree.readlines()
        # lit les lignes du fichier
        i = 0
        lignes_moyennes = []
        while i < len(fichier_en_memoire)//2:
            j = 0
            valeurs_contraintes = []
            while j < 2:
                ligne = re.sub(r'[ \t\r\f\v]+', ";", fichier_en_memoire[2*i+j])
                valeurs_contraintes.append(float(ligne.split(";")[5]))
                j += 1
            # fait la moyenne de chaque capteur pour chaque pas de temps
            valeurs_contraintes = [d.Decimal(str(contrainte))
                                   for contrainte in valeurs_contraintes]
            lignes_moyennes.append(float(
                valeurs_contraintes[0]-valeurs_contraintes[1]))
            i += 1
    return lignes_moyennes

    # print(difference_contraintes("res_M1_N"))
