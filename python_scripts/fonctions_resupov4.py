# fonctions_resupov4.py
# -*-coding:Utf-8 -*-


def nom_fichier_instructions(nom_etude, nom_modele):
    return(nom_etude + "_" + nom_modele + ".instruresupo")


def fichier_instructions_resupo(nom_etude, nom_modele, liste_numero_grandeurs,
                                liste_points, pdt_min, pdt_max,
                                nom_fichier_sortie, unique=True):

    liste_instructions = creation_liste_instructions(nom_etude,
                                                     nom_modele,
                                                     liste_numero_grandeurs,
                                                     liste_points,
                                                     pdt_min, pdt_max,
                                                     nom_fichier_sortie,
                                                     unique=True)

    # transformation de la liste d'arguments en fichier texte lisible
    # par resupov4.
    with open(nom_fichier_instructions(nom_etude, nom_modele), "w") as fichier:
        for instruction in liste_instructions:
            fichier.write(str(instruction+"\n"))


def run_resupov4(nom_executable_resupo, nom_etude, nom_modele,
                 liste_numero_grandeurs, liste_points, pdt_min, pdt_max,
                 nom_fichier_sortie, unique=True):

    fichier_instructions_resupo(nom_etude, nom_modele, liste_numero_grandeurs,
                                liste_points,
                                pdt_min, pdt_max,
                                nom_fichier_sortie,
                                unique=True)
    import os
    os.system("/home/PAYEUR/fonctions+programmes/" +
              nom_executable_resupo + " < " +
              nom_fichier_instructions(nom_etude, nom_modele))

    os.system("rm " + nom_fichier_instructions(nom_etude, nom_modele))


def creation_liste_instructions(nom_etude, nom_modele, liste_numero_grandeurs,
                                liste_points, pdt_min, pdt_max,
                                nom_fichier_sortie, unique=True):
    # syntaxe à retenir!!!
    liste_numero_grandeurs = [str(i) for i in liste_numero_grandeurs]

    # transfo la liste de points(qui sont eux même une liste de coordonnées),
    # en lignes de texte
    liste_points2 = []
    for point in liste_points:
        point = [str(i) for i in point]
        point2 = ",".join(point)
        liste_points2.append(point2)

    i = pdt_min
    chaine_pdt = ""
    while i <= pdt_max:
        chaine_pdt = chaine_pdt + " " + str(i)
        print(chaine_pdt)
        i += 1
    print(chaine_pdt)
    liste_instructions = [nom_etude, nom_modele,
                          nom_fichier_sortie,
                          "1",  # tracer des points
                          str(len(liste_points))  # nombre de points
                          ]
    liste_instructions.extend(liste_points2)
    liste_instructions.append(" ".join(liste_numero_grandeurs))

    if unique:
        liste_instructions.append("U")  # fichiers unique
    else:
        liste_instructions.append("M")  # fichiers multiples

    liste_instructions.append(chaine_pdt)

    return(liste_instructions)

# creation_liste_instructions("tata", 1, [18,4], [14.5, 12.7], 18, 22)
