#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

#define MAX_VEHICULES 100


typedef struct {
    char marque[50];
    char modele[50];
    int annee;
    char couleur[20];
    float kilometrage;
    char carburant[20];
    char type[20];
} Vehicule;


Vehicule vehicules[MAX_VEHICULES];
int nbVehicules = 0;


void ajouterVehicule();
void supprimerVehicule();
void modifierVehicule();
void afficherStatistiques();
void afficherVehicules();
void rechercherVehicule();

int main() {
    int choix;

    do {
        printf("     Application de gestion des véhicules   \n");
        printf("1. Ajouter un véhicule\n");
        printf("2. Supprimer un véhicule\n");
        printf("3. Modifier un véhicule\n");
        printf("4. Afficher les statistiques\n");
        printf("5. Afficher la liste des véhicules\n");
        printf("6. Rechercher un véhicule\n");
        printf("0. Quitter\n");
        printf("Votre choix : ");
        scanf("%d", &choix);

        switch (choix) {
            case 1:
                ajouterVehicule();
                break;
            case 2:
                supprimerVehicule();
                break;
            case 3:
                modifierVehicule();
                break;
            case 4:
                afficherStatistiques();
                break;
            case 5:
                afficherVehicules();
                break;
            case 6:
                rechercherVehicule();
                break;
            case 0:
                printf("Au revoir !\n");
                break;
            default:
                printf("Choix invalide. Veuillez réessayer.\n");
                break;
        }
    } while (choix != 0);

    return 0;
}


void ajouterVehicule() {
    if (nbVehicules >= MAX_VEHICULES) {
        printf("Impossible d'ajouter un véhicule. Le nombre maximal de véhicules a été atteint.\n");
        return;
    }

    Vehicule v;

    printf("Ajout d'un véhicule\n");
    printf("Marque : ");
    scanf("%s", v.marque);
    printf("Modèle : ");
    scanf("%s", v.modele);
    printf("Année : ");
    scanf("%d", &v.annee);
    printf("Couleur : ");
    scanf("%s", v.couleur);
    printf("Kilométrage : ");
    scanf("%f", &v.kilometrage);
    printf("Carburant : ");
    scanf("%s", v.carburant);
    printf("Type de véhicule : ");
    scanf("%s", v.type);

    vehicules[nbVehicules] = v;
    nbVehicules++;

    printf("Véhicule ajouté avec succès.\n");
}

void supprimerVehicule() {
    if (nbVehicules == 0) {
        printf("Aucun véhicule enregistré.\n");
        return;
    }

    int i, num;

    printf("Suppression d'un véhicule\n");
    printf("Numéro du véhicule à supprimer (1-%d) : ", nbVehicules);
    scanf("%d", &num);

    if (num < 1 || num > nbVehicules) {
        printf("Numéro de véhicule invalide.\n");
        return;
    }

    for (i = num - 1; i < nbVehicules - 1; i++) {
        vehicules[i] = vehicules[i + 1];
    }

    nbVehicules--;

    printf("Véhicule supprimé avec succès.\n");
}


void modifierVehicule() {
    if (nbVehicules == 0) {
        printf("Aucun véhicule enregistré.\n");
        return;
    }

    int i, num;

    printf("Modification d'un véhicule\n");
    printf("Numéro du véhicule à modifier (1-%d) : ", nbVehicules);
    scanf("%d", &num);

    if (num < 1 || num > nbVehicules) {
        printf("Numéro de véhicule invalide.\n");
        return;
    }

    Vehicule v = vehicules[num - 1];

    printf("Marque [%s] : ", v.marque);
    scanf("%s", v.marque);
    printf("Modèle [%s] : ", v.modele);
    scanf("%s", v.modele);
    printf("Année [%d] : ", v.annee);
    scanf("%d", &v.annee);
    printf("Couleur [%s] : ", v.couleur);
    scanf("%s", v.couleur);
    printf("Kilométrage [%.2f] : ", v.kilometrage);
    scanf("%f", &v.kilometrage);
    printf("Carburant [%s] : ", v.carburant);
    scanf("%s", v.carburant);
    printf("Type de véhicule [%s] : ", v.type);
    scanf("%s", v.type);

    vehicules[num - 1] = v;

    printf("Véhicule modifié avec succès.\n");
}


void afficherStatistiques() {
    if (nbVehicules == 0) {
        printf("Aucun véhicule enregistré.\n");
        return;
    }

    int i;
    int nbVoituresNoires = 0;
    int nbVoituresBlanches = 0;
    int nbTypesVehicules = 0;
    int nbVoituresEssence = 0;
    int nbVoituresDiesel = 0;
    int nbVoituresElectriques = 0;

    for (i = 0; i < nbVehicules; i++) {
        if (strcmp(vehicules[i].couleur, "noir") == 0) {
            nbVoituresNoires++;
        }

        if (strcmp(vehicules[i].couleur, "blanc") == 0) {
            nbVoituresBlanches++;
        }

        if (strcmp(vehicules[i].carburant, "essence") == 0) {
            nbVoituresEssence++;
        }

        if (strcmp(vehicules[i].carburant, "diesel") == 0) {
            nbVoituresDiesel++;
        }

        if (strcmp(vehicules[i].carburant, "électrique") == 0) {
            nbVoituresElectriques++;
        }

        int j;
        int estNouveauType = 1;

        for (j = 0; j < i; j++) {
            if (strcmp(vehicules[i].type, vehicules[j].type) == 0) {
                estNouveauType = 0;
                break;
            }
        }

        if (estNouveauType) {
            nbTypesVehicules++;
        }
    }

    printf("Statistiques\n");
    printf("Nombre de voitures noires : %d\n", nbVoituresNoires);
    printf("Nombre de voitures blanches : %d\n", nbVoituresBlanches);
    printf("Nombre de types de véhicules : %d\n", nbTypesVehicules);
    printf("Nombre de voitures essence : %d\n", nbVoituresEssence);
    printf("Nombre de voitures diesel : %d\n", nbVoituresDiesel);
    printf("Nombre de voitures électriques : %d\n", nbVoituresElectriques);
}


void afficherVehicules() {
    if (nbVehicules == 0) {
        printf("Aucun véhicule enregistré.\n");
        return;
    }

    int i;

    printf("Liste des véhicules\n");

    for (i = 0; i < nbVehicules; i++) {
        printf("Véhicule %d\n", i + 1);
        printf("Marque : %s\n", vehicules[i].marque);
        printf("Modèle : %s\n", vehicules[i].modele);
        printf("Année : %d\n", vehicules[i].annee);
        printf("Couleur : %s\n", vehicules[i].couleur);
        printf("Kilométrage : %.2f\n", vehicules[i].kilometrage);
        printf("Carburant : %s\n", vehicules[i].carburant);
        printf("Type de véhicule : %s\n", vehicules[i].type);
        printf("\n");
    }
}


void rechercherVehicule() {
    if (nbVehicules == 0) {
        printf("Aucun véhicule enregistré.\n");
        return;
    }

    char critere[50];
    int i, trouve = 0;

    printf("Recherche d'un véhicule\n");
    printf("Critère de recherche : ");
    scanf("%s", critere);

    for (i = 0; i < nbVehicules; i++) {
        if (strcmp(critere, vehicules[i].marque) == 0 ||
            strcmp(critere, vehicules[i].couleur) == 0 ||
            strcmp(critere, vehicules[i].type) == 0) {
            printf("Véhicule %d\n", i + 1);
            printf("Marque : %s\n", vehicules[i].marque);
            printf("Modèle : %s\n", vehicules[i].modele);
            printf("Année : %d\n", vehicules[i].annee);
            printf("Couleur : %s\n", vehicules[i].couleur);
            printf("Kilométrage : %.2f\n", vehicules[i].kilometrage);
            printf("Carburant : %s\n", vehicules[i].carburant);
            printf("Type de véhicule : %s\n", vehicules[i].type);
            printf("\n");
            trouve = 1;
        }
    }

    if (!trouve) {
        printf("Aucun véhicule correspondant au critère de recherche.\n");
    }
}
