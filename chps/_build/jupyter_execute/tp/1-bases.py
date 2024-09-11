#!/usr/bin/env python
# coding: utf-8

# (tp:tp1)=
# # Feuille 1
# 
# :::{note}
# 
# Feuille téléchargeable au format jupyter notebook (`.ipynb`) 
# 
# :::
# 
# - Exercices sur les notions de bases
# - Accompagner les fonctions de tests unitaires pertinents
# - Utiliser les annotations de type pour les paramètres des fonctions

# ### Exercice (`est_rectangle()`)
# 
# 1.  Définir et écrire une fonction `est_rectangle()` qui vérifie si un
#     triangle est rectangle. Aucune hypothèse est effectuée sur les
#     paramètres de ce traitement.
# 2.  Ecrire un programme qui utilise cette fonction pour traiter un
#     nombre arbitraire de triangles entrées au clavier par l'utilisateur.

# ### Exercice (`randint` du module `random`)
# 
# Cet exercice utilise la fonction `randint` du module `random`.
# 
# 1.  $\blacksquare$ Regarder la description de la fonction `randint`.
# 2.  $\blacksquare$ Ecrire une fonction qui effectue un nombre arbitraire de tirages
#     aléatoires d'entiers compris entre 1 et 6 (bornes comprises) et qui
#     renvoie le pourcentage de 6 obtenus.
# 3.  Faire varier le nombre de tirages et vérifier la qualité de la
#     fonction `randint`.

# ### Exercice (palindrome)
# 
# Un palindrome est un mot, ou un groupe de mots, dont l'ordre des lettres
# reste le même qu'on le lise de la droite vers la gauche ou inversement.
# Des exemples bien connus sont "été", "kayak", "mon nom", "élu par cette
# crapule". Ce dernier permet d'illustrer qu'on ne tient pas compte en
# général des accents, trémas, cédilles, ni des espaces. Dans cet exercice
# :
# 
# -   un mot ou un groupe de mots est représenté par une chaîne de
#     caractères (`str`),
# 
# -   ces caractères sont sans accent, tréma, ni cédille : "ete"
# 
# -   les espaces sont considérés comme des caractères : ainsi "elu par
#     cette crapule" n'est pas un palindrome ici.
# 
# 1.  Ecrire une fonction qui teste si un argument est ou non un
#     palindrome et retourne le booléen correspondant.
# 
# 2.  Utiliser cette fonction pour tester un nombre arbitraire de mots
#     entrés au clavier.

# ### Exercice (Algorithme de type Monte-Carlo)
# 
# On va calculer une approximation de $\pi$ de façon probabiliste.
# 
# 1.  Ecrire une fonction qui vérifie si un point du plan défini par ses
#     coordonnées $(x,y)$ appartient à un disque de centre $(a,b)$ et de
#     rayon $r$.  
#     Rappel. L'équation du cercle de mêmes caractéristiques est :
#     $(x-a)^2 + (y-b)^2 = r^2$.
# 
# 2.  Identifier dans la documentation du module python `random` la
#     fonction adaptée à la génération d'un point aléatoire dans le carré
#     $[-1, 1] \times [-1, 1]$.
# 
# 3.  Soit $\mathcal{C}$ le cercle de centre 0 et de rayon 1. Ecrire une
#     programme qui génère $n$ points aléatoires situés dans le carré
#     précédent et calcule le ratio entre les points situés dans le cercle
#     $\mathcal{C}$ et $n$.
# 
# 4.  Faire varier $n$ et observer l'évolution de ce ratio.
# 
# 5.  ($\star$) En déduire une approximation de $\pi$.

# ### Exercice (Une première cryptanalyse)
# 
# *L'analyse fréquentielle, découverte au IXe siècle par Al-Kindi, examine
# les répétitions des lettres d'un message chiffré afin de trouver la clé.
# Elle est inefficace contre les chiffrements modernes tels que DES, RSA.
# Elle est principalement utilisée contre les chiffrements
# mono-alphabétiques qui substituent chaque lettre par une autre et qui
# présentent un biais statistique.* (wikipedia).  
# 
# L'analyse de la fréquence d'apparition des lettres dans les écrits d'une
# langue donnée permet donc de déchiffrer les messages cryptés par
# certains chiffrements simples. En se limitant aux textes en francais et
# écrits en minuscules, nous allons effectuer les deux dernières étapes du
# processus suivant.
# 
# -   Etape 1 : Estimer la fréquence moyenne d'apparition en français des
#     lettres de l'alphabet. Ici nous utiliserons des résultats existants.
# 
# -   Etape 2 : Appliquer un chiffrement de César pour crypter un message
#     arbitraire.
# 
# -   Etape 3 : Effectuer l'analyse fréquentielle du message ainsi chiffré
#     pour (tenter de) retrouver le message d'origine.
# 
# 1.  Etape 2. Le chiffrement de César est une technique simple de
#     décalage régulier (permutation circulaire) de chaque lettre de
#     l'alphabet. La longueur de ce décalage – distance entre la position
#     d'une lettre décalée et sa position d'origine ($\le$ 26) – est la
#     *clé* de ce chiffrement.
# 
#     1.  Ecrire une fonction `cesar()` qui retourne le chiffré d'un
#         message arbitraire (chaine de caractères) pour une clé
#         arbitraire.
# 
#     2.  Ecrire une fonction `decesar()` qui retourne le message
#         d'origine connaissant la clé de chiffrement.
# 
#     (que:cesar)=
#     3.  Valider vos fonctions avec le chiffrement suivant de clé 5.
#         Faire d'autres essais et utiliser aussi les ressources
#         disponibles sur le web.  
# 
#         |                 |     |                                       |
#         |:----------------|:---:|:--------------------------------------|
#         | message clair   |  :  | `UNIVERSITE DE PERPIGNAN VIA DOMITIA` |
#         | message chiffré |  :  | `ZSNAJWXNYJ IJ UJWUNLSFS ANF ITRNYNF` |
# 
# 2.  Etape 3. Déchiffrement d'un texte chiffré de clé inconnue. La
#     fréquence moyenne d'apparition des lettres de l'alphabet dans un
#     texte en français est [par exemple donné dans](https://fr.wikipedia.org/wiki/Analyse_fréquentielle#Fréquence_d'apparition)
# 
#     1.  Proposer une solution pour déchiffrer un message que l'on sait
#         crypté par un chiffrement de César mais de clé inconnue.
# 
#     2.  Coder cette solution et l'appliquer aux messages de [la
#         question](que:cesar).
# 
#     3.  Evaluer comment votre solution "passe à l'échelle", c'est-à-dire
#         comment son efficacité évolue pour des textes de tailles qui
#         augmentent. Proposer des optimisations.

# ###  Exercice (un peu d'images)
# 
# Une image à niveaux de gris peut être représentée par un tableau 2D d'entiers compris en 0 (noir) et 255 (blanc). 
# La taille de l'image $L \times C$ est arbitraire.  
# Ecrire les algorithmes des traitements suivants. On pourra commencer en
# introduisant un tableau supplémentaire pour l'image transformée. Selon
# les cas, on essaiera ensuite une solution “en place” : la transformation
# s'effectue sur le tableau de l'image d'origine.
# On utilisera les `ndarray` de `numpy` pour ces traitements.
# 
# 1.  Générer le négatif (*reverse video*) d'une image NB ou par niveaux
#     de gris.
# 
# 2.  Générer une image NB à partir d'une image niveau de gris.
# 
# 3.  Augmenter le contraste de la transformation précédente.  
#     Principe : fixer un seuil et remplacer les pixels plus clairs que le
#     seuil par des pixels blancs, et inversement les plus sombres que le
#     seuil par des pixels noirs.
# 
# 4.  Générer une image miroir vertical (le haut se retrouve en bas et
#     réciproquement) ou horizontal d'une image NB.
# 
# 5.  Augmenter la luminosité (ou luminance) d'une image à niveau de
#     gris.  
#     Principe : ajouter ou retrancher une constante de la valeur des
#     pixels.
# 
# 6.  Générer les contours significatifs d'une image.  
#     Principe : on remplace par un pixel noir chaque pixel dont la
#     variation des valeurs de ses 4 voisins varient au delà d'un certain
#     seuil, sinon on le remplace par un pixel blanc.
# 
# 7.  Réduire par 2 la taille d'une image à niveau de gris.  
#     Principe : chaque carré de 2x2 pixels est remplacé par 1 pixel de
#     valeur la moyenne des pixels du carré.

# ### Exercice ($Tx = b$)
# 
# On veut résoudre le système linéaire $Tx=b$ où la matrice $T$ est une
# matrice triangulaire inférieure carrée de taille $n$ et $b$ un vecteur
# second membre (de taille $n$). La matrice $T$ et et le vecteur $b$ sont
# supposés donnés (au clavier ou avec une valeur d'initialisation).
# 
# 1. Ecrire la fonction qui effectue ce traitement et les tests unitaires associés :
#     a. en utilisant les listes natives Python
#     b. en utilisant les `ndarray` de `numpy`
# 2. Comparer vos résultats et leurs performances avec le m^me traitement fourni par `numpy`.
# 

# ### Exercice (efficacité des algorithmes de recherche)
# 
# Effectuer une analyse expérimentale de la
# complexité pour comparer l'efficacité des algorithmes de recherche
# itérative et dichotomique (cas de l'entrée triée). Dégager les
# comportements dans le meilleur cas, dans le pire cas et en moyenne.

# (exo:forrec)= 
# ###  Exercice (récursion terminale et itération)
# 
# 1.  Donner la forme récursive qui produit le même traitement que celui
#     d'une boucle for qui (parcourt et) affiche les indices entiers
#     successifs de 11 à 1.

# 2.  Même question pour obtenir l'affichage : 1, 2, …, 10, 11.

# (exo:syracuse)= 
# ### Exercice (suite de Syracuse)
# 
# La suite de Syracuse $s$ d'un nombre $N$ donné est définie de façon
# récursive comme suit.
# 
# On commence avec $s(0) = N$, puis :
# 
# -   $s(n+1) = s(n)/2$, si $s(n)$ est pair,  
# -   $s(n+1) = 3s(n)+1$, si $s(n)$ est impair.
# 
# Ainsi définie, $s$ est une suite infinie de valeurs entières construites
# à partir de la valeur de départ $N$.
# 
# 1.  A la main pour commencer.
# 
#     1.  Calculer à la main les valeurs de la suite pour les valeurs de
#         départ $N = 4, 2, 1$. Qu'en déduire ?
# 
#     2.  Calculer à la main les valeurs de la suite pour les valeurs de
#         départ $N = 3, 5, 6, 7, 8, 16, 32$. Il peut être utile de
#         représenter les valeurs obtenues sous la forme d'un tableau où
#         chaque colonne (ou ligne) à la forme $N u_1 u_2 \dots u_n \dots$
#         où les $u_i$ sont les valeurs de la suite pour la valeur de
#         départ $N$. Qu'en déduire et en particulier que penser de la
#         terminaison de cette suite ?

# 2.  La coder de façon récursive et observer son comportement pour l'une
#     de ces valeurs de $N$. Attention !!!

# 3.  Terminaison : on arrête la suite $s(n)$ quand on rencontre $n = 1$
#     (c'est-à-dire $s(2)$). D'après la conjecture de Collatz, cette
#     valeur est rencontrée quelque soit le terme de départ $N$.
# 
#     1.  Compléter votre code précédent avec cette condition d'arrêt.
# 
#     2.  Compléter votre code précédent avec l'affichage de chaque valeur
#         calculée avant la terminaison.

# 4.  Écrire des fonctions qui calculent les notions suivantes (source
#     Wikipédia) :
# 
#     1.  le temps de vol qui est le plus petit indice $n$ tel que
#         $s(n) = 1$, *i.e.* jusqu'à la terminaison.
# 
#     2.  le temps de vol en altitude qui est le plus petit indice $n$ tel
#         que $s(n) \le N$.
# 
#     3.  l'altitude maximale qui est la valeur maximale $s(n)$ de la
#         suite.

# 5.  Coder ces fonctions et proposer des graphiques instructifs.

# 6.  Coder ces fonctions et proposer des graphiques instructifs.

# 7.  Coder le calcul avec terminaison de façon itérative.
