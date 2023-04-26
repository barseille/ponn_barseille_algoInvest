from dataclasses import dataclass
from time import perf_counter
import csv
import tracemalloc


@dataclass
class Action:
    
    nom: str
    prix: float
    pourcent: float
    
    # calcul du profit
    def profit(self):
        return self.prix * self.pourcent / 100

    def __str__(self):
        return f"nom : {self.nom}, prix : {self.prix}, pourcent : {self.pourcent}%, profit : {self.profit():.2f}"

    # Comparaison entre deux instances
    def __lt__(self, autre_action):
        return self.pourcent < autre_action.pourcent

def recup_action_csv(nom_fichier):
    
    with open(nom_fichier, "r") as f:
        data = csv.reader(f, delimiter=",")
        actions = []
           
        # Lire la première ligne pour vérifier si elle contient des en-têtes
        headers = None
        try:
            headers = next(data)
        except StopIteration:
            pass

        for row in data:
            nom = row[0]
            prix = float(row[1])
            pourcent = float(row[2])

            if prix <= 0.0 or pourcent <= 0.0:  
                continue        

            action = Action(nom, prix, pourcent)
            actions.append(action)
        
        return actions   

#  Mesurer le temps d'exécution
def performance(fonction):
    
    """Surveiller le temps d'exécution d'une fonction"""
    def wrapper(*args, **kawrgs):

        # Enregistrer le temps actuel avant l'exécution de la fonction passée en argument
        temps1 = perf_counter()    
        
        # Appeler la fonction passée en argument avec les arguments et les mots-clés fournis
        resultat = fonction(*args, **kawrgs) 
         
        # Enregistrer le temps actuel après l'exécution de la fonction passée en argument
        temps2 = perf_counter()
        
        print(f"\nLa fonction {fonction.__name__} a pris {round(temps2 - temps1, 5)} secondes")
        return resultat
   
    return wrapper

@performance
def acheter_actions(budget_max, actions):
    # Tri des actions par profit décroissant
    actions_triees = sorted(actions, reverse=True)

    actions_achetees = []
    budget_investi = 0
    
    # O(n) = boucle for
    for action in actions_triees:
        if action.prix <= budget_max - budget_investi:
            actions_achetees.append(action)
            budget_investi += action.prix
    
    return actions_achetees, budget_investi

def afficher_resultats(actions_achetees, budget_investi):
    
    actions_choisis = []
    print(f"Budget investi : {budget_investi:.2f}")
    print(f"Profit total : {sum(action.profit() for action in actions_achetees) :.2f}")
    print("Actions achetées : ")
    for action in actions_achetees:
        actions_choisis.append(action.nom)
    print(f"{actions_choisis}\n")
       
def main():
    
    tracemalloc.start()
    
    # Récupération des actions depuis le fichier CSV
    actions1 = recup_action_csv("data/dataset1_Python+P7.csv")
    actions2 = recup_action_csv("data/dataset2_Python+P7.csv")
    
    print("-"*40)
    print("Résultats pour dataset1_Python+P7.csv :")
    print("-"*40)
    actions_achetees1, budget_investi1 = acheter_actions(500, actions1)
    afficher_resultats(actions_achetees1, budget_investi1)
    
    print("-"*40)
    print("Résultats pour dataset2_Python+P7.csv :")
    print("-"*40)
    actions_achetees2, budget_investi2 = acheter_actions(500, actions2)
    afficher_resultats(actions_achetees2, budget_investi2)

    # Obtenez la quantité de mémoire utilisée pendant l'exécution de la fonction
    memoire_courante, memoire_max = tracemalloc.get_traced_memory()
    print(f"Utilisation de mémoire courante : {memoire_courante / 10**6} MB")
    print(f"Utilisation de mémoire maximale : {memoire_max / 10**6} MB\n")
    
    tracemalloc.stop()

if __name__ == "__main__":
    main()
