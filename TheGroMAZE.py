from upemtk import *
from time import sleep


print ("Hello World")

labyrinthe=[
	["*","*","*","*"],
	["*","@","*","*"],
	["*",".",".","*"],
	["*","*","X","*"]
]

def bouger():
	for i in range(len(labyrinthe)):
		x = labyrinthe[i]
		for a in range(len(x)):
			if x[a] == "@":
				x[a] = "."
				labyrinthe[i+1][a] = "@"
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
			bouger()
		elif touche(ev) == "Escape":
			break
	sleep(1 / framerate)

ferme_fenetre()