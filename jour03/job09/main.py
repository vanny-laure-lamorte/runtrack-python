# Formule pour faire le calcule d'une moyenne selon 3 notes choisies 

def moyenne (note1, note2, note3):
    return (note1 + note2 + note3) / 3

# Pour demander à l'utilisateur de saisir 3 notes

note1 = int(input("Veuillez entrer votre première note : "))
note2 = int(input("Veuillez entrer votre deuxième note : "))
note3 = int(input("Veuillez entrer votre  note : "))

# Pour afficher la moyenne les 3 notes précedement selectionner par l'utilisateur

moyenne_etudiant = moyenne(note1,note2,note3)
print (f"Si vos notes sont: {note1}/20, {note2}/20 et {note3}/20 alors votre moyenne est de {moyenne_etudiant}/20")

# Pour afficher une appréciation en fonction de la moyenne de l'étudiant. 

if 15 <= moyenne_etudiant <= 20:
    print("Très bon élève")
elif 11 <= moyenne_etudiant <= 14:
    print("Bon élève")
elif 8 <= moyenne_etudiant <= 10:
    print("Élève moyen")
elif 0 <= moyenne_etudiant <= 7:
    print("Élève devrait faire des efforts")
else:
    print("La moyenne n'est pas dans les bornes de notation.")