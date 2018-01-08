#nom de l'etude
etud="ESS"

#nom de la lettre du calcul
lettre="M"

#nom générique des fichiers de sortie
nom="res_"$etud_$lettre

#dossier de sortie des fichiers resupo
sortie="res_"$etud

#nombre de fichiers à traiter
num_calcul=`seq 1 9`

#liste des points àù l'on veut les valeurs de sortie ATTENTION à remplacer la virgule par le point
declare -a LISTE_POINTS=(
"-0.14 4.45 1.5"
"-0.14 3.55 1.5"
"-0.14 4.45 2.25"
"-0.14 3.55 2.25"
"-0.14 4.45 3"
"-0.14 3.55 3"
"-0.14 4.45 3.75"
"-0.14 3.55 3.75"
"3 4 4.15"
"3 4 3.35"cd 
"2.25 3.25 3.35"
"2.25 4.275 3.35"
"3 4 3.45"
"8 4 3.45"
"8 4 3.35"
"2.25 4 4.15"
"2.25 4 3.85"
"2.25 4 3.45"
"2.25 4 2.7"
"3.75 4 3.85"
"3.75 4 3.45"
"3.75 4 2.7"
"3.75 3.4 3.45")
#---------------------------------------------------------------------
mkdir $sortie
cp /cygdrive/d/resupo/datasets.dat .
#initation du fichier log
echo "calcul id_point point" > log_points.txt


for i in $num_calcul;
    do
    echo $etud > rep_resupo.txt
    echo "$lettre""$i"  >> rep_resupo.txt
    echo "$nom""$i" >> rep_resupo.txt
    #tracer des points
    echo 1  >> rep_resupo.txt
    #nombre de points
    echo  ${#LISTE_POINTS[*]} >> rep_resupo.txt
    for j in ${!LISTE_POINTS[*]}
        do
        # coord des points auxquels on a enlevé les guillemets
        echo ${LISTE_POINTS[$j]}| tr -d '"' >> rep_resupo.txt
        
        #creation du fichier log
        echo $i"______"`expr $j + 1`"______"${LISTE_POINTS[$j]} >> log_points.txt
    done
    
    #contraintes et déplacements à sortir
    echo 1 2 3 4 5 6 7 8 9 10 11 12 >> rep_resupo.txt
    
    #sortie de fichiers multiples (fonctionnalité pas terrible du logiciel)
    echo M >> rep_resupo.txt
    
    echo 0 >> rep_resupo.txt
    
    /cygdrive/d/resupo/resupov4-32.exe < rep_resupo.txt
    mv "$nom"* ./$sortie 
done
rm rep_resupo.txt
rm datasets.dat
