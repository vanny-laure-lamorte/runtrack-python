def tapis(n):

# Pour dessiner la ligne 1 du tapis
    debut ="+" + "-" *(n+1) + "+" 
    print(debut)

# Pour dessiner de la ligne 2 à la ligne 12
    for i in range(n + 1): 
        print("|" + "#"*(n-i) + " " + "#"*i + "|")

# Pour dessiner la ligne 13 du tapis
    base = "+" + "-" *(n+1) + "+" 
    print(base)

# Pour afficher le tapis où "n" équivaut à 10
tapis(10)
