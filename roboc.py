# -*-coding:Utf-8 -*
# /usr/bin/python3.7

""" Fichier exécutable de notre jeu. """

#fichier_chemin = os.path.join(os.getcwd(), __file__)
#os.chdir(fichier_chemin)

# On importe les modules nécessaires :
import os
import pickle
import time
from random import randrange
from classes import *
from dicoo import *
from elements import *
#from déplacements import *

"""
		#####################
		0 . //. . . . .## . >>>
		# . ######### .## . #
		# . ##. . . . .## . #
		# ! ##. Roboc ### . #			BIENVENUE au coeur de mon CODE SOURCE mon brave
		# . ## by t0my ## . #				de chez OpenClassrooms !
		# . . . # # . ?## . #
		##### . ### . ### . #
		# . ! . //. . . . . #
		#####################
"""

# Définition des fonctions du menu :

r1 = "          ___          _\n"
r2 = "        |  _ \\       | |\n"
r3 = "        | (_) |  ___ | |_    ___  ___\n"
r4 = "        |    /  / _ \\|  _ \\ / _ \\/  _|\n"
r5 = "        | |\\ \\ | (_) | (_) | (_) | (_\n"
r6 = "        |_| \\_\\ \\___/|____/ \\___/\\___|, by T0my\n"
clignotant = "\n     Appuyez sur une touche pour continuer.."

def menu():
	var = 6
	while var >= 0:
		if var % 2 == 0:
			os.system("clear")
			print('\x1b[1;34m' + r1,r2,r3,r4,r5,r6 + '\x1b[0m')
			print('\x1b[5;33m' + clignotant + '\x1b[0m')
			print('\x1b[46m' + "\n                  jouer: 'j'")
#			print("             Editer une carte: 'e'")
#			print("          Réinitialiser les cartes: 'r'")
			print("                 crédits: 'c'")
			print("                 quitter: 'q'\n\n" + '\x1b[0m')
			print('\x1b[1;34m' + "<roboc> " + '\x1b[0m')
			time.sleep(0.5)
			var -= 1
		else:
			os.system("clear")
			print(r1,r2,r3,r4,r5,r6)
			print("\n")
			print("\n                  jouer: 'j'")
#			print("             Editer une carte: 'e'")
#			print("          Réinitialiser les cartes: 'r'")
			print("                 crédits: 'c'")
			print("                 quitter: 'q'\n\n")
			print("<roboc> ")
			time.sleep(0.6)
			var -= 1

def édition(réinitialiser=0, murs='#', chemin='.', portes='/', sortie='>', question='?', exclamation='!'):
	if réinitialiser == 0:
		murs = input("Saisissez le type de murs : ")
		chemin = input("Saisissez le type de chemin : ")
		portes = input("Saisissez le type de portes : ")
		sortie = input("Saisissez le type de sortie : ")
		question = input("Saisissez l'icône remplaçant de <?> : ")
		exclamation = input("Saisissez l'icône remplaçant de <!> : ")
		configuration = [murs,chemin,portes,sortie,question,exclamation]
		enregistrer(configuration, 'configuration.txt')
		edit = os.listdir('cartes')
		print(edit)
		for indice,edition in enumerate(edit):
			select = unpickler(os.path.join('cartes/', edit[indice]))
			print(select)
			select = list(select)
			print(select)
			i = 0
			l = 0
			for i,l in enumerate(select):
				if l == '#':
					select.remove(l)
					select.insert(i, murs)
				elif l == '.':
					select.remove(l)
					select.insert(i, chemin)
				elif l == '/':
					select.remove(l)
					select.insert(i, sortie)
				elif l == '?':
					select.remove(l)
					select.insert(i, question)
				elif l == '!':
					select.remove(l)
					select.insert(i, exclamation)
				else:
					pass
			select = str(''.join(select))
			enregistrer(select, os.path.join('cartes/', select))
		return game()
	elif réinitialiser == 1:
		edit = os.listdir('cartes')
		edits = unpickler('configuration.txt')
		mursj = configuration[0]
		cheminj = configuration[1]
		portesj = configuration[2]
		sortiej = configuration[3]
		questionj = configuration[4]
		exclamationj = configuration[5]
		for indice,edition in enumerate(edit):
			select = unpickler(os.path.join('cartes/', edit[indice]))
			select = list(select)
			i = 0
			l = 0
			for i,l in enumerate(select):
				if l == mursj:
					select.remove(l)
					select.insert(i, murs)
				elif l == cheminj:
					select.remove(l)
					select.insert(i, chemin)
				elif l == portesj:
					select.remove(l)
					select.insert(i, sortie)
				elif l == questionj:
					select.remove(l)
					select.insert(i, question)
				elif l == exclamationj:
					select.remove(l)
					select.insert(i, exclamation)
				else:
					pass
			select = str(''.join(select))
			enregistrer(select, os.path.join('cartes/', select))
		return game()

def quitter():
	pass

def crédits():
	effacer_ecran()
	print("Développeur / Concepteur : T0my\nIdée : OpenClassrooms\n\nRetour..")
	input()

def game():
	""" Fonction exécutable pour lancer le jeu ! """
	os.system("clear")
	print('\x1b[1;34m' + r1,r2,r3,r4,r5,r6 + '\x1b[0m')
	print('\x1b[33m' + clignotant + '\x1b[0m')
	print('\x1b[36m' + "\n                  jouer: 'j'")
#	print("             Editer une carte: 'e'")
#	print("          Réinitialiser les cartes: 'r'")
	print("                 crédits: 'c'")
	print("                 quitter: 'q'\n\n" + '\x1b[0m')
	try:
		réponse_joueur = input('\x1b[1;34m' + "<roboc> " + '\x1b[0m')
		assert len(réponse_joueur) == 1
		réponse_joueur = réponse_joueur.lower()
		if réponse_joueur == 'c':
			crédits()
			return game()
#		if réponse_joueur == 'e':
#			return édition()
#		elif réponse_joueur == 'r':
#			return édition(1)
		elif réponse_joueur == 'j':
			return Games()
		elif réponse_joueur == 'q':
			return quitter()
		else:
			print("\n<Error> Mon menu vous déplait ? Allons, il n'est pas si\n\
cruel de vous faire choisir une de ces lettres quand même ? Entrez celle qui\n\
conviens à votre désir.")
			input()
			return game()
	except AssertionError:
		print("\n<Error> Vous avez saisi deux caractères, un suffit !")
		input()
		return game()
	except AttributeError:
		print("\n<AttributeError> Les nombres ne sont pas considérés, faites attention !")
		input()
		return game()


def Games():
	""" Corps du jeu. """
	retrouver_carte()

# Prêt pour le grand final ? OK alors on lance l'usine à gaz mec !
#menu()
game()
