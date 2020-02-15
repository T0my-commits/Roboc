Bonjour mon brave de chez OpenClassrooms !

Ce document à pour but d'éclaircir quelques points concernant le jeu :

1 -- Jouabilité
____________________

Les déplacements se font à l'aide des touches 'z', 's', 'q' et 'd'.

Ces directions s'accompagnent de nombres comme '10' ou '01'
et peuvent être placés avant ou après la lettre.

Ex :	"z10" -> 10 cases vers le haut
	"01q" -> 1 cases vers la gauche

Pour sauvegarder et quitter la partie en cours, fermez simplement 
la fenêtre en cliquant sur la croix.


2 -- Extras
____________________

Au sein du labyrinthe se cache plusieurs conversations indentifiées
par un symbole <?>. Ces mises en scènes simulent des situations décalées
qui dinamisent le gameplay.

En plus des conversations, il existe des malus ou des bonus identifiés par le
symbole <!>. Ces "aides" (ou le contraire) sont pûrement cosmétiques
et n'ont aucun interêt vis-à-vis du jeu.

Il n'est pas impossible de tomber deux fois sur la même information durant
une partie, le nombre de chaques répliques étant de 7 maximum. Il se peut également
que le jeu crash suite à une de ces intéractions, cependant cela n'affecte pas le gameplay
et la mécanique qui s'y cache derrière, à l'origine de la création du jeu. En somme,
ces extras sont seulement des rajouts.


3 -- Notes importantes
________________________

Concernant la notion d'"upgrade" signalée dans l'exercice du cours et que je n'ai
pas compris, mon système de déplacements repose sur une structure conditionnelle
résumé brievement par l'état suivant :
	- SI il y a un point '.':
		tu avances
	- SINON autre condition:
		tu fais autre chose
De ce fait, il est possible de rajouter des escaliers vers d'autres niveaux, ou plus encore !


4 -- Fichier exécutable
________________________

Le fichier exécutable est 'roboc.py'. Il ne doit pas être déplacé dans un autre répertoire
que celui dans lequel il se trouve pour des raisons évidentes.

Si le programme rencontre des bugs et que cecis persistent, veuillez vider le répertoire
'partie' en supprimant l'intégralité de son contenu. Cette action permettra de réinitialiser
certaines variables du jeu, et permettra de résoudre certains problèmes. Cependant, cette
intervention reste une connaissance utile en cas d'urgence et en aucun cas une habitude.


5 -- Vérification des fichiers et édition de cartes
________________________

Les fichiers présents dans le répertoire sont au nombre de :
	- 5 fichier .py
	- 1 fichier .txt
	- 2 répertoires 'cartes' et 'partie'

En ce qui concerne le rajout de cartes, il suffit d'éditer un fichier texte avec votre carte à l'interrieur.
Pensez à sautez une ligne en dessous de votre labyrinthe, sinon la dernière ligne ne s'afficheras pas.
Placez votre fichier .txt dans le répertoire 'cartes'pour qu'elle soit prise en compte
par le programme. Le titre de votre fichier .txt constituras le titre de votre niveau,
choisissez-le bien ! Les espaces sont acceptés.

Enfin, pour créer une carte, il faut obéir à certaines règles de syntaxe :
	- le personnage est un '0' (zéro)
	- les murs sont des '#'
	- les portes sont des '/'
	- le chemin sur lequel évolue notre personnage est une succession
	de point '.'. Les espaces ' ' sont ignorés.
	- les conversation sont identifiées par des '?'
	- les malus ou bonus sont identifiés par des '!'
	- la sortie est un '>'
