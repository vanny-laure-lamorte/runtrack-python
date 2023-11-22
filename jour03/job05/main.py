def calcule(num1, operator, num2):
    
    if operator == '+':
        return num1 + num2

    elif operator == '-':
        return num1 - num2

    elif operator == '*':
        return num1 * num2

    elif operator == '/':
        return num1 / num2

    elif operator == '%':
        return num1 % num2

    else:
        print("L'opération n'est pas faisable")
    
# Exemple d'utilisation de la fonction calcule

resultat = calcule(10, '-' , 20)
print(f"Le résultat de votre opération est {resultat}")
