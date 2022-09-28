<!-- #region -->
(ch:bonjour)=
# Bienvenu en Prog Python!

**Ce support est en évolution tout au long du semestre.**

Mis à jour : {sub-ref}`today`, lecture : {sub-ref}`wordcount-minutes` minutes minimum, PhL.


- Vous : **M1 CHPS**  
- Moi : **Philippe Langlois**   
- Comment me contacter : ![](./cm/fig/mail_phl.png)  
- Comment me rencontrer : sur RDV _DEMANDÉ PAR E-MAIL_  
- Où me rencontrer : au bâtiment B, étage 1, à gauche (laboratoire DALI).

Ce support regroupe les ressources de la partie Python de l'UE Programmation du semestre 1 en complément de l'[espace moodle de cette UE](https://cours.univ-perp.fr/course/view.php?id=6237).


:::{important} Dates importantes et contrôle des connaissances.

Les numéros des semaines sont celles du calendrier. 

- semaine 38. Démarrage
- semaine 42. CC : diffusion du sujet
- semaine 44. CC : rendu **dead-line : dimanche 6 novembre 2022, minuit**  
- semaine 48. CT : épreuve sur machine (06.12.22, 15h30-19h30 **date et durée à confirmer**)

Note finale partie Python : $0.5 \times (CC+CT)$
:::


## Travailler en python

Il est indispensable :

- d'avoir accès à un environnement de programmation python, si possible assez complet,

- d'avoir son propre ordinateur configuré de façon complète et selon vos préférences.    

Il y a 3 choix d'OS possibles : windows, linux et mac os ; les 2 premiers étant disponibles sur les ordinateurs de l'UPVD.
Les [distributions python](#En%20pratique) sont assez variées, et peuvent différer selon les OS.
Cependant nous décrirons une solution aussi générique que possible.


**De quoi a-t-on _absolument_ besoin ?**

Ce qui suit est une liste minimale de composants utiles ce deux années
Elle peut sembler longue, mais en pratique ces composants "arrivent" d'un seul coup avec une distribution -- cf. paragraphe suivant.  

- `python` version `**3.9**`

- l'`IDLE` python 3  
    - éditeur, interpréteur, débugger 

- `Jupyter Lab` le successeur de `jupyter notebook`  
    - pour intégrer dans _un unique fichier_ du texte, des maths ($\LaTeX$) et du code python qui s'exécute, les résultats de ces éxecutions (valeurs, courbes, images, ...) et exporter tout ça en `html`ou `pdf` ou en `slide`  
    - très utile pour les exercices 
    - utilisé pour les TP de programmation
    - utilisable dans toutes les matières ou presque    
    
- les gestionnaire de paquets (modules) python pour compléter et mettre à jour son environnement
    - `conda`: plus complet si distribution anaconda utilisée (solution recommandée)  
    - `pip` : autre gestionnaire classique   
    - Exemple d'utilisation : 
        - `conda` : `conda list`, `conda install le_module_que_je_veux` et voilà, c'est fini ! 
        - `pip` : pareil `list`, `update`, `install`  

- les modules indispensables 
    - `numpy ` : fournit des _vrais_ tableaux multi-dimentionnels et des tas de fonctions et types numériques pour effectuer du calcul
    - `matplotlib`: pour le traitement graphique de données, et en particulier :
        -  `matplotlib.pyplot` pour des affichages élaborés
        -  `matplotlib.image`  pour le traitement d'images
    - `tkinter` : pour réaliser des interfaces graphiques  
    
- un module utile  
    - `scipy `: scientific python qui rassemble des modules de calcul scientifiques (dont `numpy`) 

**Pièges**
- Ne pas confondre `python 2` et `python 3` 

**Conseil**
- Choisir une distribution la plus complète possible dès le début.   

**Comment s'y prendre**

Tel est l'objet de [ce document](tp:0-installation)


## Programme de travail

### CM

Séance 1:

- types de données et structures de contrôle de base
- fonctions, modules 
- ES de base

Séance 2

- types de données avancés
- sous-programmes et affectations : aspects avancés
- ES avancées 

Séance 3

- numpy et ndarray
- matplotlib
- mesure de temps d'exécution


### Semaine 38

[**Motto**](https://www.linguee.fr/anglais-francais/traduction/motto.html) : "Pratiquer, pratiquer, pratiquer !"

- Exercices intégrés au chapitre 1 
- Chapitres 1 à 4

Préparation semaine suivante :

- Compétences : Savoir faire et pré-requis technique
- TP : installer l'environnement python et JupyterLab sur sa machine personnelle, savoir utiliser ces ressources sur les ordinateurs de l'UPVD

### Semaine 39

**Motto** : Ecrire une fonction dans l'ordre suivant. 

1. spécification avec annotations de types
2. appels sur premiers tests unitaires avec des `assert`
3. corps de la fonction
4. vérification des tests unitaires

- Chapitres 5, 6 et 7
- Feuille TP 1 


<!-- #endregion -->
