nom = "saucisson Saint Agaûne"
prix = 4.15
quantity = 20

print (f"Le {nom} coute {prix}€ et il en reste {quantity} en stock.")

demande = int(input("Quelle quantité de saucisson voulez-vous?"))

quantity = quantity - demande 
print (f"Il reste {quantity} de saucisson Saint Agaûne en stock et coutera 4.15€ l'unité")

prix = prix + prix*(10/100)
print (f"Le prix suite à l’inflation est de {prix}")




