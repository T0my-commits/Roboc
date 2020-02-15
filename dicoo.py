# -*-coding:Utf-8 -*
# /usr/bin/python3.7

# <dicoo.py> est chargé de définir la classe DictionnaireOrdonné().

class DictionnaireOrdonné:
	""" Classe permettant de simuler un dictionnaire Python qui soit ordonné, c'est
	à dire dans lequel l'ordre des valeurs à une importance. En somme, le dictionnaire
	ordonné est un mélange de liste et de dictionnaire. """
	def __init__(self, non_nomme={}, **dictionnaire):
		""" Méthode __init__ : elle définie les attributs liés à self. """
# On traite le paramètre non_nomme :

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

	def __repr__(self):
		""" Méthode permettant d'affichier notre objet sans faire appel à print(). Si
		aucune méthode __str__() n'est définie, c'est cette méthode qui est appelée. """
#		self._dictionnaire = {}
#		for i,k in enumerate(self.list_keys):
#			self._dictionnaire[k] = self.list_values[i]
		return "{0}".format(self._dictionnaire)

#	def __str__(self):
#		return repr(self)
#		return '{}'.format(self._dictionnaire)

	def __getitem__(self, *indice):
		def intervalle(borne_inf, borne_sup):
			self.new_dico_2 = dict()
			while borne_inf <= borne_sup:
				self.new_dico_2[self.list_keys[borne_inf]] = self.list_values[borne_inf]
				borne_inf += 1
			return self.new_dico_2

		try:
			assert indice[0][0] == int(indice[0][0])
			valeur_1 = indice[0][0]
			valeur_2 = indice[0][1]
			return intervalle(valeur_1, valeur_2)
		except IndexError:
			print("Index: Désolé, ça n'a pas marché.. Vous avez saisi un indice trop grand.\nEXCLUSION !!")
		except ValueError:
			for i,k in enumerate(self.list_keys):
				if k == indice[0]:
					var = int(i)
			self.new_dico_2 = dict()
			self.new_dico_2[indice[0]] = self.list_values[var]
			return self.new_dico_2
		except TypeError:
			try:
				assert indice[0] == int(indice[0])
				valeur_0 = indice[0]
				self.new_dico_2 = dict()
				self.new_dico_2[self.list_keys[valeur_0]] = self.list_values[valeur_0]
				return self.new_dico_2
			except IndexError:
				print("Index: Désolé, ça n'a pas marché.. Vous avez saisi un indice trop grand.\nEXCLUSION !!")


	def __setitem__(self, clé, valeur):
		""" Méthode permettant de definir une nouvelle valeure à l'aide de la formulation <DictionnaireOrdonné["clé"] = valeur>. """
		self.list_keys.append(clé)
		self.list_values.append(valeur)
		self._dictionnaire = dict()
		for i,k in enumerate(self.list_keys):
			self._dictionnaire[k] = self.list_values[i]
#		return self._dictionnaire

	def __len__(self):
		""" Méthode permettant de connaître la taille d'un onjet conteneur avec la syntaxe <len(objet)>. """
		return len(self.list_keys)

	def __contains__(self, clé):
		""" Méthode permettant de vérifier si un clé existe dans le dictionnaire avec la syntaxe <clé in dictionnaire>. """
		return self.list_keys.__contains__(clé)

	def __add__(self, dico_ajout):
		""" Méthode permettant de merger deux dictionnaires avec l'opérateur <+>. """
		dico_clés = list(dico_ajout.keys())
		dico_valeur = list(dico_ajout.values())
		i = 0
		while i < len(dico_clés):
			self.list_keys.append(dico_clés[i])
			self.list_values.append(dico_valeur[i])
			i += 1
		self._dictionnaire = dict()
		for i,k in enumerate(self.list_keys):
			self._dictionnaire[k] = self.list_values[i]
		return self._dictionnaire


	def __delitem__(self, index):
		""" Méthode permettant de supprimer un élément à un indice donné à l'aide de la formulation <del DictionnaireOrdonné[index]>. """
		try:
			del self.list_keys[index]
			del self.list_values[index]
			self._dictionnaire = dict()
			for i,k in enumerate(self.list_keys):
				self._dictionnaire[k] = self.list_values[i]
#			return self._dictionnaire
		except TypeError:
			self.list_keys.remove(index)
			self.list_values.remove(self._dictionnaire[index])
			self._dictionnaire = dict()
			for i,k in enumerate(self.list_keys):
				self._dictionnaire[k] = self.list_values[i]
#			return self._dictionnaire


	def __iter__(self):
		""" Itérateur permettant de parcourir le dictionnaire donné à l'aide de la formulation <for élement in dictionnaire>. """
		self.nb_chaine = len(self.list_keys)
		self.iterateur = list(self.list_keys)
		self.iterateur.reverse()
		return self

	def __next__(self):
		""" Méthode accompagnant le fonctionnement de l'itérateur. """
		if self.nb_chaine == 0:
			raise StopIteration
		self.nb_chaine -= 1
		return "{0}".format(self.iterateur[self.nb_chaine])

	def sort(self):
		""" Méthode de tri utilisée avec <objet.sort()>. """
		dico_rangée = dict(self._dictionnaire)
		self.list_keys.sort()
		self._dictionnaire = dict()
		self.list_values = list()
		i = 0
		while i < len(self.list_keys):
			self._dictionnaire[self.list_keys[i]] = dico_rangée[where(self, i)]
			self.list_values.append(dico_rangée[where(self, i)])
			i += 1

	def reverse(self):
		""" Méthode chargée d'inverser l'ordre des clés de notre dictionnaire. S'utilise avec <objet.reverse()>. """
		self.list_keys.reverse()
		self.list_values.reverse()
		self._dictionnaire = dict()
		for i,k in enumerate(self.list_keys):
			self._dictionnaire[k] = self.list_values[i]

	def items(self, indice):
		""" Méthode renvoyant un générateur avec le couple <clé:valeur>. """
		return (self.list_keys[indice], self.list_values[indice])

	def itemm(self):
		""" Méthode permettant de parcourir notre objet. """
		for i,k in enumerate(self.list_keys):
			yield (k,self.list_values[i])

	def keys(self):
		""" Méthode revoyant un générateur avec seulement les <clé> du couple <clé:valeur> de self._dictionnaire. """
		return self.list_keys

	def values(self):
		""" Méthode revoyant un générateur avec seulement les <valeur> du couple <clé:valeur> de self._dictionnaire. """
		return self.list_values

	def appends_début(self, valeur_keys, valeur_values):
		""" Méthode permettant d'instancier une nouvelle valeure au début de notre dictionnaire. """
#		valeur_keys = list(valeur_keys)
#		valeur_values = list(valeur_values)
		self.list_keys.append(valeur_keys)
		self.list_values.append(valeur_values)
		self._dictionnaire = dict()
		for i,k in enumerate(self.list_keys):
			self._dictionnaire[k] = self.list_values[i]
		return self._dictionnaire

def where(self, indice):
	for i,k in enumerate(self.list_keys):
		if i == indice:
			return k


"""
import os
os.chdir('C:/Users/devie/Documents/Projet Python/Roboc')
dico = {"tree":3, "four":4}
from dicoo import *
babe = DictionnaireOrdonné(dico,pip=12)
bob = DictionnaireOrdonné(bihl= 546, ioh= 45)
babe
"""