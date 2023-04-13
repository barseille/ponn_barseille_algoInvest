import csv
from action import Action, recup_action_csv
from typing import List


actions1 = recup_action_csv("data/dataset1_Python+P7.csv")

        
def glouton(actions: List[Action], budget: float) -> List[Action]:
    # On trie les actions par profit décroissant
    actions_triees = sorted(actions, reverse=True)
    
    
    # On initialise la liste des actions à acheter
    actions_achetees = []
    
    # On parcourt toutes les actions triées
    for action in actions_triees:
        # Si le prix ou le profit est à 0 ou en négatif, on passe à l'action suivante
        if action.prix <= 0 or action.profit() <= 0:
            continue
        
        # On calcule le nombre d'actions à acheter pour respecter le budget
        nb_actions = int(budget / action.prix)
        
        
        # Si le nombre d'actions est supérieur à 0, on les ajoute à la liste des actions achetées
        if nb_actions > 0:
            actions_achetees.append(action)
            budget -= nb_actions * action.prix
    
    return actions_achetees

# print(glouton(actions1, 500))