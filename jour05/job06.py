def arrondir_notes(notes):
    arrondis = []
    for note in notes:
        if note < 40:
            arrondis.append(note)
        elif note % 5 >= 3 and note >= 38:
            arrondis.append(note + 5 - note % 5)
        else:
            arrondis.append(note)
    return arrondis
notes = [38, 55, 63, 72, 87, 91]

arrondis = arrondir_notes(notes)

for i in range(len(notes)):
    print(f"Note : {notes[i]} -> Arrondi : {arrondis[i]}")
