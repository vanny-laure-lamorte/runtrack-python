# Pour choisir 1000 comme étant la limite de numéro
for i in range(2,1001): #Tester tous les nombres de 2 à 1000
    for v in range (2,i): #Prendre le nombre courant (i), et essayer de le diviser par toutes les valeurs entre 2 et lui même.
        if i % v == 0: #Si i % v (donc le nombre en cours; et le diviseur en cours de test) est nul, le nombre est donc divisible par un autre nombre que lui même ou 1.
            break #Dans le cas ou il n'est pas premier, on arrête d'essayer, et on ne vas  pas jusqu'au print
    else: #La boucle ligne 3 est terminée, et on ne l'a pas break, on arrive ici
        print(i) # on print le nombre courant car on est arrivé au bout de la boucle ligne 3 et on n'a pas trouvé de diviseur. Le nombre est donc premier

