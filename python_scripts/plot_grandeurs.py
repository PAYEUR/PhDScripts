# plot_contrainte.py
# -*-coding:Utf-8 -*-
from __future__ import unicode_literals
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import fonctions_moyenne as f_m

nom_modele = "M12"
num_Z = "0"
grandeur = "Fi"
coeff = 1
title_z_axis = grandeur
Xs_barres = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
Y_debut_barre = 0.05
Y_fin_barre = 5
pas = 20

fig = plt.figure()
fig.set_size_inches(15, 10, forward=True)
ax = fig.add_subplot(111, projection='3d')


nom_fichier = nom_modele + "_Z" + num_Z + "_" + grandeur
matrice = np.genfromtxt(nom_fichier, delimiter=";")
matrice = matrice/coeff

# plot

X = Xs_barres
Y = [point[0] for point in f_m.liste_points_barre([Y_debut_barre, 0, 0],
                                                  [Y_fin_barre, 0, 0],
                                                  pas)]
Y, X  = np.meshgrid(Y, X)
surf = ax.plot_surface(Y, X, matrice,
                       rstride=1, cstride=1,
                       cmap=cm.coolwarm, linewidth=1,
                       antialiased=True)

#legende
ax.set_ylabel("Abscisse (m)", labelpad=25)
ax.set_xlabel('Distance au paremement (m)', labelpad=25)
ax.set_zlabel(title_z_axis)
ax.view_init(elev=40, azim=-120)


plt.tight_layout()
plt.savefig(str(nom_fichier) + ".png", format="png")
plt.show()
