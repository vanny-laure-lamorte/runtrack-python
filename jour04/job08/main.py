# Liste de données de départ
L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]


pair = 0

# Parcours de la liste et # vérifie si le nombre est pair et créer une somme entre les chiffres pairs
for nombre in L:
    if (nombre % 2) == 0:
        pair += nombre

# Affichage du résultat
print(f"Voici la somme de toutes les valeurs paires de la liste L : {pair}")

