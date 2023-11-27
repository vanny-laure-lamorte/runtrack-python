def alphabet(message, decalage): 
    message_chiffre = ""

    for lettre in message: 
         #Si le caractère est une lettre

        if lettre.isalpha():

            # Si le caractère est une minuscule   
            if lettre.islower(): 

                #Ord permet d'avoir la lettre en chiffre et chr fait l'inverse  
                lettre = chr((ord(lettre) - ord('a') + decalage) % 26 + ord('a'))
                
                #On créé un espace vide dans lequel on va mettre les lettres
                message_chiffre += lettre 

            #Si la lettre est une majuscule
            else:
                lettre = chr((ord(lettre) - ord('A') + decalage) % 26 +ord('a'))
                
                #On créé un espace vide dans lequel on va mettre les lettres
                message_chiffre += lettre          
        
        else: 
            message_chiffre += lettre
    return message_chiffre

message = ("L'amour est une sottise faite à deux.")
resultat = alphabet(message, 3)
print(resultat)

