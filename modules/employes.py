class Employes:

    def __init__(self,lastname,firstname,salary,id,job):
        self.prenom = firstname
        self.nom = lastname
        self.salaire = salary
        self.id = id 
        self.poste= job
        






class Paiement:
    def __init__(self, montant, mode):
        self.montant = montant            
        self.mode = mode                  
    
    def afficher_details(self):
        print(f"Montant payé : {self.montant} €")
        print(f"Mode de paiement : {self.mode}")

    def est_valide(self):
        return self.montant > 0
        
    