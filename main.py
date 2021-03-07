from CONFIGS import *

from math import *

import turtle

def lire_matrice(fichierTexteDuPlan):
    """
    Cette fonction crée une matrice représentant le plan de jeu en analysant les lignes du fichier texte de plan.
    :param fichierTexteDuPlan: nom du fichier texte contenant le plan
    :return: liste
    """
    matrice = []

    with open(fichierTexteDuPlan, "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            matrice.append(ligne.split())

    return matrice

def calculer_pas(matrice):
    """
    calcule la dimension à donner aux cases pour que le plan tienne dans la zone de la fenêtre turtle que vous avez
    définie : diviser la largeur et la hauteur de la zone en question par le nombre de cases qu’elle doit accueillir,
    retenir la plus faible de ces deux valeurs.
    :param matrice: matrice de jeu
    :return: valeur de pas pour l'affichage des cases
    """
    # récupération des abscisses et ordonnées des limites du plan du château
    abscisse_mini_plan, ordonnee_mini_plan = ZONE_PLAN_MINI
    abscisse_maxi_plan, ordonnee_maxi_plan = ZONE_PLAN_MAXI

    # détermination de la valeur de pas horizontal
    valeur_pas_horizontal = (abscisse_maxi_plan - abscisse_mini_plan) / len(matrice[0])
    print(len(matrice[0]))

    # détermination de la valeur de pas vertical
    valeur_pas_vertical = (ordonnee_maxi_plan - ordonnee_mini_plan) / len(matrice)

    # renvoi de la valeur de pas la plus petite
    print("le pas est de : ", floor(min(valeur_pas_vertical, valeur_pas_horizontal)))
    return floor(min(valeur_pas_vertical, valeur_pas_horizontal))

def coordonnees(case, pas, matrice):
    """
    calcule les coordonnées en pixels turtle du coin inférieur gauche d’une case définie par ses coordonnées
    (numéros de ligne et de colonne).
    :param case: la case en question
    :param pas: le pas calculé par la fonction calculer_pas(m)
    :return: les coordonnées x (abscisse) et y (ordonnée) en pixels turtle du coin inférieur gauche de la case
    """
    #initialisation des variables qui seront retournées
    x = 0
    y = 0

    # récupération des indices de la case
    a, b = case

    # récupération des abscisses et ordonnées des limites du plan du château
    abscisse_mini_plan, ordonnee_mini_plan = ZONE_PLAN_MINI

    # calcul de l'abscisse x
    x = abscisse_mini_plan + b * pas

    # calcul de l'ordonnée y
    y = ordonnee_mini_plan + (len(matrice) - 1 - a) * pas

    return(x , y)

def tracer_carre(dimension):
    """
    cette fonction trace un carré en fonction de la longueur d'un côté
    :param dimension: longueur d'un côté
    :return: None
    """
    # Initialisation du dessinateur
    #tur = turtle.Turtle()

    # Début de la boucle
    for i in range(4):  # la boucle va tourner 4 fois
        turtle.forward(dimension)  # Avance le dessinateur de "dimension" pas en avant
        turtle.left(90)  # Rotation du dessinateur de 90 degrés
    return

def tracer_case(case, couleur, pas, matrice):
    """
    Cette fonction trace une case
    :param case: (indice de ligne, indice de colonne)
    :param couleur: couleur de remplissage de la case
    :param pas: dimension d'un côté d'une case
    :param matrice: matrice générée à partir du fichier texte de plan
    :return: None
    """
    # on définit les couleurs de tracé et de remplissage
    turtle.color("black", couleur)

    # lève le crayon
    turtle.up()

    # détermine la position de démarrage du tracé de la case
    turtle.setpos(coordonnees(case, pas, matrice))

    # baisse le crayon, trace le carré et le remplit
    turtle.down()
    turtle.begin_fill()
    tracer_carre(pas)
    turtle.end_fill()
    return


def afficher_plan(matrice):
    """
    pour chaque élément ligne de la matrice, pour chaque élément colonne de cet élément ligne, tracer une case à
    l’emplacement correspondant, dans une couleur correspondant à ce que donne la matrice.
    :param matrice: matrice générée à partir du fichier texte de plan
    :return: None
    """
    # on choisit la vitesse d'affichage la plus rapide
    turtle.speed(0)

    # pour chaque élément ligne de la matrice, pour chaque élément colonne de cet élément ligne, tracer une case à
    # l’emplacement correspondant, dans une couleur correspondant à ce que donne la matrice.
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            color = COULEURS[int(matrice[i][j])]
            tracer_case((i,j),color, calculer_pas(matrice),matrice )

    turtle.hideturtle()
    turtle.done()


    return

# afficher_plan(lire_matrice("plan_chateau.txt"))

afficher_plan(lire_matrice("planbasique.txt"))
