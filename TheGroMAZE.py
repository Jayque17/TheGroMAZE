from upemtk import *


print ("Hello World")

cree_fenetre(800,600)

while True:

	mise_a_jour()
	ev = donne_evenement()
	ty = type_evenement(ev)
	if ty == 'Quitte':
		break

ferme_fenetre()