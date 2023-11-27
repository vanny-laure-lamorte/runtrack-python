
def draw_rectangle(width, height):
    width = width - 2
    height = height - 2
    
# Dessiner la première ligne
    print("|" + "-"*width + "|") 
    
# Dessiner les lignes du milieu
    y = 0
    while y < height:
        print('|' + ' ' *width + '|')
        y = y+1
    
# Dessiner la dernière ligne
    print("|" + "-"*width + "|")    

# Appeler la fonction avec les valeurs 10 et 3
draw_rectangle(10, 3)
