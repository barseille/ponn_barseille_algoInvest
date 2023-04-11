from dataclasses import dataclass
from itertools import combinations
import csv

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
        
        for row in data:
            nom = row[0]
            prix = float(row[1])
            benefice = float(row[2])
            
            if prix <= 0.0 or benefice <= 0.0:
                continue
            
            action = Action(nom, prix, benefice)
            actions.append(action)
            
        return actions
    
    
def toutes_combinaisons(donnees: list) -> list:
    """Retourne toutes les combinaisons possibles à partir d'une liste"""
    toutes_combi = []
    for n in range(1, len(donnees) + 1):
        combinaisons = combinations(donnees, n)
        for combi in combinaisons:
            toutes_combi.append(combi)
    return toutes_combi

data = []
with open("data/action.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        element = row[0]
        data.append(element)
combinaisons_possibles = toutes_combinaisons(data)
print(combinaisons_possibles)
