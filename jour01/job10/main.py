investissement = 10000
taux = 3/100

rendement = investissement*taux
print (f"En temps 1, le rendement annuel est de {rendement}")

investissement = investissement + rendement + 5000
taux = taux + 2/100 *taux
rendement = investissement * taux
print (f"En temps 2, le nouveau rendement annuel est de {rendement}")

investissement = investissement - 10/100
taux = taux - 1/100
rendement = investissement *taux
print (f"En temps 3, Le nouveau rendement annuel est de {rendement}")
