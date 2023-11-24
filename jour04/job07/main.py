    
# Liste L avec les données 8, 24,48,2,16].
L = [8, 24, 48, 2, 16]

# Compteur pour les multiples de 3
compte = 0

# Parcours de la liste et # vérifie si le nombre est un multiple de 3
for nombre in L:
    if nombre % 3 == 0:
        compte +=1

# Affichage du résultat
print(f"Le nombre de multiples de 3 appartenant à la liste L est :{compte}")
