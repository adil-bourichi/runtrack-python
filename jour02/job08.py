def fct ( type, saison):
    if type == "fruits" and saison == "hiver":
        print ("orange, mandarine et kiwi")
    elif type== "fruits" and saison == "ete":
        print ("Poire, fraise, cassis")
    elif type== "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type== "legume" and saison == "ete":
        print("artichaut, aubergine,navet")
    else:
        print("pas connu")
fct ("legume","ete")
fct ("legume","hiver")
fct ("fruits","ete")
fct ("fruits","hiver")