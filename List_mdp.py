import json
import getpass
import random as rd
import string

# Fonction pour charger les mots de passe depuis le fichier JSON
def load_passwords():
    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}
    return passwords

# Fonction pour enregistrer les mots de passe dans le fichier JSON
def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)

#Fonction pour générer un nouveau mot de passe
def new_mdp(length):
    chars = string.ascii_letters + string.digits + string.punctuation

    maj = rd.choice(string.ascii_uppercase)
    minuscule = rd.choice(string.ascii_lowercase)
    chiffre = rd.choice(string.digits)
    special = rd.choice(string.punctuation)

    password = maj + minuscule + chiffre + special + ''.join(rd.choice(chars) for _ in range (length-4))
    return password


# Fonction pour ajouter un nouveau mot de passe
def add_password(passwords):
    service = input("Service/plateforme : ")
    username = input("Nom d'utilisateur : ")
    password_choice = input("Souhaitez-vous générer un mot de passe aléatoire ? (Oui/Non) : ")
    if password_choice.lower() == "oui":
        length = int(input("Longueur du mot de passe : "))
        password = new_mdp(length)
    else:
        password = getpass.getpass("Mot de passe : ")
    passwords[service] = {"username": username, "password": password}
    save_passwords(passwords)
    print("Mot de passe enregistré avec succès !")
    

# Fonction pour modifier un mot de passe existant
def modify_password(passwords):
    service = input("Service/plateforme à modifier : ")
    if service in passwords:
        print(f"Modification du mot de passe pour le service/plateforme '{service}'")
        new_password_choice = input("Souhaitez-vous générer un nouveau mot de passe aléatoire ? (Oui/Non) : ")
        if new_password_choice.lower() == "oui":
            new_password = generate_random_password()
        else:
            new_password = getpass.getpass("Nouveau mot de passe : ")
        passwords[service]["password"] = new_password
        save_passwords(passwords)
        print("Mot de passe modifié avec succès !")
    else:
        print(f"Le service/plateforme '{service}' n'existe pas.")


# Fonction pour afficher tous les mots de passe enregistrés
def display_passwords(passwords):
    if not passwords:
        print("Aucun mot de passe enregistré.")
    else:
        for service, data in passwords.items():
            print(f"Service/plateforme : {service}")
            print(f"Nom d'utilisateur : {data['username']}")
            print(f"Mot de passe : {data['password']}")
            print()

# Fonction pour consulter un mot de passe
def view_password(passwords):
    service = input("Service/plateforme à consulter : ")
    if service in passwords:
        print(f"Mot de passe pour le service/plateforme '{service}' : {passwords[service]['password']}")
    else:
        print(f"Le service/plateforme '{service}' n'existe pas.")

# Fonction principale pour gérer les mots de passe
def password_manager():
    passwords = load_passwords()
    while True:
        print("--- Gestionnaire de mots de passe ---")
        print("1. Afficher les mots de passe enregistrés")
        print("2. Ajouter un nouveau mot de passe")
        print("3. Modifier un mot de passe existant")
        print("4. Consulter un mot de passe")
        print("5. Quitter")
        choice = input("Choix : ")
        if choice == "1":
            display_passwords(passwords)
        elif choice == "2":
            add_password(passwords)
        elif choice == "3":
            modify_password(passwords)
        elif choice == "4":
            view_password(passwords)
        elif choice == "5":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

# Exécution du gestionnaire de mots de passe
password_manager()
