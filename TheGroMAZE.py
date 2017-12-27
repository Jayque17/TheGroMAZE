from upemtk import *
from time import sleep


print ("Hello World")

labyrinthe=[
	["*","*","*","*"],
	["*","@","*","*"],
	["*",".",".","*"],
	["*","*","X","*"]
]

def bas():
	for i in range(len(labyrinthe)):
		x = labyrinthe[i]
		for a in range(len(x)):
			if x[a] == "@":
				if labyrinthe[i+1][a] == "*":
					return
				else:
					labyrinthe[i+1][a] = "@"
					x[a] = "."
					return

def droite():
	for i in range(len(labyrinthe)):
		for a in range(len(labyrinthe[i])):
			if labyrinthe[i][a] == "@":
				if labyrinthe[i][a+1] == "*":
					return
				else:
					labyrinthe[i][a+1] = "@"
					labyrinthe[i][a] = "."
					return

def gauche():
	for i in range(len(labyrinthe)):
		for a in range(len(labyrinthe[i])):
			if labyrinthe[i][a] =="@":
				if labyrinthe[i][a-1] == "*":
					return
				else:
					labyrinthe[i][a-1] = "@"
					labyrinthe[i][a] = "."
					return

def haut():
	for i in range(len(labyrinthe)):
		for a in range(len(labyrinthe[i])):
			if labyrinthe[i][a] == "@":
				if labyrinthe[i-1][a] =="*":
					return
				else:
					labyrinthe[i-1][a] = "@"
					labyrinthe[i][a] = "."
					return



cree_fenetre(800,600)

framerate = 5

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
			bas()
		elif touche(ev) == "Right":
			droite()
		elif touche(ev) == "Left":
			gauche()
		elif touche(ev) == "Up":
			haut()
		elif touche(ev) == "Escape":
			break
	sleep(1 / framerate)

ferme_fenetre()