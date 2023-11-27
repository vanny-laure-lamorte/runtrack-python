
# La fonction nommée "trajet" prend deux arguments: x et y.
def trajet(x,y):

    # Pour calculer la distance du trajet en multipliant les valeurs de x (marches), y(hauteur des marches), 2 (aller-retour du trajet) 5 ( le gardien va 5 fois aux toilettes) et 7 ( car une semaine comporte 7 jours). Ensuite on divise le résultat par 100 car on souhaite avoir le résultat en cm.
    trajet = (x*y*2*5*7)/100
    return trajet

# Pour demander à l'utilisateur de choisir le nombre et la hauteur des marches
x = int(input("Choisissez le nombre de marches : "))
y = int(input("Choisissez la hauteur de la marche en cm : "))

# On stocke le résultat dans une variable appelée "distance"
distance = trajet(x,y)

# Pour afficher le résulat en fonction de la quantité de marches et leur hauteur saisies par l'utilisateur, ainsi que la distance calculée à l'aide de la fonction "trajet".
print (f"Pour {x} marches de {y} cm, le gardien parcourt {distance}m par semaine.")