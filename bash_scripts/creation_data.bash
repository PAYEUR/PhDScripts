#!/bin/bash
#essai de script qui calcule à la chaine LINC en 3D pour différentes
#fréquences à partir d'un chargment 10%

#mes listes sont déclarées sous forme de tableaux

declare -a LISTE_FREQUENCE=(31.4 62.8 94.2 125.7 157.1 175.9 188.5 219.9
251.3)
declare -a LISTE_ALPHA=(3.09 6.09 9.00 11.8 14.5 16.1 17.1 19.7 22.1)
nom_essai="ESS"
fichier_reference="ESS_reference.data"

#si la longueur des listes d'entree n'est pas bonne, on retourne une erreur
if [ ${#LISTE_ALPHA[*]} -ne ${#LISTE_FREQUENCE[*]} ]
	then
	echo "la longueur des tableaux de donnees n'est pas la même"
	echo "le calcul ne se lançera pas"
#------------------------

else
#initation du fichier log
echo "calcul frequence alpha" > log.txt

#creation du fichier ESS_M1.data
	for i in ${!LISTE_FREQUENCE[*]}
		   do j=`expr $i + 1`
		   temp=$nom_essai"_M"$j".data"
		   sed -e '
		   s/frequ/'"${LISTE_FREQUENCE[$i]}"'/;
		       s/alpha/'"${LISTE_ALPHA[$i]}"'/
  		     ' <$fichier_reference >$temp 
		  
#creation d'une liste de log
		 ligne="M"$j"______"${LISTE_FREQUENCE[$i]}"______"${LISTE_ALPHA[$i]}
		 echo $ligne >> log.txt

	done
fi

