# Fonction pour arrondir les notes 
def evaluation(notes):
    
    note_arrondie = []

    for note in notes:
        # Vérifie si l'étudiant a réussi le test
        if note > 40:          
                
            # Calcule le prochain multiple de 5 supérieur
            multiple_5_sup= ((note + 4) // 5) * 5  

            # Vérifie si l'arrondi est nécessaire
            if multiple_5_sup - note < 3:  
                # Ajoute la note arrondie
                note_arrondie.append(multiple_5_sup) 
            else:
                # Garde la note telle quelle
                note_arrondie.append(note) 
        else:
            # Garde la note telle quelle
            note_arrondie.append(note)  
    return note_arrondie

# Exemple d'utilisation de la fonction
liste_notes = [43, 45, 39, 74]
note_arrondie = evaluation(liste_notes)

# Pour afficher la liste initiale et la liste après avoir arrondi les notes
print(f"Notes initiales :{liste_notes}")
print(f"Notes arrondies : {note_arrondie}")
