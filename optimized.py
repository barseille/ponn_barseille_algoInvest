from brute_force import recup_action_csv
from performance import performance
import cProfile


# Récupération des actions depuis le fichier CSV
actions1 = recup_action_csv("data/dataset1_Python+P7.csv")
actions2 = recup_action_csv("data/dataset2_Python+P7.csv")

@performance
def acheter_actions(budget_max, actions):
    # Tri des actions par profit décroissant
    actions_triees = sorted(actions, reverse=True)

    actions_achetees = []
    budget_investi = 0

    for action in actions_triees:
        if action.prix <= budget_max - budget_investi:
            actions_achetees.append(action)
            budget_investi += action.prix

    return actions_achetees, budget_investi

# Acheter des actions pour chaque fichier CSV
actions_achetees1, budget_investi1 = acheter_actions(500, actions1)
actions_achetees2, budget_investi2 = acheter_actions(500, actions2)
profit1 = sum(action.profit() for action in actions_achetees1)
profit2 = sum(action.profit() for action in actions_achetees2)

# Afficher les résultats pour chaque fichier CSV
print("Résultats pour dataset1_Python+P7.csv :")
print(f"Budget investi : {budget_investi1:.2f}")
print(f"Profit total : {profit1:.2f}")
print("Actions achetées : ")
for action in actions_achetees1:
    print(action.nom)

print("Résultats pour dataset2_Python+P7.csv :")
print(f"Budget investi : {budget_investi2:.2f}")
print(f"Profit total : {profit2:.2f}")
print("Actions achetées : ")
for action in actions_achetees2:
    print(action.nom)

# Profiler la fonction acheter_actions avec cProfile
# cProfile.run('acheter_actions(500, actions1)')
# cProfile.run('acheter_actions(500, actions2)')