class Vehicule:
    def __init__(self):
        self.marque = ""
        self.modele = ""
        self.annee = 0
        self.couleur = ""
        self.kilometrage = 0.0
        self.carburant = ""
        self.type = ""

vehicules = []
nbVehicules = 0
MAX_VEHICULES = 100

def ajouterVehicule():
    global nbVehicules
    if nbVehicules >= MAX_VEHICULES:
        print("Impossible d'ajouter un véhicule. Le nombre maximal de véhicules a été atteint.")
        return

    v = Vehicule()

    print("Ajout d'un véhicule")
    v.marque = input("Marque : ")
    v.modele = input("Modèle : ")
    v.annee = int(input("Année : "))
    v.couleur = input("Couleur : ")
    v.kilometrage = float(input("Kilométrage : "))
    v.carburant = input("Carburant : ")
    v.type = input("Type de véhicule : ")

    vehicules.append(v)
    nbVehicules += 1

    print("Véhicule ajouté avec succès.")

def supprimerVehicule():
    global nbVehicules
    if nbVehicules == 0:
        print("Aucun véhicule enregistré.")
        return

    print("Suppression d'un véhicule")
    num = int(input("Numéro du véhicule à supprimer (1-{}): ".format(nbVehicules)))

    if num < 1 or num > nbVehicules:
        print("Numéro de véhicule invalide.")
        return

    del vehicules[num - 1]
    nbVehicules -= 1

    print("Véhicule supprimé avec succès.")

def modifierVehicule():
    global nbVehicules
    if nbVehicules == 0:
        print("Aucun véhicule enregistré.")
        return

    print("Modification d'un véhicule")
    num = int(input("Numéro du véhicule à modifier (1-{}): ".format(nbVehicules)))

    if num < 1 or num > nbVehicules:
        print("Numéro de véhicule invalide.")
        return

    v = vehicules[num - 1]

    v.marque = input("Marque [{}]: ".format(v.marque))
    v.modele = input("Modèle [{}]: ".format(v.modele))
    v.annee = int(input("Année [{}]: ".format(v.annee)))
    v.couleur = input("Couleur [{}]: ".format(v.couleur))
    v.kilometrage = float(input("Kilométrage [{}]: ".format(v.kilometrage)))
    v.carburant = input("Carburant [{}]: ".format(v.carburant))
    v.type = input("Type de véhicule [{}]: ".format(v.type))

    vehicules[num - 1] = v

    print("Véhicule modifié avec succès.")

def afficherStatistiques():
    global nbVehicules
    if nbVehicules == 0:
        print("Aucun véhicule enregistré.")
        return

    nbVoituresNoires = 0
    nbVoituresBlanches = 0
    nbTypesVehicules = 0
    nbVoituresEssence = 0
    nbVoituresDiesel = 0
    nbVoituresElectriques = 0

    for v in vehicules:
        if v.couleur == "noir":
            nbVoituresNoires += 1

        if v.couleur == "blanc":
            nbVoituresBlanches += 1

        if v.carburant == "essence":
            nbVoituresEssence += 1

        if v.carburant == "diesel":
            nbVoituresDiesel += 1

        if v.carburant == "électrique":
            nbVoituresElectriques += 1

        if v.type not in [vehicules[i].type for i in range(nbVehicules)]:
            nbTypesVehicules += 1

    print("Statistiques")
    print("Nombre de voitures noires :", nbVoituresNoires)
    print("Nombre de voitures blanches :", nbVoituresBlanches)
    print("Nombre de types de véhicules :", nbTypesVehicules)
    print("Nombre de voitures essence :", nbVoituresEssence)
    print("Nombre de voitures diesel :", nbVoituresDiesel)
    print("Nombre de voitures électriques :", nbVoituresElectriques)

def afficherVehicules():
    global nbVehicules
    if nbVehicules == 0:
        print("Aucun véhicule enregistré.")
        return

    print("Liste des véhicules")
    for i, v in enumerate(vehicules):
        print("Véhicule", i + 1)
        print("Marque :", v.marque)
        print("Modèle :", v.modele)
        print("Année :", v.annee)
        print("Couleur :", v.couleur)
        print("Kilométrage :", v.kilometrage)
        print("Carburant :", v.carburant)
        print("Type de véhicule :", v.type)
        print()

def rechercherVehicule():
    global nbVehicules
    if nbVehicules == 0:
        print("Aucun véhicule enregistré.")
        return

    critere = input("Recherche d'un véhicule\nCritère de recherche : ")

    trouve = False

    for i, v in enumerate(vehicules):
        if critere in [v.marque, v.couleur, v.type]:
            print("Véhicule", i + 1)
            print("Marque :", v.marque)
            print("Modèle :", v.modele)
            print("Année :", v.annee)
            print("Couleur :", v.couleur)
            print("Kilométrage :", v.kilometrage)
            print("Carburant :", v.carburant)
            print("Type de véhicule :", v.type)
            print()
            trouve = True

    if not trouve:
        print("Aucun véhicule correspondant au critère de recherche.")

choix = -1

while choix != 0:
    print("---- Application de gestion des véhicules ----")
    print("1. Ajouter un véhicule")
    print("2. Supprimer un véhicule")
    print("3. Modifier un véhicule")
    print("4. Afficher les statistiques")
    print("5. Afficher la liste des véhicules")
    print("6. Rechercher un véhicule")
    print("0. Quitter")
    choix = int(input("Votre choix : "))

    if choix == 1:
        ajouterVehicule()
    elif choix == 2:
        supprimerVehicule()
    elif choix == 3:
        modifierVehicule()
    elif choix == 4:
        afficherStatistiques()
    elif choix == 5:
        afficherVehicules()
    elif choix == 6:
        rechercherVehicule()
    elif choix == 0:
        print("Au revoir !")
    else:
        print("Choix invalide. Veuillez réessayer.")
