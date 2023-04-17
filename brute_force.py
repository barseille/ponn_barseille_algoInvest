from dataclasses import dataclass
from itertools import combinations
import csv
import cProfile
from decorateur import performance
import math


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
        
        if nom_fichier == "data/dataset1_Python+P7.csv" or nom_fichier == "data/dataset2_Python+P7.csv":
        
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


@performance
def trouver_meilleure_combinaison(actions, budget):  
    """Trouve la meilleure combinaison d'actions qui maximise le profit dans le budget donné"""
    
    #  stocker toutes les combinaisons possibles
    combinaisons = []
    
    #  fonction combinations pour générer toutes les combinaisons possibles
    for i in range(1, len(actions) + 1):
        combinaisons.extend(combinations(actions, i))
        
    meilleure_combinaison = []
    meilleur_profit = 0
    investissement_total = 0
    
    """ Pour chaque combinaison, on fait le total du prix des actions"""
    for combinaison in combinaisons:
        total_prix = sum([action.prix for action in combinaison])   
        
        # on vérifie si le total est inférieur ou égal au budget.
        if total_prix <= budget: 
            total_profit = sum([action.profit() for action in combinaison])
            
            """ 
            On vérifie si le profit total est supérieur au profit total actuel dans la boucle.
            Si c'est le cas, on met à jour le meilleur profit
            """
            if total_profit > meilleur_profit:
                meilleure_combinaison = combinaison
                meilleur_profit = total_profit
                investissement_total = total_prix
                        
    return (meilleure_combinaison, investissement_total)

def obtenir_liste_achat_actions():
    liste_achat_actions = [action.nom for action in meilleure_combinaison]
    return f"Voici la liste des actions à acheter : {liste_achat_actions}"

def obtenir_profit_total():
    profit = sum(action.profit() for action in meilleure_combinaison)
    """ :.2f = float de deux chiffres après la virgule """
    profit_total = f"Profit total sur 2 ans : {profit :.2f} euros"
    return profit_total


# Récupération des données à partir du fichier CSV
actions = recup_action_csv("data/action.csv")

# Recherche de la combinaison d'actions qui maximise le profit dans le budget de 500 euros
meilleure_combinaison, investissement_total = trouver_meilleure_combinaison(actions, 500)

print("Meilleure combinaison d'actions avec un budget de 500 : ")
print(obtenir_liste_achat_actions())
print(obtenir_profit_total())
print(f"Investissement total : {investissement_total:.2f} euros")

# Décorateur cProfile.run() pour profiler la fonction trouver_meilleure_combinaison()
cProfile.run('trouver_meilleure_combinaison(actions, 500)')

# def compteur_combinaison():
#     for i in range(1, 21):
#         nb_combinations = 0
#         for j in range(1, i+1):
#             nb_combinations += math.comb(i, j)
#         print(f"Nombre de combinaisons pour {i} actions : {nb_combinations}")
        
# compteur_combinaison()