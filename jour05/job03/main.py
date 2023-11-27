# Cette ligne demande à l'utilisateur d'entrer la hauteur du triangle. 
hauteur = int(input("Entrez la hauteur de votre triangle: "))

# Cette fonction va dessiner un triangle en fonction de la valeur donnée au départ (=hauteur)
def triangle(hauteur):

# On va créer une boucle qui va itérer de 0 jusqu'à la valeur "hauteur"5

    for i in range(hauteur - 1):

# Créer une variable pour stocker le calcul des espaces 
        espace = " " * (hauteur - i - 1)

# Si i équivaut à zero alors on pourra afficher le chapeau (1er ligne) du triangle
        if i == 0:
            print(espace + "/\\")
# Pour augmenter les espaces avant et dans " / " et "\" du triangle
        else:
            print(espace + "/" + " " * (2 * i) + "\\")

# Pour dessiner la base du triangle qui commence par /, suivi de "-" et qui se termine avec \
    base = "/" + "_" * (2 * hauteur - 2) + "\\"
    print(base)

# Appeler la fonction en fonction de la hauteur donné par l'utilisateur
triangle(hauteur)
