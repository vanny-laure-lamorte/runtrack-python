# Liste initiale avec les doublons
liste_initiale = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Afficher la liste initale
print(liste_initiale)

# Créer une liste vide
new_liste= []

# i parcours la liste initiale et ajoute les chiffres dans la nouvelle liste si le i n'y pas déja présent dans new liste. 
for i in liste_initiale:
    if i not in new_liste:
        new_liste = new_liste + [i]

# Afficher la liste sans doublons
print(new_liste)
