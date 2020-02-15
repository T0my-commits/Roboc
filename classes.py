# -*-coding:Utf-8 -*
# /usr/bin/python3.7

# <classes.py> est chargé de définir les classes de certains objets,
# à l'exception du Dictionnaire Ordonné qui bénéficie de son propre
# fichier.

# Importation des modules :
import os, pickle

# Définition des classes :

class CartesClass:
	""" Métaclasse de nos labyrinthes. Elle défini entre autres :
		- L'objet qui sera crée grâce à la méthode __new__()
		- Les attributs qui caractérisent notre labyrinthe
	"""
#	def __new__(cls):
#		""" Méthode définissant notre objet <self>. """
#		return __init__(self)

	def __init__(self, nom_carte, carte):
		""" Constructeur de notre classe. Il défini les principaux
		attributs de notre classe à savoir :
			- le nom de l'objet : nom_carte
			- le contenu de l'objet : carte
			- les murs : murs
			- les portes : portes
			- le chemin : chemin
			- la sortie : sortie
			- l'emplacement de départ : emplacement d'où part le personnage
		"""
		self.nom = nom_carte
		self.carte = carte
#		self.emplacement_départ = emplacement_départ

# On défini les lignes de notre carte pour le systeme de déplacements :
#		self.lignes = self.lignes()

	def __repr__(self):
		""" Méthode permettant de représenter notre labyrinthe. """
		return self.carte
