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
        poste = str(input("Saissiez un poste pour votre employé:"))

        E = Employes(prenom,nom,salaire,1,poste)
        print(f"Vous avez recruté {nom} {prenom},il sera {poste},Vous lui avez donner {salaire}€ par mois")
        correct = str(input("Est-ce Bien correcte [O-N]"))
        if correct == "N":
            print("Prenom,Nom,Salaire,Poste")
            edits = str(input("Que souhaitez vous Modifier: "))
            






main()