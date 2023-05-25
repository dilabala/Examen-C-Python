class Application:
    def __init__(self):
        self.name = "Mon application"

    def launch(self):
        print("L'application est lancée.")

    def use(self):
        print("Utilisation de l'application en cours.")

    def quit(self):
        print("L'application est quittée.")


class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age


class Etudiant(Personne):
    universite = "Mon université"

    def __init__(self, nom, prenom, age, niveau):
        super().__init__(nom, prenom, age)
        self.niveau = niveau

    def set_niveau(self, niveau):
        self.niveau = niveau

    def get_niveau(self):
        return self.niveau

    def augmenter_age(self):
        self.age += 1


class Professeur(Personne):
    universite = "Mon université"

    def __init__(self, nom, prenom, age, specialite):
        super().__init__(nom, prenom, age)
        self.specialite = specialite

    def set_specialite(self, specialite):
        self.specialite = specialite

    def get_specialite(self):
        return self.specialite

    def augmenter_age(self):
        self.age += 1


class Animal:
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece


class Chien(Animal):
    def __init__(self, nom, espece, race):
        super().__init__(nom, espece)
        self.race = race

    def set_race(self, race):
        self.race = race

    def get_race(self):
        return self.race


class Chat(Animal):
    def __init__(self, nom, espece, couleur):
        super().__init__(nom, espece)
        self.couleur = couleur

    def set_couleur(self, couleur):
        self.couleur = couleur

    def get_couleur(self):
        return self.couleur


# Exemple d'utilisation
if __name__ == '__main__':
    app = Application()
    app.launch()

    etudiant1 = Etudiant("Dupont", "Jean", 20, "Licence")
    etudiant2 = Etudiant("Durand", "Emma", 22, "Master")
    etudiant3 = Etudiant("Martin", "Luc", 19, "Licence")
    etudiant4 = Etudiant("Dubois", "Sophie", 21, "Master")
    etudiant5 = Etudiant("Lefevre", "Thomas", 18, "Licence")

    professeur1 = Professeur("Girard", "Marie", 45, "Mathématiques")
    professeur2 = Professeur("Leroy", "Pierre", 55, "Physique")
    professeur3 = Professeur("Moreau", "Isabelle", 50, "Chimie")
    professeur4 = Professeur("Roux", "François", 48, "Biologie")
    professeur5 = Professeur("Leclerc", "Caroline", 52, "Histoire")

    chien1 = Chien("Max", "Chien", "Labrador")
    chien2 = Chien("Milo", "Chien", "Berger allemand")
    chien3 = Chien("Bella", "Chien", "Bulldog")
    chien4 = Chien("Rocky", "Chien", "Golden Retriever")
    chien5 = Chien("Luna", "Chien", "Chihuahua")

    chat1 = Chat("Minou", "Chat", "Noir")
    chat2 = Chat("Félix", "Chat", "Roux")
    chat3 = Chat("Misty", "Chat", "Blanc")
    chat4 = Chat("Mia", "Chat", "Gris")
    chat5 = Chat("Oscar", "Chat", "Tigré")

    app.use()

    etudiant1.augmenter_age()
    professeur2.set_specialite("Informatique")
    chien3.set_race("Bouledogue français")
    chat4.set_couleur("Gris clair")

    app.quit()
