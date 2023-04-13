from itertools import combinations
from action import Action
import csv


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
            benefice = float(row[2])
            
            if prix <= 0.0 or benefice <= 0.0:
                continue
            
            action = Action(nom, prix, benefice)
            actions.append(action)
            
        return actions
    
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
    
    # Pour chaque combinaison possible, on calcule le total du prix des actions dans la combinaison
    for combinaison in combinaisons:
        total_prix = sum([action.prix for action in combinaison])
        total_prix = 0  
        for action in combinaison:
            total_prix += action.prix
        
        # on vérifie si le total est inférieur ou égal au budget.
        if total_prix <= budget: 
            total_profit = sum([action.profit() for action in combinaison])
            
            """ 
            Si oui, on calcule le profit total de cette combinaison 
            et on vérifie si le profit total est supérieur au meilleur profit.
            """
            if total_profit > meilleur_profit:
                meilleure_combinaison = combinaison
                meilleur_profit = total_profit
                investissement_total = total_prix
                        
    return (meilleure_combinaison, investissement_total)

def obtenir_liste_achat_actions(meilleure_combinaison):
    print("Voici la liste des actions à acheter : ")
    liste_achat_actions = ", ".join([action.nom for action in meilleure_combinaison])
    return liste_achat_actions

    # liste_achat_actions = []
    # for action in meilleure_combinaison:
    #     liste_achat_actions.append(action.nom)

def obtenir_profit_total(meilleure_combinaison):
    profit = sum(action.profit() for action in meilleure_combinaison)
    """ :.2f = float de deux chiffres après la virgule """
    profit_total = f"Profit total sur 2 ans : {profit :.2f} euros"
    return profit_total

# Récupération des données à partir du fichier CSV
actions = recup_action_csv("data/action.csv")


# Recherche de la combinaison d'actions qui maximise le profit dans le budget de 500 euros
meilleure_combinaison, investissement_total = trouver_meilleure_combinaison(actions, 500)

print("Meilleure combinaison d'actions avec un budget de 500 euros : ")
print(obtenir_liste_achat_actions(actions))
print(obtenir_profit_total(actions))
print(f"Investissement total : {investissement_total:.2f} euros")

