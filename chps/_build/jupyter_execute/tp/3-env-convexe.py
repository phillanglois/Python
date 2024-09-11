#!/usr/bin/env python
# coding: utf-8

# # Feuille 3
# 
# L'objectif de ce TP est de **calculer et tracer l'enveloppe convexe d'un nuage de points du plan**. L'algorithme de ce calcul utilise des piles.
# Les notions utiles seront introduites au fur et à mesure.
# 
# -   Ce TP peut profiter d'une implémentation python du type de données abstrait *pile LIFO*.
# -   Le travail demandé sera effectué dans ce notebook jupyter.
# -   Dans le notebook, les *modules* demandés pourront être codés par des fonctions ou des traitements regroupés dans une cellule. 
# - Accompagner chaque développement de son test unitaire de validation.
# -   Dans un second temps, les traitements demandés pourront être regroupés dans des fichiers python (`.py`) exécutables depuis la ligne de commande.

# In[1]:


# on regroupe les imports utiles
from math import sqrt
from random import random
import matplotlib.pyplot as plt


# ## Points du plan, relation d'ordre
# 
# Un *point* du plan est un couple $(x, y)$ (de nombres flottants).  
# On définit la relation d'ordre suivante entre 2 points du plan :  
# $$(x,y) \le (x',y') \iff x < x' \text{ ou } (x = x' \text{ et } y \le y').$$  
# Un *nuage de points* est un ensemble fini de points.
# 
# ### `points`
# 
# Concevoir et coder un module `points` qui permet de définir des points,
# de les comparer, d'afficher leurs coordonnées $(x,y)$ à l'écran.

# ## `Nuage de points : générer, trier, afficher, stocker, tracer
# 
# ### `nuage`
# 
# Ecrire un module `nuage` qui permet de définir un nuage de points de
# taille paramétrable et de d'afficher les coordonnées de ses points à
# l'écran.
# 
# ![Un nuage de points aléatoires](./fig/nuage.png)

# ### `un_nuage_random()`
# 
# Compléter ce module de façon à pouvoir générer aléatoirement un nuage de
# points de taille arbitraire et contenu dans le carré
# $[0,1] \times [0,1]$.

# ### `trier_nuage()`
# 
# Compléter ce module de façon à pouvoir trier les points d'un nuage donné selon l'ordre croissant défini sur les points du plan.

# ### `write_nuage()`
# 
# Compléter ce module de façon à pouvoir enregistrer un nuage de points de taille arbitraire dans un fichier de texte. La taille du nuage sera aussi enregistrée dans ce fichier.  
# Les fichiers `data_nuage_10.txt` et `data_nuage_100.txt` fournis dans l'archive `3-data-nuage.zip` sont des exemples de tels fichiers.

# ### `read_nuage()`
# 
# Compléter ce module de façon à pouvoir lire un nuage de points de taille arbitraire à partir d'un fichier de texte selon le format défini ci-dessus.

# ### `aff_nuage()`
# 
# Compléter ce module de façon à pouvoir tracer graphiquement un nuage de
# points donné. Le tracé sera effectué à l'écran par défaut. Il permettra
# aussi de stocker ce tracé dans un fichier `jpeg`.

# ## Orientation de 3 points du plan
# 
# On va développer progressivement un module `geometrie2d`.
# 
# On commence avec la détermination de l'orientation d'un triplet de points.
# 
# ![Orientations d'un triplet (p,q,r)](./fig/orientation_pqr.png)
# 
# Un triplet `(p,q,r)` de points *non alignés* du plan est *orienté
# positivement* si l'angle des vecteurs `(pq, pr)` est dans $]0, \pi \ [$
# (modulo $2\pi$). Sinon, il est *orienté négativement*.
# 
# On vérifie l'orientation du triplet `(p,q,r)` en calculant le signe du
# déterminant 2x2 $det(pq,pr)$ des vecteurs `pq` et `pr`. Signe du
# déterminant et sens d'orientation coïncident.
# 
# On rappelle que :
# $$det(pq,pr) = (x_q - x_p)\times(y_r - y_p) - (y_q - y_p)\times(x_r -
# x_p).$$

# ### `orientation()`
# 
# Commencer le module `geometrie2d` avec une fonction qui calcule l'orientation d'un triplet de points du plan.

# ## `geometrie2d`: enveloppe convexe
# 
# Un ensemble $C$ est *convexe* si le segment \[p,q\] qui relie deux
# points quelconques de $C$ est inclus dans $C$.
# 
# ![exemple d'ensembles convexes et non
# convexe](./fig/convexes.png)
# 
# L'*enveloppe convexe* $Conv(N)$ d'un nuage de points $N$ est le plus
# petit polygone convexe qui contient tous les points de $N$.
# 
# ![L'enveloppe convexe du nuage de points
# ‘data_nuage_10.txt'](./fig/env_conv10.png) ![L'enveloppe
# convexe du nuage de points
# ‘data_nuage_100.txt'](./fig/env_conv100.png)

# ### Construire l'enveloppe convexe d'un nuage de points 
# 
# Il existe plusieurs algorithmes. 
# Nous utiliserons l'algorithme de Graham-Andrew qui s'appuie sur un balayage du nuage de points préalablement triés. 
# 
# **Hypothèse importante : aucun triplet de points alignés**
# 
# Dans un premier temps, il est plus facile de supposer qu'aucun triplet $(p, q, r)$ du nuage de points ne sont alignés.
# 
# On choisira d'arrêter le traitement d'un éventuel nuage qui ne vérifie pas cette hypothèse.

# **Algorithme de Graham-Andrew.**
# 
# On construit $Conv(N)$ en balayant de gauche à droite avec une droite verticale le
# nuage $N$ préalablement trié par ordre croissant. 
# On convient ainsi que p0 est le plus petit point de N, *ie.* celui le plus à gauche.
# 
# Chaque point p rencontré par la droite met à jour l'enveloppe convexe du sous-nuage à gauche du point p.  
# Cette mise à jour s'effectue en distinguant une partie supérieure et une partie inférieure de l'enveloppe convexe.
# 
# L'*enveloppe supérieure* est au dessus du segment \[p0, p\]. 
# Cette enveloppe `ES` est modifiée par l'algorithme suivant qui justifie de stocker `ES` comme une pile de base p0. On ajoute aussi à `ES`, p1 le point immédiatement supérieur à p0 (*ie.* immédiatement à droite de p0).
# La pile `ES` est ainsi composée d'au moins deux éléments.

# Soit p le point rencontré par le balayage de N. 
# Notons q et r les deux derniers points ajoutés à `ES` -- q est au sommet.
# 
# -   Si le triplet (p,q,r) est orienté positivement alors p est ajouté à
#     `ES`. Ce qui termine la mise à jour de `ES`.
# -   Sinon q est retiré de `ES` et on reprend le test d'orientation et le
#     traitement précédent pour **un nouveau triplet (p,q,r)** jusqu'à
#     terminer la mise à jour de `ES` :
#     -   par l'ajout de p à `ES`  
#     -   ou parce qu'il ne reste que p0 dans `ES`. Dans ce cas, on
#         termine en ajoutant p à `ES` – qui est ainsi toujours composée
#         d'au moins deux éléments.
# 
# `ES` contient l'enveloppe convexe supérieure du nuage N une fois tous
# les points p de N balayés.
# 
# On convient aisément que le point le plus à droite de N est le dernier
# point ajouté à `ES`.

# **Illustration graphique.**
# 
# `ES` = {0,1,5,6}, début du traitement de p = 7
# 
# ![Orientation (7,6,5) négative](./fig/ES-1.png)
# 
# `ES` = {0,1,5}, p = 7
# 
# ![Orientation (7,5,1) négative](./fig/ES-2.png)
# 
# `ES` = {0,1}, p = 7
# 
# ![Orientation (7,1,0) positive](./fig/ES-3.png)
# 
# `ES` = {0,1,7}, fin du traitement de p = 7.

# ### `maj_es()` : enveloppe convexe supérieure
# 
# Compléter le module précédent avec une fonction `majES(pile, point)` qui
# effectue la mise à jour de la pile `ES` lors du traitement du point p. 

# ### `maj_ei()`: enveloppe convexe inférieure 
# 
# L'*enveloppe convexe inférieure* est obtenue de façon similaire avec une
# (autre) pile ‘EI' et un test d'orientation inverse.
# 
# Compléter le module précédent avec une fonction `majEI(pile, point)` qui
# effectue la mise à jour de la pile ‘EI' lors du traitement du point p. 

# ### Validation
# 
# Valider les deux fonctions précédentes sur des nuages de 5 ou 6 points.

# ### `env_convexe()`
# 
# L'enveloppe convexe $Conv(N)$ est une (autre) pile construite à partir
# de `ES` et `EI` en stockant successivement chaque point visité par les 2
# parcours suivants :  
# - L'enveloppe convexe supérieure est parcourue de la gauche vers la
# droite,  
# - l'enveloppe convexe inférieure est parcourue de la droite vers la
# gauche;  
# et modifié comme suit :  
# - l'extrémité droite de l'une et de l'autre de ces enveloppes n'est pas
# répétée,  
# - le sommet de $Conv(N)$ répète sa base p0.
# 
# Compléter le module précédent avec une fonction `env_convexe(nuage)` qui
# construit l'enveloppe convexe d'un nuage de points arbitraire.

# ### `print_env()`
# 
# Compléter le module précédent avec une fonction qui permet d'afficher l'enveloppe convexe ainsi construite.

# ### `aff_nuage_env()`
# 
# Compléter le module précédent avec une fonction qui permet de tracer graphiquement cette enveloppe convexe, d'abord sans le nuage de points associé, puis avec.

# ### Application à `n10`
# 
# On note `n10` le nuage de points définis par le fichier de données 
# `data_nuage_10.txt`
# 
# Déterminer et tracer l'enveloppe convexe de ce nuage de points.

# ### Application à `n100`
# 
# On note `n100` le nuage de points définis par le fichier de données 
# `data_nuage_100.txt`
# 
# Déterminer et tracer l'enveloppe convexe de ce nuage de points.
