# Demander à l'utilisateur de choisir un chiffre supérieur à zéro
try:
    N = int(input("Veuillez entrez un chiffre supérieur à zéro pour afficher la table de multiplication : "))

# Afficher la table de multiplication après que l'utilisateur ait choisi un chiffre supérieur à zéro
    if N > 0:
        for i in range(1, N + 1):
            print(f"Table de multiplication de {i}:")
            for v in range(1, 11):
                print(f"{v} x {i} = {v * i}")

# Afficher un message d'erreur si l'utilisateur choisit un chiffre inférieur ou égal à zero
    else:
        print("Error. entrer un chiffre supérieur à zéro pour afficher la table de multipllication.")                
                    
except ValueError:
    print("Veuillez entrer un nombre entier valide.")
