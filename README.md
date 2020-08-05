# Analyse de données - Historique des emprunts aux bibliothèques de Montréal

**Résumé**: nous allons écrire un script nous permettant d'obtenir les livres méritant d'être relus, selon leur ancienne popularité, en se basant sur les données du catalogue de la Ville de Montréal.

----

## Introduction

Dans le [catalogue des bibliothèques](https://donnees.montreal.ca/ville-de-montreal/catalogue-bibliotheques) de la Ville de Montréal sont recensées, de façon anonyme, le nombre de fois que chacun des 4 millions de documents a été emprunté - depuis l'inclusion dans le système du document ainsi que pour l'année en cours.

Cette analyse cherchera à faire découvrir l'analyse de données en Python par le biais de cette base de données.

## Quelle quantité de données !

La base de données est constituée d'un seul fichier de 1,2 Go, que l'on peut télécharger sur le site des Données Ouvertes de la Ville. Je ne vous recommande pas d'essayer d'ouvrir le fichier: il est fort possible que comme moi, vous n'arriviez pas à l'afficher en une seule opération, peu importe le logiciel utilisé. 

Nous allons utiliser un bref script Python pour accéder aux données avant de les traiter, et ce, ligne par ligne. Ainsi, le fichier ne sera jamais entièrement dans la mémoire de l'ordinateur, et nous pourrons effectuer nos opérations.

## Étape zéro: télécharger les données

Cela peut prendre un certain temps dépendamment de la vitesse de votre connexion Internet. Les données sont disponibles sur le site de la Ville de Montréal, sur la page du [catalogue des bibliothèques](https://donnees.montreal.ca/ville-de-montreal/catalogue-bibliotheques).

La dernière mise-à-jour du catalogue a eu lieu il y a sept mois, soit en janvier 2020.

## Première étape: établir les noms des colonnes

Dans le fichier `noms_colonnes.py` se trouve un court script visant à imprimer, dans le Terminal, la première ligne du fichier `donnees_ouvertes.csv`, qui contient l'historique d'emprunt des documents. Le script se trouve [sur GitHub]() et je le reproduis ici:


````
import csv

if __name__ == "__main__":
    filename = "donnees_ouverte.csv"
    with open(filename, 'r',) as csvfile:
        datareader  = csv.reader(csvfile)
        print(next(datareader))

````

Il retourne la liste suivante:

````
['Arrondissement', 'Localisation', 'Date-creation', 'Nombre-prets-vie', 'Nombre-prets-annee', 'Statut-document', 'Type-document', 'Cote', 'Titre', 'Variante-titre', 'Auteur', 'Collaboration', 'Editeur', 'Lieu', 'Pays', 'Annee', 'Nombre-pages', 'Langue', 'Collection', 'ISN', 'URL-image']

````
Ces noms de colonnes nous permettent d'établir les numéros des colonnes nous intéressant. Rappel: l'indexation, en Python, commence à zéro!

## Deuxième étape: lire le fichier ligne par ligne

Avant d'analyser les données, nous allons lire le fichier ligne par ligne, grâce à la librairie `csv`.

````
import csv

if __name__ == "__main__":
    filename = "donnees_ouverte.csv"
    with open(filename, 'r',) as csvfile:
        datareader  = csv.reader(csvfile)
        next(datareader)
        for row in datareader:
            # do analytical stuff
````

On ouvre le fichier ayant `filename` comme nom puis on lit la première ligne sans effectuer aucune opération. Enfin, la boucle `for row in datareader: `nous rend prêt.e.s à analyser nos données, une ligne à la fois !

## Troisième étape: tri des données

Pour cet exemple, nous avons choisi d'imprimer dans le Terminal uniquement les documents remplissant les critères suivants:

* le document est situé dans une bibliothèque de Rosemont
* le document est dans la catégorie Adultes
* le document est disponible
* le document est un documentaire ou un roman

Enfin, nous voulons faire ressortir les livres ayant un bon historique d'emprunt, mais dont la popularité est à la baisse.

* la colonne "Nombre-prets-vie" (colonne numéro 3), doit avoir une valeur supérieure à 85: on veut un nombre suffisant d'emprunts
* la colonne "Nombre-prets-annee" (colonne numéro 4), doit avoir une valeur égale à zéro: on ne veut que les livres ayant été délaissés... momentanément.

Enfin, on fait une pause entre chaque livre affiché, afin de consulter les informations affichées dans le Terminal.

Nous n'imprimons que la localisation du document, ainsi que son titre, son autrice ou auteur, et le nombre d'emprunts, depuis le début et pour l'année en cours.

Extrait du résultat obtenu (en ordre alphabétique):

````

(RPP) Rosemont / Adultes - Romans Ceux qui vont mourir te saluent / Vargas, Fred, 113 0


Appuyez sur ENTRÉE pour le prochain livre! 

(RPP) La Petite-Patrie / Adultes - Romans Les années du silence. Tremblay-D'Essiambre, Louise, 107 0


Appuyez sur ENTRÉE pour le prochain livre! 

(RPP) Rosemont / Adultes - Romans Milarepa / Schmitt, Éric-Emmanuel 112 0


Appuyez sur ENTRÉE pour le prochain livre! 
````

## Notes pour le futur

On pourrait en faire une application web qui permettrait de naviguer cette base de données de façon conviviale... à suivre !

Avec des données plus granulaires, on pourrait tracer la courbe de popularité de chaque document !


## Remerciements

Merci aux Données Ouvertes de la Ville de Montréal et au réseau des bibliothèques pour avoir rendu accessible ces données.