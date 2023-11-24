# Je mets entre crochets 5 entier et j'utilise print pour avec ma liste. 
L =  [1,2,3,4,5]
print(L) 

# J'indique 1 entre crochets pour indiquer la deuxième valeur de la liste car la première valeur correspond à l'indice 0.
print (L[1]) 

# Fonction qui remplace L[3] par la somme des cases voisines L[2] & L[4]

def changer_liste(nombre):
    nombre[3] = nombre[2] + nombre[4]

changer_liste(L)

print("La nouvelle list est:", L)

# Puis afficher la dernière valeur de la liste j'utilise "len" avec -1
print(L[len(L)-1])