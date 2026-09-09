<!-- #region -->
(ch:bonjour)=
# Bienvenu en Prog Python !

**Ce support est en évolution tout au long du semestre.**

Mis à jour : {sub-ref}`today`, lecture : {sub-ref}`wordcount-minutes` minutes minimum, PhL.


- Vous : **L3 Informatique**  
- Moi : **Philippe Langlois**   
- Comment me contacter : ![](./cm/fig/mail_phl.png)  
- Comment me rencontrer : sur RDV _DEMANDÉ PAR E-MAIL_  
- Où me rencontrer : au bâtiment B, étage 1, à gauche (laboratoire DALI).


## Travailler en python

Il est indispensable :

- d'avoir accès à un environnement de programmation python, si possible assez complet,

- d'avoir son propre ordinateur configuré de façon complète et selon vos préférences.    

Il y a 3 choix d'OS possibles : windows, linux et mac os ; les 2 premiers étant disponibles sur les ordinateurs de l'UPVD.
Les distributions python sont variées et peuvent différer selon les OS.
Cependant nous décrirons une solution aussi générique que possible.


**De quoi a-t-on _absolument_ besoin ?**

Ce qui suit est une liste minimale de composants utiles ce deux années
Elle peut sembler longue, mais en pratique ces composants "arrivent" d'un seul coup avec une distribution -- cf. paragraphe suivant.  

- `python` version `**3.11**` ou supérieures

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


<!-- #endregion -->
