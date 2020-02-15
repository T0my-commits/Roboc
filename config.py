... fichiers ... 

fonctions :

 |- retrouver_carte() : charger les cartes, les parties inachevées
 |- selection_partie() : sélectionner le niveau
 |- enregistrer() : sérialiser des objets
 |- unpickler() : désérialiser des objets
 |- déplacements() : défini les déplacements effectués par le joueur dans le
 |  labyrinthe
 |- pivotement() : interprête les indications de déplacements que le joueur à
 |  indiqué
 |- afficher_labyrinthe() : affiche le labyrinthe
 |- partie() : défini la variable <parties>, initialement <dictionnaire>
 |- checkhorizontal() : système de déplacements horizontal
 |- checkvertical() : système de déplacements vertical
 |- etc.

variables :

 |- parties : tuple() -- défini la partie en cours
0|- cartes : DictionnaireOrdonné() -- enregistre les cartes initiales
0|- append : dict() -- enregistre les cartes initiales
0|- selection : str() -- défini le choix de la carte par le joueur
 |- etc.

dictionnaires :

 |- scores : {nom_carte:score}
0|- parties : {nom_carte:contenu_carte}
0|- etc.

// <parties> et <scores> régies par un décorateur @sigleton.
/// <parties> est le double de <cartes> qui se modifie.

listes :

 |- relations_humaines : dialogues <?> (10)
 |- centres_interets : goodies <!> (6)
0|- etc.

classes :

0|- DictionnaireOrdonné() : dictionnaire ordonné
0|- CartesClass() : attributs des cartes <murs>, <portes>, <centres_interets>, etc.
 |- PersoClass() : attributs de notre personnage <systeme de déplacement>, <apparence>, etc.
0|- etc.


... syntaxe test ...

import os
os.chdir('C:/Users/moi/Documents/Projet Python/Roboc')
from elements import *
retrouver_carte()


... répertoire jeu ...

C:/Users/moi/Documents/Projet Python/Roboc


... cartes ...

# La grotte oubliée :

#####################
0 . //. . . . .## . >>>
# . ######### .## . #
# . ##. . . . .## . #
# ! ##. ### .#### . #
# . ##. # # . ### . #
# . . . # # ? .## . #
##### . ### . ### . #
# . ! . //. . . . . #
#####################

# L'émission télé :

##########################
# . ### .! . . . . . . . #
# . # # . ## . ## ? ## . #
# . ### . ## . ## . // . #
# . . . . // . ####### . #
# . ######## . . . .######
0 . ## . . . . ####### . #
# . ## . ####### . . # . #
# . ## ? . . . . . ### . >>>
# . ###########//##### ! #
# . . . ### . . . . // . #
##########################

# Le Bloc

#################################################
## . . . . . . . . . . ? . . . . . . . . . . . ##
## . ############################# . ####### . ##
## ! ## . . . . . . . . . . . . ## . ## . ## . ##
## . ## . ################### . ## . ## . ## . ##
## . ## . ## . . . . . . . ## . ## . ## . ## . ##
## . ## . ## . ############## . ## . ## . ## . ##
## . ## . ## . ## . . . . . . . ## . ## ? ## . ##
## . ## . ## . // . ######### . ## . ## . ## . ##
## . ## . ## . ## . ##     ## . ## . ## . ## . ##
## . ## . ## . ## . ##     ## . ## . ## . ## . ##
## . ## . ## . ## . ##     ## . ## . ## . ## . ##
## . ## ? ## . ## . ######### . ## . ## . ## . ##
## . ## . ## . ## . . ! . . . . ## . ## . ## . ##
## . ## . ## . ## . ######### . ## ? ## . ## . ##
## . ## . ## . ## . ##  0 . . . ## . ## . ## . ##
## . .  . ## ? ## . ############## . ## . ## . ##
## . ## . ## . ## . ## . . . . . . . .  . // . ##
## . ## . ## . ########//############## ! ## . ##
## ? ## . ## . . . . . . . . ! . . . ## ! ## ? ##
####################################### ! #######
                                        >>>

"""

##############################################
## . // . . . . .## .  . ! ##. ! .// . . #####
## . ## . ####. .## . ## . ########### . . ?>>>
## . ## . ####. .## . ## . ## .  . .## . #####
## . ## . ##! . .## . ## . ## . ## . . .  . ##
## . ## . ##. .#### . ## . ## . ##########. ##
## ! ## . ##. . .## . ## . ## . . . ? . ##. ##
## . ## . ####. .## . ## . ## . ##########. ##
## . ## . ##. ? .## . ## .  . . ## . . .  . ##
## . ## . ##. .#### . ############ .## . #####
## . ## . ##. . . . . ##.  . . ##. .## .  . ##
## . ## . ####//########. ## . ##. .##### . ##
## . ## ! . . . . . . . . ## . ##. . . ## ! ##
## . #########. ############ . ######. ## . ##
## .  . . . ##. ## . . . . //. . ? ##. ## . ##
######### . ##. ## . ### . ######. ##. ## . ##
##. . . . . ##. ## . ### . . . . . ##. ## . ##
##. ### . ####. // . ################. ## . ##
##? /// . . . . ## .  . . . . .  ##. ? ## . ##
########################### 0 ################
                          #####

"""
"""
 ___          _
|  _ \       | |
| (_) |  ___ | |_    ___  ___
|    /  / _ \|  _ \ / _ \/  _|
| |\ \ | (_) | (_) | (_) | (_
| | \_\ \___/|____/ \___/\___|
"""



... plus ...

|- faire attendre Python : import time | time.sleep(4)	# pour dormir 4 secondes..




		try:
			assert non_nomme == None or non_nomme == dict(non_nomme)
		except AssertionError:
			print("Valeurs: Désolé, ça n'a pas marché.. Votre variable doit être un dictionnaire !\nEXCLUSION !!")
		except ValueError:
			print("Valeurs: Désolé, ça n'a pas marché.. Votre variable doit être un dictionnaire !\nEXCLUSION !!")
		except NameError:
			print("Assignation: Désolé, ça n'a pas marché.. Une variable passée en paramètre n'est pas définie.\nEXCLUSION !!")
		self.non_nomme = non_nomme
# On traite le paramètre nommé appelé **dictionnaire :
		try:
			assert dictionnaire == dict(dictionnaire)
		except SyntaxError:
			print("Syntax: Désolé, ça n'a pas marché.. Peut-être avez-vous fait un faute de frappe ?\nEXCLUSION !!")
		except ValueError:
			print("Valeurs: Désolé, ça n'a pas marché.. Peut-être avez-vous rentrer en paramètres une liste et non des couples <clé:valeur>\nEXCLUSION !!")
		except NameError:
			print("Assignation: Désolé, ça n'a pas marché.. Une variable passée en paramètre n'est pas définie.\nEXCLUSION !!")
		self._dictionnaire = dictionnaire
# On merge les deux dictionnaires :
		if non_nomme != None:
			self._dictionnaire = {**self.non_nomme, **self._dictionnaire}
# On définit deux autre attributs, une liste contenant toutes les clés et une autre contenant toutes
# les valeures :
		self.list_keys = list(self._dictionnaire.keys())
		self.list_values = list(self._dictionnaire.values())



... système de déplacement ...

		if choix == 0:
			déplacement = pivotement(dictionnaire)				# Attention, <déplacement> est une liste [numero, direction] !
		elif choix != 0:
			déplacement = choix
		tq = int(emplacement_départ[0])
		while tq != tq + déplacement[0] + 1:
			nouveau_dictionnaire[tq] = dictionnaire[tq].reverse()
		if déplacement[1] == 'z':							# le numero = nombre de cases à sauter ; et direction = direction
			while déplacement[0] >= 0:
				for position, valeurs in nouveau_dictionnaire.items():
					if emplacement_départ[0] + déplacement[0] == position and position >= emplacement_départ[0]:
						scores[parties_new[0]] += 1
						parties = CheckAndPlayVertical(position, valeurs, nouveau_dictionnaire, emplacement_départ, déplacement, parties_new, direction, nombre, dictionnaire)
						enregistrer(scores, 'partie/scores.txt')
						enregistrer(parties, 'partie/parties.txt')
						if parties == True:
							jeu = True
						else:
							afficher_labyrinthe(parties)
							déplacement[0] -= 1
		elif déplacement[1] == 's':
			while déplacement[0] >= 0:
				for position, valeurs in dictionnaire.items():
					if emplacement_départ[0] + déplacement[0] == position and position >= emplacement_départ[0]:
						scores[parties_new[0]] += 1
						parties = CheckAndPlayVertical(position, valeurs, dictionnaire, emplacement_départ, déplacement, parties_new, direction, nombre, dictionnaire)
						enregistrer(scores, 'partie/scores.txt')
						enregistrer(parties, 'partie/parties.txt')
						if parties == True:
							jeu = True
						else:
							afficher_labyrinthe(parties)
							déplacement[0] -= 1
		elif déplacement[1] == 'd':
			indice = 0
			lettre = 0
			while déplacement[0] >= 0:
				for indice,lettre in enumerate(dictionnaire.values()[emplacement_départ[0]]):
					parties = CheckAndPlayHorizontal(indice, lettre, dictionnaire, emplacement_départ)
					enregistrer(parties, 'partie/parties.txt')
					enregistrer(scores, 'partie/scores.txt')
					if parties == True:
						jeu = True
					else:
						afficher_labyrinthe(parties)
						déplacement[0] -= 1
		elif déplacement[1] == 'q':
			indice = 0
			lettre = 0



... fonction CheckAndPlayVertical ...

def CheckAndPlayVertical(position, valeurs, nouveau_dictionnaire, emplacement_départ, déplacement, parties_new, direction, nombre, dictionnaire):
	""" Fonction permettant de vérifier et de définir le système de déplacement. """
	emplacement_joueur = len(valeurs) - emplacement_départ[1]
	nouvelle_liste = dict()
	i = 0
	for i,lettre in enumerate(valeurs):
		if lettre == '#':
			print("Paf ! Vous ne pouvez pas aller là-bas, il y à un mur !")
			return déplacements(parties_new, direction, nombre)
		if lettre == ' ':
			pass
		if lettre == '/':
			print("Vous ouvrez une porte et passez. Cette action vous\
	à coûter 2 points !")
			choix = list(déplacement.reverse())
			return déplacements(parties_new, direction, nombre, choix)
		if lettre == '.':
			nouveau_départ = list(nouveau_dictionnaire.values()[position])
			nouveau_départ.remove(lettre)
			nouveau_départ.insert(i, '0')
			nouveau_dictionnaire[position] = nouveau_départ
			nouveau_dictionnaire[emplacement_départ[0]].remove(emplacement_joueur)
			nouveau_dictionnaire[emplacement_départ[0]].insert(emplacement_joueur, '.')
			indice = 0
			while indice != len(dictionnaire.keys()) + 1:
				if indice in nouveau_dictionnaire:
					nouvelle_liste[indice] = nouveau_dictionnaire.values()[indice]
					nouvelle_liste[indice].reverse()
				else:
					nouvelle_liste[indice] = dictionnaire.values()[indice]
			return nouvelle_liste
		if lettre == '?':
			return goodies()

		if lettre == '!':
			return chance()

		if lettre == '>':
			jeu = True
			return jeu


... fonction CheckAndPlayHorizontal ...

def CheckAndPlayHorizontal(indice, lettre, dictionnaire, emplacement_départ):
	""" Fonction permettant de parcourir notre labyrinthe horizontalement. """
	emplacement_joueur = len(valeurs) - emplacement_départ[1]
	nouvelle_liste = dict()
	i = 0
	if lettre == '#':
		print("Paf ! Vous ne pouvez pas aller là-bas, il y à un mur !")
		return déplacements(parties_new, direction, nombre)
	if lettre == ' ':
		pass
	if lettre == '/':
		print("Vous ouvrez une porte et passez. Cette action vous\
à coûter 2 points !")
		choix = list(déplacement.reverse())
		return déplacements(parties_new, direction, nombre, choix)
	if lettre == '.':
		dictionnaire.values()[emplacement_départ[0]].remove(emplacement_départ[1])
		dictionnaire.vlaues()[emplacement_départ[0]].insert(emplacement_départ[1], '.')
		dictionnaire.values()[emplacement_départ[0]].remove(lettre)
		dictionnaire.values()[emplacement_départ[0]].insert(indice, '0')	
		indice = 0
		return dictionnaire
	if lettre == '?':
		return goodies()

	if lettre == '!':
		return chance()

	if lettre == '>':
		jeu = True
		return jeu



		try:
			assert var%2 == 0
			os.system("cls")
			print(r1,r2,r3,r4,r5,r6)
			print(clignotant)
			print("\n             Editer une carte: 'e'")
			print("                 quitter: 'q'")
			time.sleep(1)
			var += 1
		except AssertionError:
			os.system("cls")
			print(r1,r2,r3,r4,r5,r6)
			print("\n")
			print("\n             Editer une carte: 'e'")
			print("                 quitter: 'q'")
			time.sleep(2)
			var += 1



###########################
# . ### . ! . . . . . . . #
# . # # . ### . ### ? # . #
# . ### . ### . ### . / . #
# . . . . /// . ####### . #
# . ######### . . . .######
0 . ## . . .  . ####### . #
# . ## . ####### . . ## . #
# . ## ? . . . . . #### . >>>
# . ###########//###### ! #
# . . . #### . . . . // . #
###########################
