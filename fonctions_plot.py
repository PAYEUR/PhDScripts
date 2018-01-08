# -*-coding:Utf-8 -*-
from __future__ import unicode_literals
import matplotlib.pyplot as plt
import numpy as np
from fonctions_moyenne import liste_points_barres

def treat(data):
    """ fonction qui permet de traiter les données issues d'un fichier csv, en virant les retours à la ligne"""
    return(data[0:data.shape[0], 0:data.shape[1]-1])


def contraintes(fichier_dN_dyn, fichier_szz_dyn, fichier_dN_stat, fichier_szz_stat):
    """sort [szz_total, dN_dx_total]"""
    increment_dN_dx = treat(np.genfromtxt(fichier_dN_dyn, delimiter=";"))
    increment_szz = treat(np.genfromtxt(fichier_szz_dyn, delimiter=";"))

    # matrice (1,nombre_pdt) remplie de 1 000 000 pour avoir les mêmes unités
    uns = 1000000*np.ones((1, increment_dN_dx.shape[1]))

    # matrices (nb_points,nb_pdt) correspondant aux valeurs statiques en chacun des points, pour tout pdt, a la bonne unite
    dN_dx_statique = np.dot(treat(np.genfromtxt(fichier_dN_stat, delimiter=";")), uns)
    szz_statique = np.dot(treat(np.genfromtxt(fichier_szz_stat, delimiter=";")), uns)

    # definition des champs resultants totaux
    dN_dx_total = dN_dx_statique + increment_dN_dx
    szz_total = szz_statique + increment_szz

    return([szz_total, dN_dx_total])


def rapport_contraintes(fichier_dN_dyn, fichier_szz_dyn, fichier_dN_stat, fichier_szz_stat):
    """ donne un nuage de points correspondant au coefficient de frottement local, sous reserve de bonne dimension des fichiers d'entree"""
    liste = contraintes(fichier_dN_dyn, fichier_szz_dyn, fichier_dN_stat, fichier_szz_stat)
    return(liste[1]/liste[0])


def subplot_contour(fig, position_in_fig, data, point_debut_y, point_fin_y, nombre_pas_y, titre_subplot):
    """ fonction qui permet de definir des zones en 2D, avec leur titre"""
    ax = fig.add_subplot(position_in_fig)

    # remplissage
    ax.imshow(data, vmin=0, vmax=1, cmap=plt.cm.gray, aspect=4, origin='lower', interpolation='nearest', extent=[0, len(data[1]), point_debut_y[0], point_fin_y[0]])
    # ax.set_yticks(np.linspace(point_debut_y[0], point_fin_y[0], nombre_pas_y, endpoint=True))
    ax.set_xlabel('Incrément de temps')
    ax.set_ylabel('distance au parement (m)')
    ax.set_title(titre_subplot)


def pente_dilatance(mu_zero,tan_phi,sigma_lim):
    """ calcul de (a,b) de dilatance empechée a*mu+b = sigma, en kPa"""
    a = -sigma_lim/(mu_zero - tan_phi)
    b = -mu_zero*a
    return(a, b)


def subplot_lignes(fig,position_in_fig, data, point_debut_y, point_fin_y, nombre_pas_y, titre_subplot):
    """ fonction qui permet de definir des zones en 2D, avec leur titre"""
    ax = fig.add_subplot(position_in_fig)
    X = np.arange(0, len(data[1]), 1)
    # vecteur des points correspondants à la longueur depuis le parement
    Y = np.array([point[0] for point in liste_points_barres(point_debut_y, point_fin_y, nombre_pas_y, False)])
    ax.contour(X, Y, data, [-1, 1], colors='black', linestyles=['-', '--'])
    ax.set_xlabel('Incrément de temps')
    ax.set_ylabel('x (m)')
    ax.set_title(titre_subplot, size='large', style='italic')

def coord(point_debut_y, point_fin_y, nombre_pas_y, data):
    """ grille de base d'une surface"""
    # vecteur des abscisses
    X = np.arange(0, len(data[1]), 1)
    # vecteur des points correspondants à la longueur depuis le parement
    y = np.array([point[0] for point in liste_points_barres(point_debut_y, point_fin_y, nombre_pas_y, False)])
    return(np.meshgrid(X, y))


def legend(ax, titre_axe_z, titre_subplot, zmin, zmax, view_init_auto = True):
    """ gere les parametres de legende d'un subplot"""
    ax.set_xlabel('Incrément de temps', labelpad=25)
    ax.set_zmargin(0)
    ax.set_ylabel('x (m)', labelpad=25)
    ax.set_zlabel(titre_axe_z)
    ax.set_title(titre_subplot, size='large', style='italic')
    ax.set_zlim(zmin, zmax)
    # ax.ticklabel_format(style= 'plain', axis='both')
    if view_init_auto is False:
        # pure fonction pour parametrer la view
        ax.view_init(elev=30, azim=120)


def grid(coeff):
    """ layer 9 figures + une colorbar; le coeff définit la place relative de la colorbar/aux figures"""
    grid = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    grid = [[coeff*i for i in coord] for coord in grid]
    return(grid)
