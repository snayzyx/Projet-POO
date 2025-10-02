from modules.employes import * 
from modules.stock import * 
from modules.produits import * 


def main():
    print("" \
    "[1]: Créer un emplpyé\n" 
    "[2]: Test")


    choice = input("Faites un choix\n")

    if choice == "1":
        prenom = str(input("Saisissez un prénom:"))
        nom = str(input("Saisissez un nom:"))
        salaire= int(input("Saisissez un salaire"))






main()