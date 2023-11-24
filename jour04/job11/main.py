# Créer une liste d'entiers
L = [7, 11, 42, 39, 2]

# On va considérer que v est une variable qui prendre la valeur de chacun des chiffres consécutivement, de la liste L 
for v in range(len(L)):

# Pour additionner +1 à chaque chiffre de la liste
    L[v] += 1

# Afficher la nouvelle liste L avec chaque valeur ayant +1
print(L)

