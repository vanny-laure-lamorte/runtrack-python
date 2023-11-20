# J'ai choisi 100 comme capital de départ et un taux de 3% par an
capital = 100
taux = 3/100

interets = capital * taux
print (f"En temps 1, l'interêt annuel est de {interets}")

# Au capital initial s'ajoutent les intérêts et 5000 pour l'année suivante
capital = capital + interets + 5000

# On applique à ce nouveau un taux initial majoré de 2%
taux = taux + taux*2/100

interets = capital * taux
print (f"En temps 2, l'interêt annuel est de {interets}")

# On retire 10% du capital précédemment calculé et l'ancien taux est minoré de 1%
capital = capital - 10/100
taux = taux - taux*1/100

interets = capital * taux

# Le capital final 
capital = capital + interets

print (f"En temps 3, le capital final est {capital} et l'interêt annuel est de {interets}")
