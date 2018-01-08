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


def affiche_mur_en_face(position_x, position_y):
    n = 0
    while labyrinthe[position_y+n][position_x] != "*":
        n += 1
        
        if labyrinthe[position_y+n][position_x] == "*":
            polygone([(25 + 25 * n/2, 20 + 18.75 * n/2), (375 - 25 * n/2, 20 + 18.75 * n/2),\
             (375 - 25 * n/2, 280 - 18.75 * n/2), (25 + 25 * n/2, 280 - 18.75 * n/2)], remplissage = 'grey')

        elif labyrinthe[position_y+n][position_x] == "X":
            polygone([(25 + 25 * n/2, 20 + 18.75 * n/2), (375 - 25 * n/2, 20 + 18.75 * n/2),\
             (375 - 25 * n/2, 280 - 18.75 * n/2), (25 + 25 * n/2, 280 - 18.75 * n/2)], couleur = 'white', remplissage = 'white')
            break
        else:
            pass


def affiche_mur_a_gauche_en_face(position_x, position_y):
    n = 0
    while labyrinthe[position_y+n][position_x+1] != "*":
        n += 1
        if labyrinthe[position_y+n][position_x+1] == "*":
            polygone([(0, 20 + 18.75 * n/2 ),(25 + 25 * n/2, 20 + 18.75 * n/2),\
                (25 + 25 * n/2, 280 - 18.75 * n/2),(0, 280 - 18.75 * n/2 )], remplissage = 'grey')

        elif labyrinthe[position_y+n][position_x+1] == "X":
            polygone([(0, 20 + 18.75 * n/2 ),(25 + 25 * n/2, 20 + 18.75 * n/2),\
                (25 + 25 * n/2, 280 - 18.75 * n/2),(0, 280 - 18.75 * n/2 )], couleur = 'white', remplissage = 'white')
            break

        else :
            pass

def affiche_mur_a_droite_en_face(position_x, position_y):
    n = 0
    while labyrinthe[position_y+n][position_x-1] != "*":
        n += 1
        if labyrinthe[position_y+n][position_x-1] == "*":
            polygone([(375 - 25 * n/2, 20 + 18.75 * n/2),(400, 20 + 18.75 * n/2),\
                (400,  280 - 18.75 * n/2),(375 - 25 * n/2,  280 - 18.75 * n/2)], remplissage = 'grey')

        elif labyrinthe[position_y+n][position_x-1] == "X":
            polygone([(375 - 25 * n/2, 20 + 18.75 * n/2),(400, 20 + 18.75 * n/2),\
                (400,  280 - 18.75 * n/2),(375 - 25 * n/2,  280 - 18.75 * n/2)], couleur = 'white', remplissage = 'white')
            break
        
        else :
            pass




def affiche_mur_a_gauche(position_x, position_y):
    n = 0
    while labyrinthe[position_y+n][position_x] != "*":
        n += 1
        if labyrinthe[position_y][position_x+1] == "*":
            if labyrinthe[position_y+n][position_x+1] =="*":
                polygone([(0 , 0 ),(25 + 25*n, 18.75 + 18.75*n),(25 + 25*n, 281.25 - 18.75*n),(0 , 300 )])
            else:
                n -= 1
        else:
            pass
 

        
def affiche_mur_a_droite(position_x, position_y):
    n = 0
    while labyrinthe[position_y+n][position_x] != "*":
        n += 1
        if labyrinthe[position_y][position_x-1] == "*":
            if labyrinthe[position_y+n][position_x-1] =="*":
                polygone([( 375 - 25*n, 18.75 + 18.75*n),(400, 0),(400, 300),( 375 - 25*n , 281.25 - 18.75*n )])
            else:
                n -= 1
        else:
            pass

 



""" Jeu """


""" Initialisation du jeu """

fenetre = cree_fenetre(400, 300)

framerate = 10000

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
    #affiche_perso2d(position_x, position_y)
    #affiche_chemin2d()
    #affiche_sortie2d()
    
    affiche_vide()
    affiche_mur_a_gauche_en_face(position_x, position_y)
    affiche_mur_a_gauche(position_x, position_y)
    affiche_mur_a_droite_en_face(position_x, position_y)
    affiche_mur_a_droite(position_x, position_y)
    affiche_mur_en_face(position_x, position_y)
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