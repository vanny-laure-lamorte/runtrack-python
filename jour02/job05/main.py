# Déterminer un interval entre 1 et 100

for i in range(1, 101):

#Pour que les multiples de 3 et 5, affiche "FizzBuzz"
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

# Pour remplacer les multiples de 3 par le mot "Fizz" et les multiples de 5 par "Buzz"

    elif i % 3 == 0:
        print("Fizz")
                
    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)
