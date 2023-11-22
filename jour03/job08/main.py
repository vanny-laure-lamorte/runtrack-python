def jardin(type, saison):

    if type == "fruits"  and saison == "hiver":
        print ("orange, mandarine et kiwi")

    elif type == "fruits" and saison == "ete":
        print ("Poire, fraise, cassis")

    elif type == "legume" and saison == "hiver":
        print ("carotte, topinambour, endive")

    elif type == "legume" and saison == "ete":
        print ("artichaut, aubergine,navet")

    else:
        print("Error")

jardin ("fruits","hiver")
jardin ("fruits", "ete")
jardin ("legume", "hiver")
jardin ("legume","ete")
jardin ("icetea", "coca-cola")




