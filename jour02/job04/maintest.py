def afficher_tables_multiplication():

#Demander à l'utilisateur d'afficher un chiffre supérieur à zéro
    while True:
        try:
            N = int(input("Vueillez entrez un chiffre supérieur à zéro pour afficher la table de multiplication : "))



#Afficher la table de multiplication après que l'utilisateur ait choisi un chiffre
            if N > 0:
                for i in range(1, N + 1):
                    print(f"Table de multiplication de {i}:")
                    for v in range(1, 11):
                        print(f"{v} x {i} = {v * i}")

#Afficher un message d'erreur si l'utilisateur choisit un chiffre inférieur ou égal à zero
            else:
                
                if N <= 0:
                    print("Error. entrer un chiffre supérieur à zéro pour afficher la table de multipllication.")                
                    
#Pour sortir de la boucle si l'utilisateur met une donnée incorrect
                break
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

afficher_tables_multiplication()
