(tp:0-installation)=
# Préparer son ordinateur et travailler avec Python et JupyterLab

Ce document détaille les étapes pour disposer sur votre machine personnelle de l'environnement Python utile en programmation scientifique et dans le Master, puis comment profiter de l'environnement de développement JupyterLab.


## Préparer son ordinateur

### Pourquoi installer un environnement sur sa machine ...

... et ne pas simplement utiliser [Google Colab](https://colab.research.google.com/?hl=fr) ?

Il est commode d'utiliser _ponctuellement_ cette ressource. 
Alors pourquoi  "perdre du temps" à installer un environnement Python _qui fonctionne_ sur sa machine ? 
La question est légitime. 
Je partage entièrement les arguments pros/cons développés dans ce [bootcamp](http://justinbois.github.io/bootcamp/2020_fsri/lessons/l00_configuring_your_computer.html#Why-install-on-my-own-machine?) d'apprentissage de la programmation scientifique en Python.

### Pré-requis selon votre OS

#### Mac OS

- installer XCode

#### Windows

- installer `Firefox` ou `Chrome` car `Jupyter Lab` ne fonctionne pas avec `Internet Explorer`. 
    - **Rmq.** `Jupyter Lab` fonctionne avec le browser récent `Microsoft Edge` 
- [installer `git`](https://gitforwindows.org)

A partir de maintenant, aucune hypothèse est faite sur l'OS utilisé.
Ce document a été préparé dans un environnement Mac OS Catalina (10.15.7).
Selon votre système, quelques différences peuvent exister.

### Les étapes pour la première installation

Sauter cette section une fois l'installation effectuée

On va installer une distribution python : [anaconda](https://www.anaconda.com/) ou [miniconda](https://docs.conda.io/en/latest/miniconda.html) si votre espace disque est réduit.
Puis on va créer un environnement virtuel qui permet de séparer l'espace de _votre_ travail Python de [celui de la distribution](sec:root) ou de versions de Python déjà présentes sur votre machine. 
Ainsi vous serez propriétaire et gestionnaire de cet environnement (monPython) dans lequel vous installerez les modules dont vous avez besoin pour votre projet.
Il est classique de créer un environnement de travail spécifique à chaque projet que l'on développe.

1. installer la distribution python **3.9** d'[anaconda](https://www.anaconda.com/products/distribution)  
    - Il suffit de télécharger le fichier proposé (ça peut être un peu long) et l'installer simplement en cliquant
    - Si anaconda est déjà présent sur votre machine, s'assurer qu'il s'agit bien de la distribution python **3.9**. Dans le cas contraire, [désinstallez](https://docs.anaconda.com/anaconda/install/uninstall/) cette version d'anaconda 
    - L'installation prend du temps et nécessite une connection internet. Elle peut régulièrement vous demander d'installer une nouvelle version d'un des nombreux composants de la distribution.
2. créer un environnement virtuel (par exemple `monPython`) 
    - en ligne de commande (si besoin s'aider de cette [page](https://www.pythoniste.fr/anaconda/les-environnements-virtuels-en-python-avec-anaconda/) ou de [celle-ci](https://fr.acervolima.com/configurer-un-environnement-virtuel-pour-python-a-laide-danaconda/)) :
    ```shell
    conda create -n monPython python=3.9
    ```  
    - ou en utilisant l'interface graphique du navigateur anaconda :
    ![creer environnement via navigateur](fig/navigator-create-environment.png)
3. installer [les modules utiles](sec:modules) dans `(monPython)`
    - un à un avec la commande `conda install ...`
    - ou en utilisant l'interface graphique du navigateur anaconda.
    
Ca y est : vous pouvez enfin commencer à travailler dans un cadre que vous maîtrisez entièrement.

(sec:root)=
#### Note concernant anaconda sur Windows

L'installation d'anaconda sous windows s'effectue en mode `root`. 
Si vous n'êtes pas (`root`) sur votre machine, le lancement de certaines applications peut vous être refusé.
En revanche, vous êtes propriétaire de tout environnement que vous créez.


(sec:modules)=
### Liste des modules utiles

- `numpy`
- `matplotlib`
- `jupyterlab`
- `jupyterlab-spellchecker`
- `jupyterlab-language-pack-fr-fr`
- `jupyterlab-mathjax3`

### Autres références pour l'installation

- [Un tutoriel en français](https://zestedesavoir.com/tutoriels/1448/installer-un-environnement-de-developpement-python-avec-conda/) .
- [Un autre en anglais](https://www.dataquest.io/blog/installing-python-on-mac/) et très complet.

Le web est bien sûr plein de tutos et autres sites explicatifs ...


## Utiliser votre environnement

1. Commencer chaque session de travail en activant votre environnement virtuel :

```bash
conda activate monPython
```

Votre prompt shell doit maintenant commencer par le nom de l'environnement entre parenthèses, ici '(monPython)' :

```bash
(monPython) bash-3.2$ 
```

2. Lancer Jupyter Lab :  
- en ligne de commande (dans un terminal), avec la commande `jupyter lab` ou `jupyter-lab` 
```bash
(monPython) bash-3.2$ jupyter lab
```
- via l'interface graphique du navigateur anaconda :
![jupyterlab par anaconda](fig/anaconda-jupyterlab.png)


3. Jupyter Lab s'ouvre dans votre browser web. Son interface est similaire à celle-ci.

![accueil Jupyter Lab](./fig/accueilJlab.png)

- Un nouveau notebook peut être créé et lancé par l'icône de la section `Notebook`  (celui qui indique `ipykernel`) ou bien sûr via le menu Fichier/Nouveau.
- L'accès et le lancement de notebooks existants s'obtient après avoir cliqué sur l'icône Dossier de la barre latérale (menu vertical à gauche) qui vous permet de vous déplacer dans votre arborescence de travail.
- L'interface de `Jupyter Lab` permet de créer des fichiers d'un format différent de celui des notebooks (`.ipynb`) : markdown (`.md`), pyhtin (`.py`) ou texte (`.txt`) plus simplement, de lancer une session terminal (dans votre environnement (monPython))  

4. Pour terminer _proprement_ votre session 

Une exécution d'un noyau python différent est associé à chaque notebook ouvert.  

- Il est conseillé d'arrêter tout ces noyaux en cours d'exécution via l'icône de la barre latérale : ![icone noyau](./fig/iconenoyaux.png)   
- Remarquez que les onglets des notebooks restent ouverts. 
    - Si besoin, vous relancez le noyau du notebook via l'icône  

(sec:jupyter)=
## Jupyter et ses notebooks

Ce [chapitre sur Jupyter](https://python.sdv.univ-paris-diderot.fr/18_jupyter/) extrait du cours en ligne du master de Biologie Informatique de l'université Paris Diderot - Paris 7 (devenue Université Paris Cité) vous permettra d'utiliser rapidement les notebooks de `Jupyter Lab` ou de `Jupyter` son prédécesseur.

Vous étudierez en particulier les sections suivantes.

### Créer et utiliser des notebooks

On a montré plus haut comment créer un notebook dans `Jupyter Lab`.
Ensuite, l'utilisation des notebooks est identique dans `Jupyter Lab` et `Jupyter`.
Les [principes de création et d'utilisation des notebooks](https://python.sdv.univ-paris-diderot.fr/18_jupyter/#182-lancement-de-jupyter-et-creation-dun-notebook) sont présentés ici dans l'environnement `Jupyter`. 

### Jupyter Lab

Les spécificités de [Jupyter Lab](https://python.sdv.univ-paris-diderot.fr/18_jupyter/#186-jupyterlab) par rapport à `Jupyter` y sont rapidement présentées.

### Le format markdown

Le [format markdown](https://python.sdv.univ-paris-diderot.fr/18_jupyter/#183-le-format-markdown) permet d'écrire du texte mis en forme de fort belle façon pour une sortie à l'écran, en html ou en pdf. 
Il est décliné dans plusieurs variantes -- par exemple [GitHub Flavored Markdown](https://fr.wikipedia.org/wiki/GitHub_Flavored_Markdown) utilisée dans [github](https://github.com).
Ce langage de balisage léger s'utilise facilement dans le notebook jupyter ou "seul". 
Dans ce cas, on profitera du très puissant convertisseur de formats de documents [pandoc](https://pandoc.org).


### Compléments

Et dans un second temps, vous lirez les sections plus spécifiques sur les [graphiques dans les notebooks](https://python.sdv.univ-paris-diderot.fr/18_jupyter/#184-des-graphiques-dans-les-notebooks) et les très pratiques [_magic commands_](https://python.sdv.univ-paris-diderot.fr/18_jupyter/#185-les-magic-commands).


## Pour finir

Bon travail : la programmation s'apprend en pratiquant !


