from upemtk import *
from time import sleep



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

def laby_console():
    for i in range(len(labyrinthe)):
        print(labyrinthe[i])


def affiche_mur():
    L = 25
    l = 25
    dx = 25
    dy = 25
    for i in range(len(labyrinthe)):
        for a in range(len(labyrinthe[i])):
            if labyrinthe[i][a] == "*":
                rectangle(ax = a*L + dx, ay = i*l + dy, bx = (a + 1)*L + dx, by = (i + 1)*l + dy, remplissage = 'grey')

def affiche_perso():
    dx = 25
    dy = 25
    for i in range(len(labyrinthe)):
        for a in range(len(labyrinthe)):
            cercle(x = a + dx, y = i + dy, r = 10, remplissage='green')




cree_fenetre(400,300)

framerate = 5
win = False

labyrinthe = lire_laby("labyrinthe.txt")

for i in range(len(labyrinthe)):
    for a in range(len(labyrinthe[i])):
            if labyrinthe[i][a] == "@":
                position_y = i
                position_x = a

laby_console()

while True:
    affiche_mur()
    affiche_perso()
    mise_a_jour()
    ev = donne_evenement()
    ty = type_evenement(ev)
    if ty == 'Quitte':
        break
    elif ty == "Touche":
        print(touche(ev))

        if touche(ev) == "Down":
            win, position_x, position_y = bas(position_x, position_y)
            print(win)
            laby_console()

        elif touche(ev) == "Right":
            win, position_x, position_y = droite(position_x, position_y)
            print(win)
            laby_console()

        elif touche(ev) == "Left":
            win, position_x, position_y = gauche(position_x, position_y)
            print(win)
            laby_console()

        elif touche(ev) == "Up":
            win, position_x, position_y = haut(position_x, position_y)
            print(win)
            laby_console()

        elif touche(ev) == "Escape":
            break
        
        if win == True:
            print("win")
            laby_console()
            break

    sleep(1 / framerate)

ferme_fenetre()