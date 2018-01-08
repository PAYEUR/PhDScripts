#!/bin/bash

#on travaille depuis Bureau/amorti 3E_Soyez/

#On crée le fichier de d'instructions pour cesar
etude=ESS
num_calcul=`seq 1 9`

for i in $num_calcul;
do
echo n > fichier_commande_cesar
echo $etude >> fichier_commande_cesar
echo "M"$i >> fichier_commande_cesar
echo f >> fichier_commande_cesar
/cygdrive/d/CESAR/cesar_v4/GESKEY.exe

/cygdrive/d/CESAR/cesar_v4/CESARv4.exe < fichier_commande_cesar
rm fichier_commande_cesar
done


