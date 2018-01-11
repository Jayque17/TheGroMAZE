from upemtk import *
from time import sleep

""" Fonctions """


""" Lecture du fichier texte où est le labyrinthe """

def lire_laby(nom_de_fichier):
    fichier_laby = open(nom_de_fichier,"r")
    lignes_fichier = fichier_laby.readlines()
    laby = [] 
    for ligne_fichier in lignes_fichier :
        ligne_laby = []
        for element in ligne_fichier:
            if element != "\n":
                ligne_laby.append(element)
        laby.append(ligne_laby)
    fichier_laby.close()
    return laby,len(laby[0]),len(laby)


""" Gestion des mouvements du personnage """

def initialise_position_personnage():
    for y in range(len(labyrinthe)):
        for x in range(len(labyrinthe[y])):
            if labyrinthe[y][x] == "@":
                return x, y



def bas(personnage_x, personnage_y):
    print (personnage_y,personnage_x)
    if labyrinthe[personnage_y+1][personnage_x] == "*":
        return (False, personnage_x, personnage_y)
    elif labyrinthe[personnage_y+1][personnage_x] == ".":
        labyrinthe[personnage_y+1][personnage_x] = "@"
        labyrinthe[personnage_y][personnage_x]  = "."
        return (False, personnage_x, personnage_y + 1)
    elif labyrinthe[personnage_y+1][personnage_x] == "X":
        labyrinthe[personnage_y+1][personnage_x] = "@"
        labyrinthe[personnage_y][personnage_x] = "."
        return (True, personnage_x, personnage_y + 1)


def droite(personnage_x, personnage_y):
    print (personnage_y,personnage_x)
    if labyrinthe[personnage_y][personnage_x+1] == "*":
        return (False, personnage_x, personnage_y)
    elif labyrinthe[personnage_y][personnage_x+1] == ".":
        labyrinthe[personnage_y][personnage_x+1] = "@"
        labyrinthe[personnage_y][personnage_x] = "."
        return (False, personnage_x + 1, personnage_y)
    elif labyrinthe[personnage_y][personnage_x+1] == "X":
        labyrinthe[personnage_y][personnage_x+1]= "@"
        labyrinthe[personnage_y][personnage_x] = "."
        return (True, personnage_x + 1, personnage_y)


def gauche(personnage_x, personnage_y):
    print (personnage_y,personnage_x)
    if labyrinthe[personnage_y][personnage_x-1] == "*":
        return (False, personnage_x, personnage_y)
    elif labyrinthe[personnage_y][personnage_x-1] == ".":
        labyrinthe[personnage_y][personnage_x-1] = "@"
        labyrinthe[personnage_y][personnage_x] = "."
        return (False, personnage_x - 1, personnage_y)
    elif labyrinthe[personnage_y][personnage_x-1] == "X":
        labyrinthe[personnage_y][personnage_x-1]= "@"
        labyrinthe[personnage_y][personnage_x] = "."
        return (True, personnage_x - 1, personnage_y)
	

def haut(personnage_x, personnage_y):
    print (personnage_y,personnage_x)
    if labyrinthe[personnage_y-1][personnage_x] == "*":
        return (False, personnage_x, personnage_y)
    elif labyrinthe[personnage_y-1][personnage_x] == ".":
        labyrinthe[personnage_y-1][personnage_x] = "@"
        labyrinthe[personnage_y][personnage_x]  = "."
        return (False, personnage_x, personnage_y - 1)
    elif labyrinthe[personnage_y-1][personnage_x] == "X":
        labyrinthe[personnage_y-1][personnage_x] = "@"
        labyrinthe[personnage_y][personnage_x] = "."
        return (True, personnage_x, personnage_y - 1)


""" Affichage du labyrinthe dans la console pour qu'il soit plus lisible """

def affiche_laby_console():
    for ligne_laby in labyrinthe:
        print(ligne_laby)


""" Affichage des éléments du labyrinthe en gaphique mais le labyrinthe est vu du dessus """

def affiche_mur2d():
    L = 25
    l = 25
    dx = 25
    dy = 25
    for i in range(len(labyrinthe)):
        for a in range(len(labyrinthe[i])):
            if labyrinthe[i][a] == "*":
                rectangle(ax = a*L + dx, ay = i*l + dy, bx = (a + 1)*L + dx, by = (i + 1)*l + dy, remplissage = 'grey')


def affiche_perso2d(personnage_x, personnage_y):
    L = 25
    l = 25
    dx = 37.5
    dy = 37.5
    cercle(x = personnage_x*L + dx, y = personnage_y*l + dy, r = 10, remplissage = 'green')


def affiche_chemin2d():
    L = 25
    l = 25
    dx = 25
    dy = 25
    for i in range(len(labyrinthe)):
        for a in range(len(labyrinthe[i])):
            if labyrinthe[i][a] == ".":
                rectangle(ax = a*L + dx, ay = i*l + dy, bx = (a + 1)*L + dx, by = (i + 1)*l + dy, remplissage = 'white')


def affiche_sortie2d():
    L = 25
    l = 25
    dx = 25
    dy = 25
    for i in range(len(labyrinthe)):
        for a in range(len(labyrinthe[i])):
            if labyrinthe[i][a] == "X":
                rectangle(ax = a*L + dx, ay = i*l + dy, bx = (a + 1)*L + dx, by = (i + 1)*l + dy, remplissage = 'red')


""" Affichage du labyrinthe en vue subjective """

def affiche_vide():
    efface_tout()


def affiche_mur_en_face(personnage_x, personnage_y):
    
    def affiche_mur(n, couleur):
         polygone([( 17.2 * n , 12.9 * n ),( 400 - 17.2 * n , 12.9 * n ),\
                ( 400 - 17.2 * n , 300 - 12.9 * n ),( 17.2 * n , 300 - 12.9 * n )], remplissage = couleur)
    
    for n in range( 1 , hauteur - personnage_y ):

        if labyrinthe[personnage_y+n][personnage_x] == "*":
            affiche_mur(n, 'grey')
            return

        elif labyrinthe[personnage_y+n][personnage_x] == "X":
            affiche_mur(n, 'green')
            return


def affiche_mur_en_face_a_gauche(personnage_x, personnage_y):

    def affiche_mur(n, couleur):
        polygone([( 0 , 12.9 * n ),( 17.2 * n , 12.9 * n ),\
                ( 17.2 * n , 300 - 12.9 * n ),( 0 , 300 - 12.9 * n )], remplissage = couleur )

    for y in reversed(range( personnage_y+1 , hauteur )):

        if labyrinthe[y][personnage_x+1] == "*":
            affiche_mur(y - personnage_y, 'grey')
            

        elif labyrinthe[y][personnage_x+1] == "X":
            affiche_mur(y - personnage_y, 'green')
            


def affiche_mur_en_face_a_droite(personnage_x, personnage_y):

    def affiche_mur(n, couleur):
        polygone([( 400 - 17.2 * n , 12.9 * n ),( 400 , 12.9 * n ),\
                ( 400 , 300 - 12.9 * n ),( 400 - 17.2 * n , 300 - 12.9 * n )], remplissage = couleur)

    for y in reversed(range( personnage_y+1 , hauteur )):

        if labyrinthe[y][personnage_x-1] == "*":
            affiche_mur(y - personnage_y, 'grey')
            

        elif labyrinthe[y][personnage_x-1] == "X":
            affiche_mur(y - personnage_y, 'green')
                

            
def affiche_mur_a_gauche(personnage_x,personnage_y):

    def affiche_mur(n, couleur):
        polygone([( 0 + 17.2 * n , 0 + 12.9 * n ),( 17.2 + 17.2 * n , 12.9 + 12.9 * n ),\
                ( 17.2 + 17.2 * n , 287.1 - 12.9 * n ),( 0 + 17.2 * n , 300 - 12.9 * n )], remplissage = couleur )

    for y in range(personnage_y , hauteur ):

        if labyrinthe[y][personnage_x+1] == "*":
            affiche_mur(y - personnage_y, 'grey')

        elif labyrinthe[y][personnage_x+1] == "X":
            affiche_mur(y - personnage_y, 'green')


def affiche_mur_a_droite(personnage_x, personnage_y):

    def affiche_mur(n, couleur):
        polygone([( 382.8 - 17.2 * n , 12.9 + 12.9 * n ),( 400 - 17.2 * n , 0 + 12.9 * n ),\
                ( 400 - 17.2 * n , 300 - 12.9 * n ),( 382.8 - 17.2 * n , 287.1 - 12.9 * n )], remplissage = couleur )

    for y in range(personnage_y , hauteur ):

        if labyrinthe[y][personnage_x-1] == "*":
            affiche_mur(y - personnage_y, 'grey')

        elif labyrinthe[y][personnage_x-1] == "X":
            affiche_mur(y - personnage_y, 'green')


""" Manipulation du labyrinthe """

def tourne_labyrinthe_a_gauche():

    labyrinthe_tourne = []

    for x in reversed(range(0, largeur )):
        
        ligne = []

        for y in range(0 , hauteur):
            ligne.append(labyrinthe[y][x])

        labyrinthe_tourne.append(ligne)

    return labyrinthe_tourne, hauteur, largeur


def tourne_labyrinthe_a_droite():

    labyrinthe_tourne = []

    for x in range(0, largeur ):
        
        ligne = []

        for y in reversed(range(0 , hauteur)):
            ligne.append(labyrinthe[y][x])

        labyrinthe_tourne.append(ligne)

    return labyrinthe_tourne, hauteur, largeur






""" Jeu """


""" Initialisation du jeu """

fenetre = cree_fenetre(400, 300)

framerate = 60

gagner = False

labyrinthe,largeur,hauteur = lire_laby("labyrinthe.txt")



""" Création de variables prenant en compte la position du personnage et qui évitent de répéter cette boucle dans les fonctions """

personnage_x, personnage_y = initialise_position_personnage()


""" Affichage du labyrinthe dans la console """

affiche_laby_console()


""" Boucle principale """

while True:

   
    """ Affichage des objets """

    #affiche_mur2d()
    #affiche_perso2d(personnage_x, personnage_y)
    #affiche_chemin2d()
    #affiche_sortie2d()
    
    affiche_vide()
    affiche_mur_en_face_a_gauche(personnage_x, personnage_y)
    affiche_mur_a_gauche(personnage_x, personnage_y)
    affiche_mur_en_face_a_droite(personnage_x, personnage_y)
    affiche_mur_a_droite(personnage_x, personnage_y)
    affiche_mur_en_face(personnage_x, personnage_y)
    mise_a_jour()


    """ Gestion des évènements """

    ev = donne_evenement()
    ty = type_evenement(ev)
    if ty == 'Quitte':
        break
    elif ty == "Touche":
        print(touche(ev))

        if touche(ev) == "Down" or touche(ev) == "z" :
            gagner, personnage_x, personnage_y = bas(personnage_x, personnage_y)
            print(gagner)
            affiche_laby_console()

        elif touche(ev) == "Right" or touche(ev) == "q" :
            gagner, personnage_x, personnage_y = droite(personnage_x, personnage_y)
            print(gagner)
            affiche_laby_console()

        elif touche(ev) == "Left" or touche(ev) == "d" :
            gagner, personnage_x, personnage_y = gauche(personnage_x, personnage_y)
            print(gagner)
            affiche_laby_console()

        elif touche(ev) == "Up" or touche(ev) == "s" :
            gagner, personnage_x, personnage_y = haut(personnage_x, personnage_y)
            print(gagner)
            affiche_laby_console()

        elif touche(ev) == "Escape":
            break

        elif touche(ev) == "e":
            
            labyrinthe, largeur, hauteur = tourne_labyrinthe_a_gauche()
            personnage_x, personnage_y = initialise_position_personnage()
            affiche_laby_console()

        elif touche(ev) == "a":

            labyrinthe, largeur, hauteur = tourne_labyrinthe_a_droite()
            personnage_x, personnage_y = initialise_position_personnage()
            affiche_laby_console()

        if gagner == True:
            print("gagner")
            affiche_laby_console()
            break


    """ Attente avant rafraîchissement """

    sleep(1 / framerate)


    """ Fermeture et sortie """

ferme_fenetre()