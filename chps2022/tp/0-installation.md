(tp:0-installation)=
# Préparer son ordinateur

Ce document détaille les étapes pour disposer sur votre machine personnelle de l'environnement Python utilisé en Master.


## Pré-requis selon votre OS

### Mac OS

- installer XCode

### Windows

- installer `Firefox` ou `Chrome` car `Jupyert Lab` ne fonctionne pas avec `Internet Explorer`  
- [installer `git`](https://gitforwindows.org)

A partir de maintenant, aucune hypothèse est faite sur l'OS utilisé.
Ce document a été préparé dans un environnement Mac OS Catalina (10.15.7).

## Les étapes pour la première installation

Sauter cette section une fois l'installation effectuée

1. installer la distribution python **3.9** d'[anaconda](https://www.anaconda.com/products/distribution)  
    a. Si anaconda est déjà présent sur votre machine, s'assurer qu'il s'agit bien de la distribution python **3.9**. Dans le cas contraire, [désinstallez](https://docs.anaconda.com/anaconda/install/uninstall/) cette version d'anadonda 
2. récupérer les fichiers suivants :
    a. Pipfile  
    b. Pipfile.lock  


## Utiliser votre environnement

1. Commencer chaque session de travail en activant votre environnement virtuel :

```bash
pipenv shell
```

Votre prompt shell doit maintenant commencer par le nom de l'environnement entre parenthèses, ici '(Python)' :

```bash
(Python) bash-3.2$ 

```

2. Lancer Jupyter Lab avec la commande `jupyter lab` ou `jupyter-lab` 

```bash
(Python) bash-3.2$ jupyter lab
```

3. Dans votre browser web, l'interface de Jupyter Lab est similaire à celui-ci.

![accueil Jupyter Lab](./fig/accueilJlab.png)

- Un nouveau notebook peut être créé et lancé par l'icône de la section `Notebook`  (celui qui indique `ipython`) ou bien sûr via le menu Fichier/Nouveau.
- L'accès et le lancement de notebooks existants s'obtient après avoir cliqué sur l'icône Dossier de la barre latérale (menu vertical à gauche) qui vous permet de vous déplacer dans votre arborescence de travail.

4. Pour terminer _proprement_ votre session 

Une exécution d'un noyau python différent est associé à chaque notebook ouvert.  

- Il est conseillé d'arrêter tout ces noyaux en cours d'exécution via l'icône de la barre latérale : ![icone noyau](./fig/iconenoyaux.png)   
- Remarquez que les onglets des notebooks restent ouverts. 
    - Si besoin, vous relancez le noyau du notebook via l'icône  

## Quelques points techniques importants

## Concilier `pipenv` et `conda`

Suivre [ce point de la documentation de pipenv](https://pipenv.pypa.io/en/latest/advanced/#pipenv-and-other-python-distributions) ou [ce post](https://stackoverflow.com/questions/50546339/pipenv-with-conda).

## Autres références 

- [Un tutoriel](https://zestedesavoir.com/tutoriels/1448/installer-un-environnement-de-developpement-python-avec-conda/)  
- [Un autre](https://www.davidculley.com/installing-python-on-a-mac/) pour mac mais/et en anglais, très complet : le début seul devrait vous suffire.

Le web est bien sûr plein de tutos et autres sites explicatifs ...

## Pour finir

Bon travail : la programmation s'apprend en pratiquant !


