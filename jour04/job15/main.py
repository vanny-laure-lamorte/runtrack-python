# Afficher la liste de départ
liste_initiale= [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print (f"Liste initiale: {liste_initiale}")

# Fonction pour arrondir les chiffres au nombre supérieur
def arrondir_num(num):
    entier = num //1
    decimal = num %1
    if decimal >= 0.5:
        entier+=1
    return entier

# Fonction pour replacer la fonction len
def long(liste):
    count=0
    for i in liste:
        count+=1
    return count

# Fonction qui utilise le trie à bulle pour mettre les chiffres dans l'ordre croissant
def organiser(liste):
    i = long(liste) - 1
    while i > 0:
        j=0
        while j < i:
            if liste[j+1] < liste[j]:
                stock=liste[j+1]
                liste[j+1]=liste[j]
                liste[j]=stock
            j+=1
        i-=1

# Création d'une liste vide pour stocker les chiffres 
L_arrondie = []

# Boucle qui parcours chaque valeur et va arrondir à la valeur supérieur
for i in liste_initiale:
    L_arrondie +=[arrondir_num(i)]

# Pour afficher le resultat avec les chiffres arrondis
organiser(L_arrondie)
print (f"La nouvelle liste avec les chiffres arrondis {L_arrondie}")