#!/bin/bash
frequences=`seq 1 9`


##on reformate une première fois les fichiers de sortie pour avoir partie réelle et imaginaire l'un à côté de l'autre

#pour les contraintes
list="sxx sxy syy syz szx szz"
for grandeur in $list
    do
    for frequence in $frequences
        do

        fichier_traite="res_M"$frequence"_"$grandeur
        new="nouveau_"$fichier_traite

        echo "fichier traité : "$fichier_traite
        
        #remplace les tabulations par des ;
        tr -s [:blank:] < $fichier_traite > temp
        sed -e 's/\s/;/g' temp > temp2

        # Commance le tri
        for i in `seq 1 2`
            do
            sed -ne '/^;'"$i"'/p' temp2 > col
            #recupère les bonnes colonnes
            cut -d ';' -f 6 col > "truc"$i
        done
        
        #fusion du fichier final et remplace les . par , et les tabulations par des ; y compris à la fin
        paste truc1 truc2 > machin
        sed -e 's/\t/;/g;s/\./,/g;s/$/;/g' machin > $new
    done
done

# pour les déplacements
for frequence in $frequences
    do
    list="u(re) v(re) w(re)"
    for grandeur in $list
        do
        fichier_traite="res_M"$frequence"_"$grandeur
        echo "fichier traité : "$fichier_traite
        
        #remplace les tabulations par des ;
        tr -s [:blank:] < $fichier_traite > temp
        sed -e 's/\s/;/g' temp > temp2        
        sed -ne '/^;'"1"'/p' temp2 > col
        #recupère les bonnes colonnes
        cut -d ';' -f 6 col > Re_$grandeur
    done

    list="u v w"
    for grandeur in $list
        do
        fichier_traite="res_M"$frequence"_"$grandeur
        echo "fichier traité : "$fichier_traite
        
        #remplace les tabulations par des ;
        tr -s [:blank:] < $fichier_traite > temp
        sed -e 's/\s/;/g' temp > temp2
        sed -ne '/^;'"2"'/p' temp2 > col
        #recupère les bonnes colonnes
        cut -d ';' -f 6 col > Im_$grandeur


        #fusion du fichier final et remplace les . par , et les tabulations par des ; y compris à la fin
        paste "Re_"$grandeur"(re)" "Im_"$grandeur > machin
        sed -e 's/\t/;/g;s/\./,/g;s/$/;/g' machin > "nouveau_res_M"$frequence"_"$grandeur
    done
done

rm machin
rm temp*
rm col
rm truc*
rm Re_*
rm Im_*