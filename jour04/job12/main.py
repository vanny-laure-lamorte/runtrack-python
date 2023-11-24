liste = [10, 20, 50, 5, 1, 15]

# Recréer un len pour compte le nombre de chiffre dans la liste "liste"
def organiser(chiffre):
    taille_liste = 0
    for i in chiffre:
        taille_liste +=1
    return (taille_liste)

# Créer une fonction pour comparer les chiffres entre eux et les classer en ordre croissant

def trier_croissant(trier):     
    i = organiser(trier) -1
    while i > 0: 
        j = 0
        while j < i: 
            if trier[j+1] < trier[j]: 
                stocker = trier[j+1]
                trier [j+1] = trier [j]
                trier[j] = stocker
            j += 1
        i -= 1
print(liste)
trier_croissant(liste)
print(liste)


