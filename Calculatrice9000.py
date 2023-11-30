def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Division par zéro")

def afficher_historique(historique):
    print("Historique des opérations :")
    for operation in historique:
        print(operation)

def calculatrice():
    historique = []  # Liste pour stocker l'historique des opérations

    while True:
        try:
            # Demander à l'utilisateur les deux nombres et le type d'opération
            nombre1 = float(input("Entrez le premier nombre (ou 'q' pour quitter) : "))
            
            # Vérifier si l'utilisateur veut quitter
            if nombre1 == 'q':
                break

            nombre2 = float(input("Entrez le deuxième nombre : "))
            operation = input("Entrez le type d'opération (+, -, *, /) : ")

            # Effectuer l'opération appropriée
            if operation == "+":
                resultat = addition(nombre1, nombre2)
            elif operation == "-":
                resultat = soustraction(nombre1, nombre2)
            elif operation == "*":
                resultat = multiplication(nombre1, nombre2)
            elif operation == "/":
                resultat = division(nombre1, nombre2)
            else:
                raise ValueError("Opération non valide")

            # Ajouter l'opération à l'historique
            operation_str = f"{nombre1} {operation} {nombre2} = {resultat}"
            historique.append(operation_str)

            # Afficher le résultat
            print(f"Le résultat de {operation_str}")

        except ValueError as e:
            print(f"Erreur : {e}")
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

    # Afficher l'historique avant de quitter
    afficher_historique(historique)

    # Demander à l'utilisateur s'il veut effacer l'historique
    effacer_historique = input("Voulez-vous effacer l'historique ? (oui/non) : ")
    if effacer_historique.lower() == "oui":
        historique.clear()
        print("L'historique a été effacé.")

# Appeler la fonction principale de la calculatrice
calculatrice()