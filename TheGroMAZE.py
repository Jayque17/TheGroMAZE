from upemtk import *
from time import sleep


print ("Hello World")

labyrinthe=[
	["*","*","*","*"],
	["*","@","*","*"],
	["*",".",".","*"],
	["*","*","X","*"]
]

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

def bas():
	for i in range(len(labyrinthe)):
		for a in range(len(labyrinthe[i])):
			if labyrinthe[i][a] == "@":
				if labyrinthe[i+1][a] == "*":
					return False
				elif labyrinthe[i+1][a] == ".":
					labyrinthe[i+1][a] = "@"
					labyrinthe[i][a]  = "."
					return False
				elif labyrinthe[i+1][a] == "X":
					labyrinthe[i+1][a] = "@"
					labyrinthe[i][a] = "."
					return True

def droite():
	for i in range(len(labyrinthe)):
		for a in range(len(labyrinthe[i])):
			if labyrinthe[i][a] == "@":
				if labyrinthe[i][a+1] == "*":
					return False
				elif labyrinthe[i][a+1] == ".":
					labyrinthe[i][a+1] = "@"
					labyrinthe[i][a] = "."
					return False
				elif labyrinthe[i][a+1] == "X":
					labyrinthe[i][a+1] = "@"
					labyrinthe[i][a] = "."
					return True

def gauche():
	for i in range(len(labyrinthe)):
		for a in range(len(labyrinthe[i])):
			if labyrinthe[i][a] =="@":
				if labyrinthe[i][a-1] == "*":
					return False
				elif labyrinthe[i][a-1] == ".":
					labyrinthe[i][a-1] = "@"
					labyrinthe[i][a] = "."
					return False
				elif labyrinthe[i][a-1] == "X":
					labyrinthe[i][a-1] = "@"
					labyrinthe[i][a] = "."
					return True

def haut():
	for i in range(len(labyrinthe)):
		for a in range(len(labyrinthe[i])):
			if labyrinthe[i][a] == "@":
				if labyrinthe[i-1][a] == "*":
					return False
				elif labyrinthe[i-1][a] == ".":
					labyrinthe[i-1][a] = "@"
					labyrinthe[i][a] = "."
					return False
				elif labyrinthe[i-1][a] == "X":
					labyrinthe[i-1][a] = "@"
					labyrinthe[i][a] = "."
					return True


cree_fenetre(800,600)

framerate = 5
win = False

labyrinthe = lire_laby("labyrinthe.txt")

while True:
	print(labyrinthe)
	mise_a_jour()
	ev = donne_evenement()
	ty = type_evenement(ev)
	if ty == 'Quitte':
		break
	elif ty == "Touche":
		print(touche(ev))

		if touche(ev) == "Down":
			win = bas()
		elif touche(ev) == "Right":
			win = droite()
		elif touche(ev) == "Left":
			win = gauche()
		elif touche(ev) == "Up":
			win = haut()
		elif touche(ev) == "Escape":
			break
		
		if win == True:
			print("win")
			print(labyrinthe)
			break
	sleep(1 / framerate)

ferme_fenetre()