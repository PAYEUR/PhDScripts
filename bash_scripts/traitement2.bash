#on travaille sur une seule contrainte

grandeurs="sxx sxy syy syz szx szz u v w"
frequences=`seq 1 9`
id_capteurs=`seq 1 23`
nom_sortie="ESScapteur"
extension_sortie=".csv"
fichier_frequences="frequences.csv"

#######################################################
##récupère la 1ere colonne du fichier fréquences
#cut -d ';' -f 1 $fichier_frequences > liste_frequence_temp

for i in $id_capteurs;
    do
    fichier_sortie="$nom_sortie""$i""$extension_sortie"
    rm -f temp
    touch temp
    
    for grandeur in $grandeurs;
        do    
        echo $grandeur"_Re;"$grandeur"_Im;"> "re_im_par"$grandeur
        #tableau des Re et Im des dépl/contraintes pour chaque fréquence
        for id_frequence in $frequences;
            do
            nom_fichier="nouveau_res_M"$id_frequence"_"$grandeur
        
            #sort les valeurs des contraintes du capteur $i
            sed -n "$i"'p' $nom_fichier >> "re_im_par"$grandeur
        done
        #substitue la fin du fichier par la table précédente pour ajouter les tables par la droite
        paste temp "re_im_par"$grandeur > temp2
        #enlève les tabulations en trop et ajoute une rangée de ; à la fin
        sed -e 's/\t//g;s/$/;/g' temp2 > temp           
    done        
    
    #colle la définition des fréquences.
    #paste liste_frequence_temp temp3 > temp4
    paste temp > $fichier_sortie
    #ajoute le titre et les coord du capteur
    #echo "titre" > $fichier_sortie
    #echo "coordonnées" >> $fichier_sortie
    #paste temp4 >> $fichier_sortie    
done 
   
rm temp*
rm re_im_par*
rm nouveau*