from brute_force import recup_action_csv, performance
import tracemalloc

# Récupération des actions depuis le fichier CSV
actions1 = recup_action_csv("data/dataset1_Python+P7.csv")
actions2 = recup_action_csv("data/dataset2_Python+P7.csv")

@performance
def acheter_actions(budget_max, actions):
    # Tri des actions par profit décroissant
    actions_triees = sorted(actions, reverse=True)

    actions_achetees = []
    budget_investi = 0

    #  O(n) = boucle for
    for action in actions_triees:
        if action.prix <= budget_max - budget_investi:
            actions_achetees.append(action)
            budget_investi += action.prix

    return actions_achetees, budget_investi


def main():
    tracemalloc.start()
    
    # Acheter des actions pour chaque fichier CSV
    liste1 = []
    actions_achetees1, budget_investi1 = acheter_actions(500, actions1)
    profit1 = sum(action.profit() for action in actions_achetees1)
    
    liste2 = []
    actions_achetees2, budget_investi2 = acheter_actions(500, actions2)
    profit2 = sum(action.profit() for action in actions_achetees2)

    # Afficher les résultats pour chaque fichier CSV
    print("\nRésultats pour dataset1_Python+P7.csv :")
    print(f"Budget investi : {budget_investi1:.2f}")
    print(f"Profit total : {profit1:.2f}")
    print("Actions achetées : ")
    for action in actions_achetees1:
        liste1.append(action.nom)
    print(f"{liste1}\n")

    
    print("Résultats pour dataset2_Python+P7.csv :")
    print(f"Budget investi : {budget_investi2:.2f}")
    print(f"Profit total : {profit2:.2f}")
    print("Actions achetées : ")
    for action in actions_achetees2:
        liste2.append(action.nom)
    print(f"{liste2}\n")
    
    # Obtenez la quantité de mémoire utilisée pendant l'exécution de la fonction
    memoire_courante, memoire_max = tracemalloc.get_traced_memory()
    print(f"Utilisation de mémoire courante : {memoire_courante / 10**6} MB")
    print(f"Utilisation de mémoire maximale : {memoire_max / 10**6} MB\n")
    
    tracemalloc.stop()

if __name__ == "__main__":
    main()
