def nombre_pair_impair (v):

#Si le nombre (v) est divisible par 2 sans reste, alors il est pair.
    if (v % 2) == 0 and v > 0 and (v % 1 == 0):
        print(f"Le nombre {v} est pair")

# Si le nombre (v) n'est pas divisible par 2, alors il est impaire

    elif (v % 2) != 0 and v > 0 and (v % 1 == 0):
        print(f"Le nombre {v} est impair")
 
    else:
        print("Error. Ce nombre n'est pas entier ou positif")

# Appel de la fonction pour exécuter le programme
nombre_pair_impair (5)
nombre_pair_impair (10)
nombre_pair_impair (20)
nombre_pair_impair (22)
nombre_pair_impair (0.2)