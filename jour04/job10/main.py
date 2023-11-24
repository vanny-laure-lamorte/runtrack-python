L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

# On attribue la valeur 1 pour garantir un calcul correct du produit des valeurs dans l'intervalle spécifié. Si on commence par 0, le produit de n'importe quel nombre par 0 sera toujours 0. C'est pourquoi on utilise 1 ici.

resultat = 1

# Dans la liste L, on souhaite récupérer des valeurs
for nombre in L: 

# Pour indiquer qu'on souhaite uniquement les valeurs entre 25 et 90 de la liste L
    if 25 < nombre < 90:

# Pour multiplier les valeurs entre elles
        resultat *= nombre

# Pour afficher le resultat de la multiplication de toutes les valeurs
print(resultat)






