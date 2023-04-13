def distance_toilettes(marches, hauteur):
    distance_marches = marches * hauteur / 100
    distance_toilettes = distance_marches * 5
    distance_semaine = distance_toilettes * 7
    return round(distance_semaine, 2)
marches = 100
hauteur = 20

distance = distance_toilettes(marches, hauteur)

print(f"Pour {marches} marches de {hauteur} cm, le gardien parcours {distance:.2f} m par semaine.")
