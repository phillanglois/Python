#!/usr/bin/env python
# coding: utf-8

# (ch:synthese)=
# # Synthèse introductive à Python

# *Ce document adapte 
# [ce support](https://github.com/christinaboura/M1-AlgoProg/) 
# aux étudiants du Master CHPS de l'UPVD.*
# 
# Python est un langage de programmation orienté objet (mais oublions le
# côté objet pour l'instant). Sa première version a été écrite en 1991 par Guido
# van Rossum -- qui était un grand fan de Monty Python.
# 
# Ce mini-tutoriel est une introduction très basique et rapide à la
# syntaxe et aux règles du langage. Si vous voulez approfondir plus, 
# des tutoriels bien faits existent sur le net, n'hésitez pas à les
# consulter.
# 
# Nous travaillerons avez l'environnement `Jupyter Lab` et l'interpréteur
# `python3`, le tout au sein d'un environnement virtuel géré par `pipenv`.
# Ce cadre de travail est disponible sur les machines de l'UPVD mais aussi via la
# distribution
# [`anaconda`](https://www.anaconda.com/products/distribution) qu'il est
# conseillé d'installer sur votre machine personnelle.
# 
# Les détails de ces installations sont précisées dans [ce
# document](tp:0-installation) qui vous sera utile pour votre première
# utilisation.
# 
# Nous verrons plus loin comment utiliser les _notebook_ jupyter qui permettent de rassembler dans un seul document du texte formaté (en markdown et LaTeX), du code python, les résultats de ses exécutions (courbes, graphiques, ...), des images ... 
# 
# Commençons par une prise en main simple.

# ## Python en mode calculatrice
# 
# `python3` est accessible directement **dans un terminal** : tapez
# `python3` pour lancer l'interpréteur.
# 
# ```shell
# (Python) bash-3.2$  python3
# ```
# 
# **Remarque**.
# 
# Comme nous le verrons dans [ce document](tp:0-installation), la forme du prompt de ce shell nous indique que l'exécution par le shell `bash` (ici 3.2) de la commande `python3` s'effectue dans l'_environnement virtuel_ '(Python)'.

# La plus simple utilisation de Python est de l'utiliser comme une simple calculatrice. 
# Vous pouvez essayer dans le terminal les calculs suivants.

# ```python
# >>> 2+6
# 8
# >>> 10 - 12   # Les espaces sont optionnels
# -2
# >>> 13 + 2*4  # La priorité des opérations est comme d'habitude
# 21
# >>> 21 / 4    # Attention ! En Python 2 cette instruction retourne 
# 5.25          # la partie  entière de la division. En Python 3 c'est  
#               # une division flottante, même entre deux entiers
# >>> 21 // 4   # Partie entière de la division
# 5
# >>> 21 % 4    # Reste de la division
# 1
# >>> 3 ** 4    # Opérateur puissance (3 à la puissance 4)
# 81
# >>> 10 < 2 * 13  # Comparaison
# True
# >>> 10 < 4 or not 10 < 4  # Connecteurs booléens
# True
# >>> 1 < 2 == 1 + 1 < 3   # Comparaisons chaînées
# True
# ```

# ### Exercice
# 
# Calculer dans un terminal, puis dans la cellule suivante de ce notebook:
# 
# -   $5 \times (1293 - 390)$,
# 
# -   La partie entière ainsi que le reste de la division de 1234 par 7,
# 
# -   $13^{13}$.

# ### Exercice
# 
# Reprendre ces calculs dans la cellule suivante de ce notebook.

# In[ ]:





# ## Données et variables
# 
# Pour pouvoir accéder aux données qu'un programme manipule on fait usage
# d'un nombre de **variables** de différents types. Une variable apparaît
# dans un langage de programmation sous son *nom de variable*, mais il ne
# s'agit de rien d'autre qu'une référence désignant l'adresse mémoire où
# sont stockées les données.
# 
# En Python il existe un nombre de règles simples sur les noms de
# variables qu'il faut respecter :
# 
# -   Seules les lettres a -\> z, A -\> Z, les chiffres 0-9 et le
#     caractère '`_`' sont autorisés.
# -   Le nom d'une variable doit toujours commencer par une lettre.
# -   La casse est significative. Par exemple `vitesse`, `Vitesse` et
#     `VITESSE` désignent des variables différentes.
# 
# Une bonne habitude à prendre est d'écrire les noms de variables en
# minuscules y compris la première lettre. Il s'agit d'une convention qui
# est largement respectée. N'utilisez les majuscules qu'à l'intérieur du
# nom afin de faciliter la lisibilité. Par exemple :
# `matriceDesCoefficients`.

# Le signe '`=`' est utilisé afin d'affecter une valeur à une variable.
# 
# ``` python
# >>> n = 5
# >>> message = 'Bonjour'
# >>> pi = 3.14
# ```

# Les deux constructions suivantes sont très spécifiques à Python. 
# Elles simplifient certaines affectations (la seconde en particulier) mais elle cachent des mécanismes assez sophistiqués sur lesquels nous revenons dans le [chapitre](ch:fonctionsavancees) consacré aux aspects avancés des fonctions.
# Il est donc important de ne pas limiter la compréhension de ces constructions à leur seul aspect syntaxique.
# 
# On peut affecter une valeur à **plusieurs variables simultanément**.
# 
# ``` python
# >>> x = y = z = 1
# >>> x
# 1
# >>> y
# 1
# >>> z
# 1
# ```
# 
# On peut aussi effectuer des **affectations parallèles**.
# 
# ``` python
# >>> x, y = 3.5, 7
# >>> x
# 3.5
# >>> y
# 7
# ```

# **Typage dynamique**
# 
# En Python, contrairement à d'autres langages de programmation, il n'est
# pas nécessaire d'écrire des lignes de code spécifiques pour définir le
# type des variables avant de pouvoir les utiliser. Il suffit d'assigner
# une valeur à un nom de variable pour que celle-ci soit automatiquement
# créée avec le type qui correspond à la valeur fournie. On dit alors que
# Python est un langage à **typage dynamique**, contrairement aux langages
# à **typage statique** comme c'est le cas des langages C ou Java. De
# plus, les variables peuvent changer de type au gré des affectations. On
# peut vérifier ceci avec l'opérateur `type`. Nous y reviendrons au [chapitre consacré aux fonctions](ch:fonctions).
# 
# ``` python
# >>> x = 3
# >>> type(x)
# <class 'int'>
# >>> x = 3.5
# >>> type(x)
# <class 'float'>
# >>> x = 'message'
# >>> type(x)
# <class 'str'>
# ```
# 
# **Annotations de typage** 
# 
# Depuis des versions récentes du langages ($\ge 3.9$), il est très facile de "définir"  le _type_ des paramètres des fonctions et même des variables. 
# "Définir" est entre guillemets car il ne s'agit que d'une **annotation** du type de la variable qui ne remet pas en question le typage dynamique de python. L'intérêt de ces annotations est de permettre un contrôle avant l'exécution d'éventuelles incohérences de typage. Par exemple, un paramètre de type entier utilisé par une chaîne de caractères. Ce contrôle est réalisé par des outils extérieur au langage lui-même comme [mypy](http://mypy-lang.org). 

# **Premières entrées-sorties** 
# 
# - _Fonction_ `print()`. Pour afficher une valeur à l'écran, il
#     existe deux possibilités. Soit, on entre au clavier le nom de la
#     variable et ensuite on appuie sur *Enter* (comme on a fait jusqu'à
#     ici), soit on peut utiliser la fonction `print()`.
# 
# ``` python
# >>> n = 3.5
# >>> print(n)
# 3.5
# >>> msg = 'Ça va ?'
# >>> print(msg)
# Ça va ?
# ```
# 
# **Attention** cependant à la différence entre `print a` (Python 2) et
# `print(a)` (Python 3).
# 
# On peut combiner texte et variables dans une même fonction `print()`.
# 
# ``` python
# >>> poids = 3.67
# >>> print("Le poids du nouveau-né est", poids, "kilos.")
# Le poids du nouveau-né est 3.67 kilos.
# ```

# ### Exercice
# 
# Soient deux points de l'espace $A$ et $B$. Déclarez 4 variables
# $x_A$, $x_B$, $y_A$ et $y_B$ correspondant aux coordonnées
# réelles de ces deux points et affectez-leur des valeurs. Calculez la
# distance euclideienne entre $A$ et $B$, donnée par la formule
# $\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$, et affichez le résultat à
# l'écran sous la forme *La distance entre $A$ et $B$ est : .*
# 
# **Attention !** Vous devez utiliser pour cet exercice la méthode
# `math.sqrt()`. Pour utiliser cette méthode il faut d'abord importer le
# module `math`, avec l'instruction `import math`.

# ## Contrôle du flux d'exécution
# 
# 
# ## Choix ou branchement
# 
# Dans la plupart des programmes que vous allez écrire vous aurez besoin
# d'utiliser des instructions qui permettront au programme de suivre des
# chemins différents selon les circonstances. Pour ceci il est nécessaire
# de disposer d'instructions capables de *tester une certaine condition*
# et de modifier le comportement du programme en conséquence.
# 
# L'instruction qui est sans doute la plus utile afin de permettre un tel
# comportement est l'instruction `if`. Son fonctionnement sous Python est
# très simple. Si la condition à droite du mot-clé `if` est vraie, alors
# le bloc d'instructions en dessus est exécuté.
# 
# ``` python
# >>> if age > 18 :
# ...     print("La personne peut voter.")
# ```

# ### Indentation
# 
# En Python, les instructions composées (comme c'est le cas de
# l'instruction `if`, mais aussi des instructions `while`, `for` et des
# *fonctions* que nous verrons plus tard) ont toujours la même structure :
# une *ligne d'en-tête* terminée par un *deux-points*, suivie d'un bloc
# d'instructions *indenté* sous la ligne d'en-tête. Toutes les instructions
# de ce bloc **doivent être indentées exactement au même niveau**. Une
# convention très respectée est d'utiliser un décalage de 4 espaces.
# 
# Avec une telle convention, il est inutile de marquer le début et la fin
# d'un bloc par des éléments du langage (comme des accolades { et } en C
# ou Java , ou les mots réservés `begin` et `end` dans certains autres
# langages).
# 
# Pour cette raison, en Python on n'est pas libre d'insérer des retours à
# la ligne partout comme en C. Les retours à la ligne sont *obligatoires*
# à la fin d'une instruction, et *permis* à l'intérieur des parenthèses.
# En effet, ce code n'est pas correct :
# 
# ``` python
# if a < 1
#     and b < 2:
#     print('hello')
# ```
# 
# alors que celui-ci l'est :
# 
# ``` python
# if (a < 1
#     and b < 2):
#     print('hello')
# ```

# On peut, si on le souhaite ajouter une instruction `else` pour exécuter
# un autre bloc si la condition est fausse :
# 
# ``` python
# >>> if age > 18:
# ...     print("La personne peut acheter de l'alcool.")
# ... else:
# ...     print("Trop jeune !")
# ```
# 
# Plutôt que d'emboîter des instructions `if`, on peut utiliser une
# instruction `if` suivie par une ou plusieurs instructions `elif`
# (raccourci de *else if*):
# 
# ``` python
# >>> if n == 0:
# ...     print("Le nombre est égal à zéro")
# ... elif n > 0:
# ...     print("Le nombre est positif")
# ... else:
# ...     print("Le nombre est négatif") 
# ```

# ### Exercices
# 
# 1.  Déclarez une variable et affectez lui un entier naturel. Testez en
#     utilisant les instructions `if` et `else` si l'entier est pair ou
#     impair et affichez le résultat.
# 2.  Déclarez trois variables `a`, `b` et `c` correspondant aux
#     coefficients de l'équation quadratique $ax^2 + bx + c = 0$.
#     Calculez le discriminant $\Delta = b^2 - 4ac$ de l'équation.
#     Testez en utilisant les instructions `if`, `elif` et `else` la
#     valeur du déterminant et calculez la ou les solutions de l'équation.
#     Si le déterminant est négatif, affichez le message “*L'équation n'a
#     pas de solution réelle*”.

# ### Boucles ou répétitions
# 
# Très souvent dans nos programmes nous avons besoin de répéter un certain
# nombre d'instructions plusieurs fois. Python, comme probablement tous
# les autres langages que vous connaissez, possède dans ce but les
# instructions `while` et `for`.
# 
# -   La boucle `while` permet d'itérer un bloc d'instructions tant qu'une
#     condition reste vraie.
# 
# ``` python
# >>> a = 0
# >>> while a < 10: # N'oubliez pas le deux-points !
# ...     print(a)   # N'oubliez pas l'indentation !
# ...     a += 2
# ... 
# 0
# 2
# 4
# 6
# 8
# ```

# **`range`**
# Avant d'introduire l'instruction `for` parlons un peu de la fonction
# `range()`. Cette fonction peut nous être très utile lorsque on veut
# itérer sur une suite de nombres. Elle génère des progressions
# arithmétiques.
# 
# ``` python
# range(2, 10) # 2, 3, 4, 5, 6, 7, 8, 9
# range(0, 15, 2) # 0, 2, 4, 6, 8, 10, 12, 14
# range(10, -50, -10) # 10, 0, -10, -20, -30, -40
# ```

# La boucle `for` est très utile lorsque on veut répéter un bloc
# d'instructions un nombre de fois connu à l'avance. Si on veut par
# exemple imprimer tous les nombres de 0 à 5, voici comment on peut le
# faire à l'aide de l'instruction `for` et de la de la fonction `range`.
# 
# ``` python
# >>> for i in range(6): # N'oubliez pas le deux-points !
# ...     print(i)        # N'oubliez pas l'indentation !
# ...
# 0
# 1
# 2
# 3
# 4
# 5
# ```
# 
# Comme on va le voir un peu plus tard, la boucle `for` peut être utilisée
# très facilement pour parcourir les éléments d'une liste.

# ### Exercices
# 
# 1. 
#     a. Initialisez deux entiers : `a = 0` et `b = 15`. Ecrivez une boucle qui
# affiche et incrémente de 1 la valeur de `a` tant qu'elle reste
# inférieure à celle de `b`.
# 
#     b. Ecrivez ensuite une autre boucle qui décrémente la valeur de `b` et
# affiche sa valeur seulement si elle est impaire. Itérez tant que `b` est
# supérieur à 0.
# 
# 2. Affichez la somme des cubes de tous les multiples de 3 compris entre 0
# et 99 inclus. Utilisez pour cela l'instruction `for` et la fonction
# `range()`.

# ## Fonctions
# 
# ### Aspects classiques
# 
# Pour créer une fonction en Python, on commence par le mot-clé `def`
# (définition). Il doit être suivi par le nom de la fonction, la liste des
# paramètres entre parenthèses et un deux-points ‘`:`'. Le corps de la
# fonction commence à la ligne suivante et doit être écrit avec un retrait
# de quelques espaces.
# 
# Voici une fonction qui imprime les `n` premiers termes de la suite *Fibonacci*.

# In[1]:


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print(a)


# In[2]:


fibonacci(20)


# **Rmq.** Cette première fonction n'est pas un "exemple parfait" car elle mélange des calculs et des entrées-sorties. Il est préférable de séparer calculs et des entrées-sorties. 
# 
# On peut bien sûr écrire une fonction qui nous renvoie quelque chose.
# Ceci se fait avec le mot-clé `return`. Voici une fonction qui renvoie la
# somme des carrés des entiers de 0 à `n`.

# In[3]:


def sommeCarres(n):
     sum = 0
     for i in range(n):
         sum += i**2
     return sum


# In[4]:


res = sommeCarres(20)
print(res)


# ### Avec annotations de types
# 
# Comme déjà indiqué, le module `typing` permet de définir des _annotations_ du type des paramètres des fonctions. Les types de base comme `int`, `float`, `str`. Voir plus de détails dans la [PEP 484](https://peps.python.org/pep-0484/).
# Depuis python 3.9, ces annotations incluent les types natifs génériques (c-a-d. les types paramétrables par d'autres types) comme  `list`, `dict`, `tuple`, `set`, ... ainsi que les structures de données du module `collections` -- voir la [PEP 585](https://peps.python.org/pep-0585/) pour plus de détails. 
# 
# Reprenons les fonctions précédentes avec ces annotations.
# 
# - le paramètre `n`  de la fonction `fibonacci()` est un entier `int` et cette fonction ne retourne "rien".  (Par défaut, toute fonction python retourne la valeur `None`. Dans le contexte des annotations de type, `None` désigne `type(None))`. 

# In[5]:


def fibonacci(n: int) -> None:
    '''Cette fonction moche calcule et affiche les 
    n premiers termes de la suite de Fibonacci'''
    a, b = 0, 1
    for i in range(20):
        print(a, end=' ')
        a, b = b, a + b
    print(a)


# In[6]:


from math import log, e
print(e)
help(log)


# In[7]:


help(fibonacci)


# In[8]:


fibonacci(10)


# - la fonction `sommesCarres()` prend et retourne des paramètres de type `int`.

# In[9]:


def sommeCarres(n: int) -> int:
    '''Calcule et retourne la somme des n premiers carrés'''
    sum = 0
    for i in range(n):
        sum += i**2
    return sum

s = sommeCarres(20)
print(s)


# La suite suppose la connaissance de la notion de liste présentée dans cette [section](sec:listes).
# 
# Imaginons maintenant la fonction `sommeListe()` qui effectue la somme d'une liste  de flottants.
# 
# Fabriquons une telle liste pour commencer

# In[10]:


d = [0.0]
for i in range(5):
    d.append(d[-1] + 0.2)
    
print(d)


# **Exercice.** Expliquer pourquoi la valeur `0.6` n'est pas calculée exactement. 
# 
# Effectuons sa somme avec `sommeListe()`.

# In[11]:


def sommeListe(data: list[float]) -> float:
    s = 0.0
    for val in data:
        s = s + val
    return s


# In[12]:


print(sommeListe(d))


# Sommer une liste d'entiers ou de complexes ne change pas notre algorithme. 
# Les annotations permettent cependant de décrire ces cas grâce au mécanisme d'`Union[]` de types (à comprendre comme un ensemble de types possibles). La syntaxe `Union[]` est même remplacé par le symbole classiqiue `|` depuis python 3.10.

# In[13]:


from typing import Union

def sommeListe2(data: Union[list[int], list[float], list[complex]]) \
  -> Union[int, float, complex]:
    s = 0
    for val in data:
        s = s + val
    return s


# In[14]:


d_int = [i for i in range(10)]
d_cmplx = [complex(1, y) for y in range(1, 5)]
print(d_int, sommeListe2(d_int))
print(d_cmplx, sommeListe2(d_cmplx))


# ### Exercice
# 
# Ecrivez une fonction `tableDeMultiplication(base, fin)` qui prend en
# paramètre un entier `base` et un entier `fin` et affiche à l'écran les
# `fin` premiers éléments de la table de multiplication de l'entier
# `base`. Compléter la définition des annotations nécessaires.
# 
# Par exemple :
# 
# ``` python
# >>> tableDeMultiplication(3, 10)
# 0 3 6 9 12 15 18 21 24 27
# ```

# (sec:listes)=
# ## Listes
# 
# Les listes sont des structures ordonnées de données. En Python, une
# liste est définie à l'aide des crochets.

# In[15]:


nombres = [2, 5, 13, -35, 0]
fromages = ['roquefort', 'camembert', 'saint-nectaire', 'comté']


# On peut accéder aux données d'une liste à l'aide de leur indice associé.

# In[16]:


print(nombres[2])


# In[17]:


print(fromages[0])


# In[18]:


print(fromages[-1])


# In[19]:


print(nombres[0:3])


# **Rmq.** La tranche ainsi construite est aussi une liste.

# In[20]:


type(nombres), type(nombres[0:3])


# On peut accéder à la taille d'une liste à l'aide de la fonction `len()`.
# Elle renvoie le nombre d'éléments présents dans la liste.

# In[21]:


print(len(nombres), nombres)


# In[22]:


len(fromages)


# Il existe plusieurs manières de créer une liste. Voici quelques unes :
# 
# -   Liste vide

# In[23]:


liste1 = []


# In[24]:


print(liste1)


# In[25]:


-   On peut créer une liste en indiquant à la création les éléments
    qu'elle doit contenir. Vous pouvez remarquer qu'une liste peut
    contenir d'éléments ayant des types variés.


# In[26]:


liste2 = ['ac/dc', 42, 3.14]


# In[27]:


print(liste2)


# -   **Important.** La syntaxe de *compréhension de listes* permet de générer une
#     liste par une boucle. C'est la forme de création de liste à privilégier en python.

# In[28]:


liste3 = [i for i in range(20)]


# In[29]:


print(liste3)


# In[30]:


-   Liste contenant le carré de tous les entiers de 0 à 9.


# In[31]:


liste4 = [i ** 2 for i in range(10)]


# In[32]:


print(liste4)


# On peut parcourir une liste à l'aide d'une boucle `for` sur les indices des valeurs de la liste :

# In[33]:


nombres = [9, 13, -2, 25, 31, 7, 4]
sum = 0
for i in range(len(nombres)):  # accès par indices aux valeurs de la liste
    sum += nombres[i]


# In[34]:


print(sum)


# Et plus directement (en python) à l'aide d'une boucle `for` sur _les valeurs_ de la liste (on verra plus loin qu'une liste python est un _itérable_) :

# In[35]:


nombres = [9, 13, -2, 25, 31, 7, 4]
sum = 0
for v in nombres:  # accès direct aux valeurs de la liste
     sum += v


# In[36]:


print(sum)


# où à l'aide d'une boucle `while` -- pour un calcul qui n'a rien à voir avec les précédents.

# In[37]:


i = 0
sum = 0
while i < len(nombres):
    sum += i
    i += 3


# In[38]:


print(sum)


# On peut tester si un élément est dans la liste à l'aide de l'instruction
# `in`.

# In[39]:


print(-2 in nombres) 


# In[40]:


print(8 in nombres) 


# Les listes sont des objets (comme tout autre type en Python). Il existe
# plusieurs _méthodes_ déjà définies pour la classe `list` de Python, qu'on
# peut utiliser pour nos listes. Pour utiliser une méthode sur une liste,
# on écrit le nom de la liste, suivi d'un ‘`.`', suivi du nom de la
# méthode.
# 
# **Rmq.** Une méthode est une fonction qui s'applique à un objet.
# 
# Voici quelques méthodes qui peuvent vous être utiles.
# 
# -   La méthode `append(x)` qui permet d'ajouter un élément `x` à la fin
#     d'une liste.
# 
# ``` python
# >>> liste = [0, 3, 1, 5.0, 6, 4.3]
# >>> liste.append(7)
# >>> print(liste)
# [0, 3, 1, 5.0, 6, 4.3, 7]
# ```
# 
# -   La méthode `insert(index,x)`qui insère l'élément `x` à la position
#     `index` de la liste.
# 
# ``` python
# >>> liste.insert(3, 13.2)
# >>> liste
# [0, 3, 1, 13.2, 5.0, 6, 4.3, 7]
# ```
# 
# -   La méthode `remove(x)` qui supprime de la liste le premier élément
#     `x` trouvé.
# 
# ``` python
# >>> liste.remove(13.2)
# >>> liste
# [0, 3, 1, 5.0, 6, 4.3, 7]
# ```
# 
# Cette liste des méthodes est loin d'être exhaustive. 
# Nous donnons plus de détails au [chapitre sur les types composés](ch:typescomposes).
# Vous pouvez aussi trouver plus d'informations sur la page
# [docs.python.org](https://docs.python.org/3.9/tutorial/datastructures.html).

# <div class="alert alert-block alert-warning">
#     
# **WARNING.** Ce qui suit est source d'erreur classique.
# 
# </div>

# **Copie d'une liste**: Que fait le code suivant ?

# In[41]:


L1 = [1, 2, 3, 4, 5, 6]
L2 = L1
print(L2)

L2.append(7)
print(L2)
print(L1)


# En modifiant L2, la liste L1 a été modifiée aussi !
# 
# -   Il ne faut jamais utiliser l'opérateur `=` pour copier une liste.
# 
# -   Les deux objets L1 et L2 partagent la même zone mémoire. Une
#     modification de l'un entraîne une modification de l'autre.
# 
# Nous verrons que les listes sont des **objets mutables**.

# Toutes les méthodes suivantes sont des manières légitimes de
# correctement copier une liste :

# In[42]:


L1 = [1, 2, 3, 4, 5, 6]

L2 = list(L1)  # instanciation d'un nouvel objet list avec les valeurs de la liste L1
L3 = L1.copy() # méthode copy
L4 = L1[:]     # affectation de tranche intégarle
L5 = [i for i in L1] # compréhension d'une liste existante


# On visualisera l'effet de ces commandes avec [python tutor](https://pythontutor.com).

# In[43]:


id(L1) == id(L2)


# ### Exercice
# 
# #### 1
# 
# Définissez la liste `liste = [34, 0, -17, 5, 18, 9]`, puis effectuez les
# actions suivantes :
# 
# -   Triez et affichez la liste.
# 
# -   Ajoutez l'élément 15 à la fin de la liste et affichez la.
# 
# -   Renversez et affichez la liste.
# 
# -   Affichez l'indice de l'élément -17.
# 
# -   Enlevez l'élément 5 et affichez la liste.
# 
# -   Affichez la sous-liste du $2^e$ au $3^e$ élément.
# 
# -   Affichez la sous-liste du début au $4^e$ élément.
# 
# -   Affichez la sous-liste du $3^e$ élément à la fin de la liste.
# 
# -   Affichez l'avant dernier élément en utilisant un indiçage négatif.
# 
# #### 2
# 
# Modifier la fonction `fibonacci(n)` de la Section 5 afin qu'elle renvoie
# une liste avec les `n` premiers termes de la suite Fibonacci.

# ## Exercices
# 
# Vous êtes prêts maintenant à écrire par vous mêmes des programmes un peu
# plus longs et compliqués. 
# 
# - Le notebook est toujours pratique. Utilisez-le.
# - Le mode terminal lui ne l'est plus. 
# - Une alternative est d'utiliser des *scripts* pour écrire, sauvegarder et modifier vos programmes. 
# 
# Pour écrire un script, il suffit de créer un fichier dont le nom se termine par
# `.py` afin d'indiquer qu'il s'agit bien d'un script Python. Vous pouvez
# ensuite l'exécuter dans un terminal en écrivant 

# ```shell
# $ python3 script.py
# ```
# ou dans l'environnement virtuel `monPyhton` que nous mettrons en place en TP :
# 
# ```shell
# $ (monPython) python script.py
# ```

# ### Crible d'Eratosthène
# 
# Le crible d'Eratosthène est un algorithme qui permet de trouver tous les
# nombres premiers qui sont inférieurs à un certain entier naturel $N$.
# Cet algorithme est dû au mathématicien grec Eratosthène de Cyrène qui
# est également connu pour être la première personne à avoir mesuré le
# méridien terrestre.
# 
# L'idée du crible est très simple. On commence par écrire la liste de
# tous les nombres de $2$ jusqu'à $N$. Ensuite on barre (on enlève de
# la liste) tous les multiples de $2$. On note ensuite le plus petit
# nombre non-barré de la liste, qui est donc le nombre 3, et on procède de
# façon similaire en enlevant tous ses multiples. On continue de la même
# façon jusqu'à atteindre le nombre $N$. Les nombres qui restent à la
# fin sont exactement les nombres premiers plus petits ou égaux à $N$.
# 
# Vous pouvez voir une jolie animation de l'exécution de l'algorithme sur
# [la page wikipedia](https://fr.wikipedia.org/wiki/Crible_d%27Ératosthène).
# 
# **Remarque**. En réalité, il suffit de tester uniquement les multiples
# des nombres de 2 à $\sqrt{N}$, puisque un nombre composé plus petit ou
# égal à $N$, a forcément un facteur plus petit ou égal à $\sqrt{N}$.
# 
# Vous devez maintenant programmer le crible d'Eratosthène en Python.
# Ecrivez une fonction `eratosthene(N)` qui prend comme paramètre un
# entier naturel $N$ et qui affiche à l'écran la liste de tous les
# nombres premiers plus petits ou égaux à $N$. Il existe plusieurs
# façons de coder cet algorithme en Python, vous êtes libres de faire à
# votre propre guise.

# ### Recherche dichotomique
# 
# La recherche dichotomique est un algorithme très simple et efficace pour
# rechercher un élément dans une liste **triée**.
# 
# Imaginez par exemple que nous souhaitons retrouver le numéro de
# téléphone d'une personne dans un annuaire qui est trié par ordre
# alphabétique. La recherche séquentielle, c.-à-d. parcourir l'annuaire du
# début en comparant tous les noms avec celui dont on cherche le numéro de
# téléphone peut être très longue (surtout si le nom recherché se trouve à
# la fin de l'annuaire). Une approche bien plus efficace est d'ouvrir
# l'annuaire au milieu et commencer par regarder si le nom se trouve à
# cette page. Si ce n'est pas le cas, et si le nom dont on cherche se
# trouve plus loin, alors on recommence la recherche avec la deuxième
# moitié de l'annuaire. Si le nom se trouve avant, alors on recommence
# avec la première moitié.
# 
# On peut voir qu'avec cette approche, on réduit à chaque étape la taille
# de l'annuaire à parcourir de la moitié. Cet algorithme fait partie alors
# des algorithmes dits *diviser pour régner* et a une complexité
# *logarithmique* en la taille de la liste.
# 
# Pour cet exercice, on suppose que l'utilisateur possède une liste
# croissante de nombres et on lui fournit un nombre qu'on suppose être
# dans la liste. Le but est de retourner l'indice du nombre recherché dans
# la liste.
# 
# Si la liste fournie est \[1,3,4,6,10,14,15\] et l'élément qu'on cherche
# est 10, alors le programme doit retourner 4 (souvenez-vous que, dans une
# liste, les indices sont numérotés à partir de 0).
# 
# Ecrivez une fonction `rechercheDichotomique(valeur, listeTriee)` qui
# prend en entrée une liste triée de nombres et une valeur à rechercher
# dans la liste et renvoie l'indice de la liste correspondant à cette
# valeur.

# In[ ]:




