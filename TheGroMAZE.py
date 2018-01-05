from upemtk import *
from time import sleep

""" Fonctions """


""" Lecture du fichier texte où est le labyrinthe """

def lire_laby(nom_de_fichier):
    laby = open(nom_de_fichier,"r")
    lignes = laby.readlines()
    liste=[] 
    for i in lignes :
        l=[]
        for a in i:
            if a != "\n":
                l.append(a)
        liste.append(l)
    laby.close()
    return liste


""" Gestion des mouvements du personnage """

def bas(position_x, position_y):
    print (position_y,position_x)
    if labyrinthe[position_y+1][position_x] == "*":
        return (False, position_x, position_y)
    elif labyrinthe[position_y+1][position_x] == ".":
        labyrinthe[position_y+1][position_x] = "@"
        labyrinthe[position_y][position_x]  = "."
        return (False, position_x, position_y + 1)
    elif labyrinthe[position_y+1][position_x] == "X":
        labyrinthe[position_y+1][position_x] = "@"
        labyrinthe[position_y][position_x] = "."
        return (True, position_x, position_y + 1)


def droite(position_x, position_y):
    print (position_y,position_x)
    if labyrinthe[position_y][position_x+1] == "*":
        return (False, position_x, position_y)
    elif labyrinthe[position_y][position_x+1] == ".":
        labyrinthe[position_y][position_x+1] = "@"
        labyrinthe[position_y][position_x] = "."
        return (False, position_x + 1, position_y)
    elif labyrinthe[position_y][position_x+1] == "X":
        labyrinthe[position_y][position_x+1]= "@"
        labyrinthe[position_y][position_x] = "."
        return (True, position_x + 1, position_y)


def gauche(position_x, position_y):
    print (position_y,position_x)
    if labyrinthe[position_y][position_x-1] == "*":
        return (False, position_x, position_y)
    elif labyrinthe[position_y][position_x-1] == ".":
        labyrinthe[position_y][position_x-1] = "@"
        labyrinthe[position_y][position_x] = "."
        return (False, position_x - 1, position_y)
    elif labyrinthe[position_y][position_x-1] == "X":
        labyrinthe[position_y][position_x-1]= "@"
        labyrinthe[position_y][position_x] = "."
        return (True, position_x - 1, position_y)
	

def haut(position_x, position_y):
    print (position_y,position_x)
    if labyrinthe[position_y-1][position_x] == "*":
        return (False, position_x, position_y)
    elif labyrinthe[position_y-1][position_x] == ".":
        labyrinthe[position_y-1][position_x] = "@"
        labyrinthe[position_y][position_x]  = "."
        return (False, position_x, position_y - 1)
    elif labyrinthe[position_y-1][position_x] == "X":
        labyrinthe[position_y-1][position_x] = "@"
        labyrinthe[position_y][position_x] = "."
        return (True, position_x, position_y - 1)


""" Affichage du labyrinthe dans la console pour qu'il soit plus lisible """

def laby_console():
    for i in range(len(labyrinthe)):
        print(labyrinthe[i])


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


def affiche_perso2d(position_x, position_y):
    L = 25
    l = 25
    dx = 37.5
    dy = 37.5
    cercle(x = position_x*L + dx, y = position_y*l + dy, r = 10, remplissage = 'green')


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
    polygone([(0,0),(400,0),(400,300),(0,300)], couleur = "white", remplissage = 'white')


def affiche_mur_de_face(position_x, position_y):
    if labyrinthe[position_y+1][position_x] == "*":
        polygone([(50,50), (350,50), (350,250), (50,250)], remplissage = 'grey')


def affiche_mur_a_gauche_en_face(position_x, position_y):
    if labyrinthe[position_y+1][position_x] == "*" and labyrinthe[position_y+1][position_x+1] == "*" and labyrinthe[position_y][position_x+1] != "*" \
    or labyrinthe[position_y+1][position_x] == "." and labyrinthe[position_y+1][position_x+1] == "*":
        polygone([(0,50), (50,50), (50,250), (0,250)], remplissage = 'grey')


def affiche_mur_a_droite_en_face(position_x, position_y):
    if labyrinthe[position_y+1][position_x] == "*" and labyrinthe[position_y+1][position_x-1] == "*" and labyrinthe[position_y][position_x-1] != "*"\
    or labyrinthe[position_y+1][position_x] == "." and labyrinthe[position_y+1][position_x-1] == "*":
        polygone([(350,50), (400,50), (400,250), (350,250)], remplissage = 'grey')


def affiche_mur_a_gauche(position_x, position_y):
    if labyrinthe[position_y][position_x+1] == "*":
        polygone([(0,0),(50,50),(50,250),(0,300)], remplissage = 'grey')
    if labyrinthe[position_y+1][position_x+1] == "*":
        polygone([(50,50),(100,100),(100,200),(50,250)], remplissage = 'grey')
    if labyrinthe[position_y+1][position_x] == "*" and labyrinthe[position_y+1][position_x+1] == ".":
        polygone([(0,100),(50,50),(50,250),(0,200)], remplissage = 'grey')

        
def affiche_mur_a_droite(position_x, position_y):
    if labyrinthe[position_y][position_x-1] == "*":
        polygone([(350,50),(400,0),(400,300),(350,250)], remplissage = 'grey')
    if labyrinthe[position_y+1][position_x-1] == "*":
        polygone([(300,100),(350,50),(350,250),(300,200)], remplissage = 'grey')
    if labyrinthe[position_y+1][position_x] == "*" and labyrinthe[position_y+1][position_x-1] == ".":
        polygone([(350,50),(400,100),(400,200),(350,250)], remplissage = 'grey')
        


""" Jeu """


""" Initialisation du jeu """

cree_fenetre(400, 300)

framerate = 50

win = False

labyrinthe = lire_laby("labyrinthe.txt")


""" Création de variables prenant en compte la position du personnage et qui évitent de répéter cette boucle dans les fonctions """

for i in range(len(labyrinthe)):
    for a in range(len(labyrinthe[i])):
            if labyrinthe[i][a] == "@":
                position_y = i
                position_x = a


""" Affichage du labyrinthe dans la console """

laby_console()


""" Boucle principale """

while True:

   
    """ Affichage des objets """

    #affiche_mur2d()
    #ffiche_perso2d(position_x, position_y)
    #affiche_chemin2d()
    #affiche_sortie2d()
    affiche_vide()
    affiche_mur_a_gauche_en_face(position_x, position_y)
    affiche_mur_a_droite_en_face(position_x, position_y)
    affiche_mur_a_gauche(position_x, position_y)
    affiche_mur_a_droite(position_x, position_y)
    affiche_mur_de_face(position_x, position_y)
    mise_a_jour()


    """ Gestion des évènements """

    ev = donne_evenement()
    ty = type_evenement(ev)
    if ty == 'Quitte':
        break
    elif ty == "Touche":
        print(touche(ev))

        if touche(ev) == "Down" or touche(ev) == "z" :
            win, position_x, position_y = bas(position_x, position_y)
            print(win)
            laby_console()

        elif touche(ev) == "Right" or touche(ev) == "q" :
            win, position_x, position_y = droite(position_x, position_y)
            print(win)
            laby_console()

        elif touche(ev) == "Left" or touche(ev) == "d" :
            win, position_x, position_y = gauche(position_x, position_y)
            print(win)
            laby_console()

        elif touche(ev) == "Up" or touche(ev) == "s" :
            win, position_x, position_y = haut(position_x, position_y)
            print(win)
            laby_console()

        elif touche(ev) == "Escape":
            break
        
        if win == True:
            print("win")
            laby_console()
            break


    """ Attente avant rafraîchissement """

    sleep(1 / framerate)


    """ Fermeture et sortie """

ferme_fenetre()