# Pour choisir 1000 comme étant la limite de numéro et tester tous les nombres de 2 à 1000
for i in range(2,1001): 

#Prendre le nombre courant (i), et essayer de le diviser par toutes les valeurs entre 2 et lui même.

    for v in range (2,i): 

#Si i % v (donc le nombre en cours; et le diviseur en cours de test) est nul, le nombre est donc divisible par un autre nombre que lui même ou 1.
        if i % v == 0: 

#Dans le cas ou il n'est pas premier, on arrête d'essayer, et on ne vas  pas jusqu'au print
            break 
#La boucle ligne 3 est terminée, et on ne l'a pas break, on arrive ici
    else: 

# on print le nombre courant car on est arrivé au bout de la boucle ligne 3 et on n'a pas trouvé de diviseur. Le nombre est donc premier

        print(i) 