from BoardGame import *
from Joueur import *



class Jeu:

    def __init__(self,t,n):
        self.taillegrille=t
        self.nombrejoueurs=n


def jeu():
    print("INITIALISATION \n")
    taille_grille= input("taille de la grille :")
    taille_grille=int(taille_grille)
    nbre_joueurs= input("Nombre de joueurs :\n")
    nbre_joueurs=int(nbre_joueurs)
    joueurs=[Player for k in range(nbre_joueurs)]
    k=0
    for j in joueurs:
        k+=1
        j.nom=input('Nom joueur '+str(k)+' :')
        IA=input('Ordi (y ou n):')
        if IA=="y":
            j.type_is_IA=True
        print("ACTIONS \n")
        position=input("Positions (y ou n) :")
        if position=="y":
            j.action=position
            coordonées=input("1D ou 2D (1 ou 2) :")
        deplacement=input("deplacement (y ou n) :")
        if deplacement=="y":
            j.action=deplacement
            fusion=input("fusion (y ou n) :")













