# -*-coding:Utf-8 -*
# /usr/bin/python3.7

# <elements.py> est chargé de définir les fonctions neccessaires au bon fonctionnement du jeu.

# Importation des modules :

import os
import pickle
import time
from random import randrange
from classes import *
from dicoo import *
#from roboc import *
#from déplacements import *

# Définition de la fonction chargée d'effacer l'écran;
def effacer_ecran():
	if os.uname().sysname == 'Linux':
		os.system('clear')
	else:
		os.system('cls')

# Définition des fonctions :

def retrouver_carte():
	""" Fonction chargée de retrouver les cartes du dossier <cartes>. """
	cartes = DictionnaireOrdonné()
	append = dict()

# Récupération des cartes :
	for nom_fichier in os.listdir('cartes'):	# on lit les cartes..
		if nom_fichier.endswith('.txt'):		# on sélectionne les fichiers .txt
			path = os.path.join('cartes', nom_fichier)	# on crée un chemin vers le fichier de la carte..
			nom_carte = nom_fichier[:-4].capitalize()	# on crée son nom..
			with open(path, 'r') as fichier:			# on lit son contenu..
				nom_fichier = str(fichier.read())
				nom_fichier = CartesClass(nom_carte, nom_fichier)	# on enregistre notre carte dans une
				append[nom_carte] = nom_fichier
				cartes.appends_début(nom_carte, nom_fichier)		# on enregistre notre carte dans un
#				cartes.reverse()					# parties ordonné..
				fichier.close()						# on ferme notre fichier..


# Affichage du menu :
#	effacer_ecran()		# nettoyage de l'écran..
	print("\nListe des niveaux :")
	for i,carte in enumerate(cartes.keys()):					# affichage des différents
		if i == len(cartes) - 1:								# niveaux..
			print("   '- <{0}> - Level {0} : {1}.\n".format(i + 1, cartes.keys()[-1]))
		elif i < len(cartes):
			print("   |- <{0}> - Level {0} : {1}.".format(i + 1, cartes.keys()[i]))

# Récupération de l'état des parties précédentes ou création d'une nouvelle :
	if os.path.exists('partie/parties_new.txt'):
		try:
			parties_new = unpickler('partie/parties_new.txt')			# Si <parties> existe et contient une partie..
			assert os.path.exists('partie/parties.txt')
			if os.path.exists('partie/parties.txt'):
				parties = unpickler('partie/parties.txt')
#			scores = unpickler('partie/scores.txt')
			if len(parties_new) == 2 and type(parties_new) is tuple:
				print("Partie en cours:\n   |_ <{0}> - {1}.".format(len(cartes) + 1, parties_new[0]))
		except EOFError:
			parties_new = tuple()
#			scores = dict()
#			enregistrer(scores, 'partie/scores.txt')
			enregistrer(parties_new, 'partie/parties_new.txt')
			return selection_partie(cartes, parties_new)
		except AssertionError:
			parties_new = tuple()
#			scores = dict()
#			enregistrer(scores, 'partie/scores.txt')
			enregistrer(parties_new, 'partie/parties_new.txt')
			return selection_partie(cartes, parties_new)
	else:														# Si <parties> n'existe pas..
		parties_new = tuple()
#		scores = dict()
#		enregistrer(scores, 'partie/scores.txt')
		enregistrer(parties_new, 'partie/parties_new.txt')
	return selection_partie(cartes, parties_new)



def selection_partie(cartes, parties_new):
	""" Fonction qui défini le numero de partie à commencer. """

# Sélection de la partie :
	selection = input("\n<level> ")
#	try:
	selection = int(selection)
	assert selection != 0
	selection -= 1
	if selection == len(cartes) and len(parties_new) == 2:
		return déplacements(1)
	else:									# création d'une nouvelle partie..
		parties_new = (cartes.items(selection))
		enregistrer(parties_new, 'partie/parties_new.txt')
		return déplacements(0)
#	except TypeError:
#		print("<TypeError> Vous n'avez pas entrer un nombre.")
#		return retrouver_carte()
#	except ValueError:
#		print("<ValueError> Vous n'avez pas saisi un nombre.")
#		return retrouver_carte()
#	except IndexError:
#		print("<IndexError> Vous avez saisi un nombre trop grand.")
#		return retrouver_carte()
#	except AssertionError:
#		print("<AssertionError> Vous n'avez pas saisi un nombre valide.")
#		return retrouver_carte()


def enregistrer(objet, fichier):
	""" Fonction permettant de sérialiser des objets. """
	with open(fichier, 'wb') as fichier0:
		pickler = pickle.Pickler(fichier0)
		pickler.dump(objet)

def unpickler(fichier):
	""" Fonction permettant de dépickler des objets. """
	with open(fichier, 'rb') as fichier0:
		unpickler = pickle.Unpickler(fichier0)
		objet_à_créer = unpickler.load()
	return objet_à_créer

def déplacements(choix=1,pivot=0):
	""" Fonction permettant de se déplacer. """
# On fait ici déplacer notre personnage. Le parcours est régie de la manière suivante :
#		- <0> : le personnage
#		- <.> : le personnage avance
#		- <#> : le personnage est bloque par le mur
#		- <//> : le personnage traverse la porte
#		- <?> : le personnage participe à un conversation
#		- <!> : le personnage bénificie d'une aide... ou le contraire !

# On défini le système de déplacements :
# On à les variables suivantes :
#	- parties : notre labyrinthe découpé {numéro:liste}
#	- parties_inversé : parties inversé {numéro:liste}
#	- liste_inversé : liste inversée [c,b,a]
#	- position : emplacement du personnage [liste,indice]
#	- déplacement : indications de déplacement du personnage [indice, direction]
#	effacer_ecran()	
#input()
	effacer_ecran()

#	print("\n")
	if choix == 1:
		parties = unpickler('partie/parties.txt')
	elif choix == 0:
		parties_new = unpickler('partie/parties_new.txt')
		parties = partie(parties_new)
		enregistrer(parties, 'partie/parties.txt')
#		print(parties)
	afficher_labyrinthe()
	if pivot == 0:
		nombre_déplacements, direction_déplacements = pivotement(parties)
	else:
		nombre_déplacements, direction_déplacements = list(pivot)
#		print(pivot)
#		print(parties)
	numero_ligne, indice_liste = personnage()
# On crée des objets qui vont se parcourir à l'envers :
	variable = len(parties)
	parties_inversé = dict()
	while variable > 0:
		parties_inversé[list(parties.keys())[variable-1]] = list(parties.values())[variable-1]
		variable -= 1

	liste_inversé = list(parties[numero_ligne])
	liste_inversé.reverse()
# On défini les différentes issues :
#	afficher_labyrinthe(parties_inversé)
#	print(liste_inversé)
	if direction_déplacements == 'd':
		i = 0
		v = 0
		for i,v in enumerate(parties[numero_ligne]):
			if i > indice_liste:
				CheckLong(i,v,nombre_déplacements,direction_déplacements,numero_ligne,indice_liste)

	elif direction_déplacements == 'q':
		i = 0
		v = 0
		for i,v in enumerate(liste_inversé):
			new_indice_liste = len(parties[numero_ligne]) - indice_liste - 1
			if i > new_indice_liste:
				CheckLong(i,v,nombre_déplacements,direction_déplacements,numero_ligne,indice_liste,1)

	elif direction_déplacements == 's':
		i = 0
		v = 0
		for clé,valeur in parties.items():
			if clé >= numero_ligne:
				CheckUp(clé,valeur,nombre_déplacements,direction_déplacements,numero_ligne,indice_liste)

	elif direction_déplacements == 'z':
		i = 0
		v = 0
		#new_numero_ligne = len(parties) - numero_ligne
#		print("numero :", numero_ligne, new_numero_ligne)
		for clé,valeur in parties_inversé.items():
			if clé <= numero_ligne:
				CheckUp(clé,valeur,nombre_déplacements,direction_déplacements,numero_ligne,indice_liste,1)

	else:
		print("\n<ValueError> Vous devez saisir les bonnes lettres. Voici un rappel :\n\
- 'z': aller vers le haut\
- 's': aller vers le bas\n\
- 'q': aller vers la gauche\
- 'd': aller vers la droite\n")
		input("\nContinuer..")
		return déplacements(1)

def CheckLong(i,v,nombre_déplacements,direction_déplacements,numero_ligne,indice_liste, gauche=0):
	""" Parcours de liste horizontal. """
	parties = unpickler('partie/parties.txt')
	#print("v est la lettre : ",i,v)
	if v == '#':
		print("Un mur ? Vous souhaitez traverser un mur ! Voyons, un peu de tenue..")
		input("\nContinuer..")
		return déplacements(1)
	elif v == ' ':
#		changelongespace(i,v,parties,numero_ligne,indice_liste)
#		pivot = [nombre_déplacements,direction_déplacements]
#		return déplacements(1,pivot)
		pass
	elif v == '/':
		pass
	elif v == '>':
		print("\nC'est gagné ! Vous vous en êtes sorti !")
		parties = 0
		enregistrer(parties, 'partie/parties.txt')
		parties_new = unpickler('partie/parties_new.txt')
		parties_new = '1'
		enregistrer(parties_new, 'partie/parties_new.txt')
		input("\nQuitter..")
		return retrouver_carte()
	elif v == '?':
		if gauche == 0:
			parties[numero_ligne].remove('?')
	#		parties[numero_ligne].insert(indice_liste, ' ')
			parties[numero_ligne].insert(i, '.')
		else:
			parties[numero_ligne].remove('?')
			parties[numero_ligne].insert(indice_liste-2, '.')
		enregistrer(parties, 'partie/parties.txt')
		return goodies()
		input('Continuer..')
		pass
	elif v == '!':
		if gauche == 0:
			parties[numero_ligne].remove('!')
	#		parties[numero_ligne].insert(indice_liste, ' ')
			parties[numero_ligne].insert(i, '.')
		else:
			parties[numero_ligne].remove('!')
			parties[numero_ligne].insert(indice_liste-2, '.')
		enregistrer(parties, 'partie/parties.txt')
		return miracle()
		input('Continuer..')
		pass
	elif v == '.':
		if gauche == 0:
			changelong(i,v,parties,numero_ligne,indice_liste)
		else:
			changelonggauche(i,v,parties,numero_ligne,indice_liste)
		nombre_déplacements -= 1
		if nombre_déplacements != 0:
			pivot = [nombre_déplacements,direction_déplacements]
			return déplacements(1,pivot)
		else:
			return déplacements(1)


def changelong(i,v,parties,numero_ligne,indice_liste):
	""" Fonction permettant de modifier <parties>. """
#	print(''.join(parties[numero_ligne]))
	changes = list()
	changes = list(parties[numero_ligne])
#	print("changes_print : \n", ''.join(changes))

	indice = 0
	caractère = 0
	changes_2nd_moitié = list()
	for indice, caractère in enumerate(changes):
		if indice >= indice_liste:
			changes_2nd_moitié.append(caractère)

	for u,n in enumerate(changes_2nd_moitié):
		if n == '.':
			nombre = int(u)
			break

	changes_2nd_moitié.remove('0')
	changes_2nd_moitié.remove('.')
	changes_2nd_moitié.insert(0, '.')
	changes_2nd_moitié.insert(nombre, '0')

	indice = 0
	caractère = 0
	changes_1ere_moitié = list()
	for indice, caractère in enumerate(changes):
		if indice < indice_liste:
			changes_1ere_moitié.append(caractère)

	changes = changes_1ere_moitié + changes_2nd_moitié

	parties[numero_ligne] = list(changes)
	enregistrer(parties, 'partie/parties.txt')

def changelonggauche(i,v,parties,numero_ligne,indice_liste):
	""" Fonction permettant de modifier <parties>. """
#	print(''.join(parties[numero_ligne]))
	liste_inversé = list(parties[numero_ligne])
	liste_inversé.reverse()
	changes = list()
	changes = list(liste_inversé)
#	print("changes_print : \n", ''.join(changes))

	indice = 0
	caractère = 0
	changes_2nd_moitié = list()
	for indice, caractère in enumerate(changes):
		new_indice_liste = len(parties[numero_ligne]) - indice_liste - 1
		if indice >= new_indice_liste:
			changes_2nd_moitié.append(caractère)

	for u,n in enumerate(changes_2nd_moitié):
		if n == '.':
			nombre = int(u)
			break

	changes_2nd_moitié.remove('0')
	changes_2nd_moitié.remove('.')
	changes_2nd_moitié.insert(0, '.')
	changes_2nd_moitié.insert(nombre, '0')

	indice = 0
	caractère = 0
	changes_1ere_moitié = list()
	for indice, caractère in enumerate(changes):
		if indice < new_indice_liste:
			changes_1ere_moitié.append(caractère)

	changes = changes_1ere_moitié + changes_2nd_moitié
	changes.reverse()

	parties[numero_ligne] = list(changes)
	enregistrer(parties, 'partie/parties.txt')

def CheckUp(clé,valeur,nombre_déplacements,direction_déplacements,numero_ligne,indice_liste,haut=0):
	parties = unpickler('partie/parties.txt')
	i=0
	v=0
	for i,v in enumerate(valeur):
		if i == indice_liste:
			if v == '#':
				print("Un mur ? Vous souhaitez traverser un mur ! Voyons un peu de tenue..")
				input("\nContinuer..")
				return déplacements(1)
			elif v == ' ':
				pass
			elif v == '/':
				pass
			elif v == '!':
				try:
					parties[int(numero_ligne)-1].remove('!')
					parties[int(numero_ligne)-1].insert(indice_liste, '.')
				except ValueError:
					parties[int(numero_ligne)+1].remove('!')
					parties[int(numero_ligne)+1].insert(indice_liste, '.')	
				enregistrer(parties, 'partie/parties.txt')
				return miracle()
				input('Continuer..')
				pass
			elif v == '?':
				try:
					parties[int(numero_ligne)-1].remove('?')
					parties[int(numero_ligne)-1].insert(indice_liste, '.')
				except ValueError:
					parties[int(numero_ligne)+1].remove('?')
					parties[int(numero_ligne)+1].insert(indice_liste, '.')
				enregistrer(parties, 'partie/parties.txt')
				return goodies()
				input('Continuer..')
				pass
				return déplacements(1)
			elif v == '>':
				print("\nC'est gagné ! Vous vous en êtes sorti !")
				parties = 0
				enregistrer(parties, 'partie/parties.txt')
				parties_new = unpickler('partie/parties_new.txt')
				parties_new = '1'
				enregistrer(parties_new, 'partie/parties_new.txt')
				input("\nQuitter..")
				return retrouver_carte()
				pass
			elif v == '.':
				if haut == 0:
					changesup(clé,valeur,i,v,numero_ligne,indice_liste)
				else:
					changesupgauche(clé,valeur,i,v,numero_ligne,indice_liste)
				nombre_déplacements -= 1
				if nombre_déplacements != 0:
					pivot = [nombre_déplacements,direction_déplacements]
					return déplacements(1,pivot)
				else:
					return déplacements(1)


def changesup(clé,valeur,i,v,numero_ligne,indice_liste):
	parties = unpickler('partie/parties.txt')

	indice = 0
	caractère = 0
	new_liste = list()
	for indice,caractère in enumerate(parties[numero_ligne]):
		if indice >= indice_liste:
			new_liste.append(caractère)

	new_liste.remove('0')
	new_liste.insert(0, '.')

	indice = 0
	caractère = 0
	new_liste_avant = list()
	for indice,caractère in enumerate(parties[numero_ligne]):
		if indice < indice_liste:
			new_liste_avant.append(caractère)

	parties[numero_ligne] = new_liste_avant + new_liste

	indice = 0
	caractère = 0
	new_new_liste = list()
	for indice,caractère in enumerate(parties[clé]):
		if indice >= indice_liste:
			new_new_liste.append(caractère)

	new_new_liste.remove('.')
	new_new_liste.insert(0, '0')

	indice = 0
	caractère = 0
	new_new_liste_avant = list()
	for indice,caractère in enumerate(parties[clé]):
		if indice < indice_liste:
			new_new_liste_avant.append(caractère)

	parties[clé] = new_new_liste_avant + new_new_liste
	enregistrer(parties, 'partie/parties.txt')


def changesupgauche(clé,valeur,i,v,numero_ligne,indice_liste):
	parties = unpickler('partie/parties.txt')
	variable = len(parties)
	parties_inversé = dict()
	while variable > 0:
		parties_inversé[list(parties.keys())[variable-1]] = list(parties.values())[variable-1]
		variable -= 1

#	new_numero_ligne = len(parties) - numero_ligne - 1

	indice = 0
	caractère = 0
	new_liste = list()
	for indice,caractère in enumerate(parties[numero_ligne]):
		if indice >= indice_liste:
			new_liste.append(caractère)

	new_liste.remove('0')
	new_liste.insert(0, '.')

	indice = 0
	caractère = 0
	new_liste_avant = list()
	for indice,caractère in enumerate(parties[numero_ligne]):
		if indice < indice_liste:
			new_liste_avant.append(caractère)

	parties[numero_ligne] = new_liste_avant + new_liste

	indice = 0
	caractère = 0
	new_new_liste = list()
	for indice,caractère in enumerate(parties[clé]):
		if indice >= indice_liste:
			new_new_liste.append(caractère)

	new_new_liste.remove('.')
	new_new_liste.insert(0, '0')

	indice = 0
	caractère = 0
	new_new_liste_avant = list()
	for indice,caractère in enumerate(parties[clé]):
		if indice < indice_liste:
			new_new_liste_avant.append(caractère)

	parties[clé] = new_new_liste_avant + new_new_liste
	enregistrer(parties, 'partie/parties.txt')

def personnage():
# On cherche notre personnage :
	parties = unpickler('partie/parties.txt')
	for ligne, valeurs in parties.items():
		if '0' in valeurs:
			for indice, lettre in enumerate(valeurs):
				if '0' == lettre:							# Attention, <position> est une liste [ligne, indice] !
					return [ligne, indice]				# la ligne = liste ; et l'indice = valeur


def pivotement(parties):
	""" Fonction permettant de choisir sa direction et de trouver sa voie ;) """
	pivotements = input("\n<déplacements> ")
	try:
		pivotements = list(pivotements)
		assert len(pivotements) <= 3
		direction = str()
		numero = int()
		direction_list = list()				# On défini des listes pour controler
		numero_list = list()				# la réponse de l'utilisateur..
		for i in enumerate(pivotements):
			try:
				int(i[1])
				numero_list.append(i[1])
			except ValueError:
				direction = str(i[1])
				direction = direction.lower()
				direction_list.append(i[1])
		try:
			if direction_list == [] and numero_list != []:
				print("<ValueError> Voyons, un chiffre ne suffit pas. Ce ne sont\nque des compléments, voila tout !")
				return pivotement(parties)
			if direction_list == []:
				direction_list.append('a')
			if numero_list == []:
				numero = 1
			elif len(numero_list) <= 2:
				numero = int(''.join(numero_list))
			if len(direction_list) > 1:
				print("\n<ValueError> Vous avez entrer deux lettres, une seule suffit !")
				return pivotement(parties)					# On lève une "exception" (sans raise)..
		except:
			print("<Error> Désolé, ça n'a pas marché !")
			return pivotement(parties)
	except AssertionError:
		print("\n<AssertionError> Vous avez saisi un nombre trop grand de caractères.")
		return pivotement(parties)
	return [numero, direction]		# On revoie une liste..


def afficher_labyrinthe():
	""" Fonction permettant d'afficher le labyrinthe modifié. """
#	parties = dict(parties)
#	parties_print = str()
#	for cle,val in parties.items():
#		parties_print += str(''.join(val))
#	print(parties_print)
	parties = unpickler('partie/parties.txt')
#	print(parties)
	maxi = len(parties)
	var = 0
	while var < maxi:
		print(''.join(list(parties.values())[var]))
		var += 1
# On défini l'HUD :
#	print("\nVos déplacements : {0}".format(scores[1]))

def partie(parties_new):
#	Définition de la variable parties. Cette variable contient chaques lignes du 
#	labyrinthe, de manière à pouvoir le manipuler plus simplement.

	chaine = str(parties_new[1])
	liste = list()
	parties = dict()
	indice = 0
	for i in chaine:
		if i != '\n':
			liste.append(i)
		else:
			parties[indice] = liste
			liste = list()
			indice += 1
	return parties

m1 = '\n'
m2 = '###############################################\n'
m3 = '##   _       _           _          o        ##\n'
m4 = '##  | \\   o / |      O  | |     O        o   ##\n'
m5 = '##  |  \\   /  | o ___   |o|   ___   _   ___  ##\n'
m6 = '##  |o  \\_/   |  / _o\\  | |  |o | |  | /o _\\ ##\n'
m7 = '##  |    _  O | / (_) \\ | |__|  |_|o | \\  \\  ##\n'
m8 = '##  | o | |   |/o  _   \\| _o | o     |_/o /  ##\n'
m9 = '##  |___| |___|___| |_O_\\____|_____O_|\\__/  O##\n'
m10 = '## _________________________________________ ##\n'
m11 = '###############################################\n'

b1 = '\n'
b2 = '###########################################\n'
b3 = '##    _______    *      *           *    ##\n'
b4 = '##   |   _   \\                *          ##\n'
b5 = '##   |  (_)  |   *  _    _       *       ##\n'
b6 = '##   |   *  /  ___ | \\  | |_   _   ___   ##\n'
b7 = '##   |   __ \\ / _ \\|  \\_| | | | | /  _\\  ##\n'
b8 = '##   |* (__) | (_) |* _   |*|_| |_\\ *\\   ##\n'
b9 = '##   |______/ \\___/|_| \\__|\\____/\\___/*  ##\n'
b10 = '## _____________________________________ ##\n'
b11 = '###########################################\n'

répliques_malus = [
"Vous rencontrez un passeur en route. Celui-ci vous demande de payer\npour pouvoir passer. Vous perdez 10 pièces d'or.",
"En chemin, vous tombez sur une pierre. Vous vous tordez la cheville.",
"Vous examinez les lieux quand vous rencontrez une marrée de rats.\nUn d'eux vous mord, vous êtes infectés.",
"Un vieux monsieur au sol vous demande de lui offrir un filet de pèche. Par\ncharité, vous lui en fabriquez un avec les lacets de vos chaussures.\nAttendez quoi ? Un filet de pèche ici c'est inutile !",
"Un enfant vous tire la langue et vous fait des remarques méchantes. \nVous êtes vexé.",
"Vous rencontrez une personne assise à une table de poker. Vous la défiez et\nperdez beaucoup d'argent.",
"Des bandits vous barrent la route. Pour sauver votre peau, vous leurs jetez\nvotre camarade, sans son consentement. Vous avez des remords."
]

répliques_bonus = [
"Vous assistez à un vol et décidez d'intervenir. Les gens vous respectent.",
"Ayant récemment trouver votre chemin dans le labyrinthe, vous décidez d'indiquer\nla sortie sur un panneau à l'attention d'autres joueurs. C'est bien.",
"Après avoir jouer au jeu, vous mettez une très bonne note et un petit commentaire\nbienveillant à l'attention du dévellopeur. Merci à vous.",
"Vous croisez un monstre peu acceuillant dans les couloirs du labyrinthe. Vous\nlui donnez vos dernière provisions pour couvrir votre fuite et survivez.",
"Vous trouvez une porte monnaie au sol et décidez de le rendre à son propriétaire.\nBravo.",
"Vous réservez une peu d'eau de votre gourde pour préserver votre hygiène. Vous évitez\nde justesse les infections.",
"Seul, vous décidez de chanter pour vous détendre. Vous êtes un vrai régal pour les\noreilles, les gens vous adorent."
]

répliques_goodies = [
["<Homme>, fumant une pipe:\nTu sais ce que j'aimes dans les soirées organisées chez les escrocs ?", "<Moi>:\nDites-moi.", "<Homme>:\nTout le monde s'en fout que tu fumes à l'interieur !", "<Moi>:\nJ'ai déjà entendu ça quelque part..."],
["<Femme>:\nAlors comme ça on se parle plus..", "<Homme>:\nBah tu m'as bien fait comprendre que tu voulais plus jamais qu'on se parle, nan ?", "<Femme>:\n...", "<Femme>:\nNan mais ça c'était hier..."],
["<Femme>:\nJ'te jure, il l'a embrassée.", "<Amie>:\nQui ça, Mme Michu ?", "<Femme>:\nOuais, je t'assures ! Quelle veille bique quand j'y pense !", "<Amie>:\nOh ma pauvre chérie, je vais te chercher un thé.",],
["<Homme nu>, sous la douche, chante:\nOhhhh, hiiiiii, lalalala bamm !", "<Voix masculine>, criant:\nC'est pas bientôt fini ton cirque !!","<Homme nu>:\nHii, laaaa dia rédonnaa benma locu !!", "<Voix masculine>:\nTa gueule du con !!", "<Homme nu>\nJeves enco rede guelé !"],
["<Homme>:\nAssis sur un banc, cinq minutes avec toi..", "<Femme>:\nRegardons les gens tant qu'il y en a !", "<Homme>:\nMais il y en a pas...", "<Femme>:\nBah voilà, vous avez tout gaché."],
["<Homme>, seul:\n*Vromm* *Vromm* !", "<Homme>, des petites voiture en mains:\n*Vroooomm* !!!", "<Homme>:\n*Hiiii* !", "<Voix feminine>:\nChérie, tout va bien là-haut ?", "<Hemme>:\nOui Oui mon coeur, tout vas bien !"],
["<Homme>, en pleine nuit, chuchotte:\nJ'te jure maintenant je vais le faire !", "<Homme>:\nCa fait des mois que je la supporte j'en peux plus,\nje vais la découper en morceaux, lui arracher les tripes\net la mettre dans un putain de sac poubelle...", "<Veille femme>:\nMon chérie tout va bien ? Tu viens te coucher ?", "<Homme>:\nHeu oui maman, j'arrive ! Et merde.."],
["<Homme>, devant son mirroir, seul:\nHey, salut belle gosse ! Nan, nan trop téléphoné tout ça..", "<Homme>:\nOh, salut belle gosse, t'as de chouettes oreilles.. Rahh nan c'est trop nul", "<Homme>:\nHeu, ah ça alors c'est toi ? Ca fait un bail dis-donc ! Comment tu vas ? Merde !"]
]

def miracle(compteur=20):
	effacer_ecran()
	var = randrange(len(répliques_goodies)-1)
	if os.path.exists('partie/var.txt'):
		var_list = unpickler('partie/var.txt')
	else:
		var_list = list()
	if var not in var_list:
		nh = randrange(100)
		if nh % 2 == 0:
			print(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11)
			print('\n')
			print(répliques_malus[var])
			input()
		elif nh % 2 == 1:
			print(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11)
			print('\n')
			print(répliques_bonus[var])
			input()
	elif compteur != 0:
		compteur -= 1
		miracle(compteur)
	var_list.append(var)
	enregistrer(var_list, 'partie/var.txt')
	if len(var_list) == len(répliques_goodies):
		var_list = list()
		enregistrer(var_list, 'partie/var.txt')
	return déplacements(1)

def goodies(compteur=20):
	effacer_ecran()
	opt = randrange(len(répliques_bonus)-1)
	if os.path.exists('partie/opt.txt'):
		opt_list = unpickler('partie/opt_list.txt')
	else:
		opt_list = list()
	if opt not in opt_list:
		print("             Conversation")
		print("_________________________________________")
		for i,v in enumerate(répliques_goodies[opt]):
			print(v, '\n')
			time.sleep(3.5)
	elif compteur != 0:
		compteur -= 1
		return goodies(compteur)
	opt_list.append(opt)
	enregistrer(opt_list, 'partie/opt_list.txt')
	if len(opt_list)+1 == len(répliques_bonus):
		opt_list = list()
		enregistrer(opt_list, 'partie/opt_list.txt')
	return déplacements(1)
