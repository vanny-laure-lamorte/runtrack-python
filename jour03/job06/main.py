def chiffre(nombre):
    
    if nombre > 0:
        print (f"Le nombre {nombre} est de catégorie positif.")

    elif nombre < 0:
        print (f"Le nombre {nombre} est de catégorie négatif.")

    else: 
        print ("Error")

chiffre(20)
chiffre(-20)


