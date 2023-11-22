# Afficher l'alphabet fois 10
list = "abcdefghijklmnopqrstuvwxyz"*10

# Pour afficher sous forme de pyramide
for i in range(len(list)): 
    if i % 2 != 0:
        print(list[:i])            


