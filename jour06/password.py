import re
import hashlib
while True:
    passe=input("veuillez entrer votre mot de passe :")
    if len(passe)<8:
     print("le mot de passe doit contenir au moins 8 caractères")
    elif not re.search("[A-Z]",passe):
        print("Le mot de passe doit contenir au moins une lettre majuscule.")
    elif not re.search("[a-z]", passe):
        print("Le mot de passe doit contenir au moins une lettre minuscule.")
    elif not re.search("[0-9]", passe):
        print("Le mot de passe doit contenir au moins un chiffre.")
    elif not re.search("[!@#$%^&*]", passe):
        print("Le mot de passe doit contenir au moins un caractère spécial.")
    else:
        print("Le mot de passe est valide.")
        hashed_password = hashlib.sha256(passe.encode()).hexdigest()
        print("Mot de passe crypté: ", hashed_password)
    break
