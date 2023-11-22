# Fonction pour prendre des minutes pour le convertir en heures et minutes
def time_to_text(minutes):
    heures = minutes // 60
    minute_restante = minutes % 60

# Dans le cas où il n'y a pas d'heure, on affiche les minutes restantes du calcul
        
    if heures == 0:
        print(f"{minute_restante} minutes")

# Dans le cas où il n'y a pas de minutes, on affiche les heures restantes 

    elif minute_restante == 0:
        print(f"{heures} heures")
    
# Pour afficher l'heure et les minutes en fonction du calcul
 
    else:
        print(f"{heures} heures et {minute_restante} minutes")

# Appelle a la fonction pour afficher 2h  et 40min soit (60x2+40=160)

time_to_text(160)
