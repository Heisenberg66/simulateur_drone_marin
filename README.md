# Stage L3 2017

[![N|Solid](http://digidoc.labri.fr/img/l3i.jpg)](https://nodesource.com/products/nsolid)

### Developpement d’un simulateur de navigation pour un drone marin de surface avec une IA detecteur d’obstacles. 
### Utilisation des approches d’apprentissage par renforcement (reinforcement learning)

- Encadrants Michel Menard, Bruno Lescalier
- laboratoire L3i
- Développement en Python

#### Principe de fonctionnement (pour l'instant) 

Clic gauche sur la carte pour placer un marker, clic droit pour le supprimer. Bouton Clear pour supprimmer tous les markers. Bouton Start pour lancer la simulation. 
Le "bateau" va suivre le trajet, les rayons détectent les obstacles fixes (pontons, plage,...) mais ne les évite pas pour l'instant. 
Le simulateur affiche aussi 5bateaux

#### Description des classes  
#
- fenetre.py : initialisation + boucle d'événements
- Button.py : création des objets "boutons" (start/stop et clear)
- MarkerMap : coordonnées et image des markers
- boat.py : hérite de Pymunk.body, gestion des mouvments du drone et s des bateaux simulés
- arm_sonar : création, translation, rotation d'un bras du sonar
- point_sonar : création, translation, rotation d'un point d'un bras  du sonar
- init_trajet_boat : création de 12 trajets pour les bateaux simulés
- trajet_bateau : déplacement sur un trajet d'un bateau simulé
- simulation_bateau : gestion des trajets de tous les bateaux simulés


[![N|Solid](https://image.noelshack.com/fichiers/2017/18/1493975328-capture-d-ecran-2017-05-05-a-10-26-32.png)](https://nodesource.com/products/nsolid)

[![N|Solid](https://image.noelshack.com/fichiers/2017/22/1496051495-capture-d-ecran-2017-05-28-a-14-28-19.png)](https://nodesource.com/products/nsolid)

### Installation 

| util | lien |
|-----|-------|
|OS| [Mac osX Sierra 10.12.1] |
|langage | [python 2.7]
|environnement|[Anaconda-navigator] |
|librairie 1 | [pygame] |
|librairie 2 | [pymunk] |
|librairie 3 | [numpy] |
|librairie 4 | [tensorflow] |

##### Anaconda-navigator

Pour installer Ananconda sur mac OSX, cliquez [ici] et suivez le tutoriel.

Une fois installer, lancez le navigateur anaconda puis cliquez sur l'onglez ***environnements***. 
Cliquez ,en bas de la fenêtre, ensuite sur le bouton ***create***. 
Entrez un *nom_environnement* et selectionner python 2.7.

Votre environnement anaconda est maintenant créé, cliquez sur cette environnement, cliquez sur la flèche à du nom et selectionnez ***Open terminal***

##### Pygame 

Dans le terminal de l'environnement que vous venez de créer, entrez la commande suivante

```sh
$ pip install pygame
```

##### Pymunk 
Pymunk est un moteur physique sous python qui va nous permettre de gerer les collisions et les déplacements de nos objects.
```sh
$ pip install pymunk
```

##### Numpy
Librairie capable de faire des opérations mathématiques complexes.

```sh
$ pip install numpy
```

##### tensorflow
Librairie pour le deep learning 

```sh
$ pip install --ignore-installed –upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.1.0-py2-none-any.whl
```

### Utilisation

Pour lancer le simulateur, entrez la commande si dessous : 

```sh
$ python fenetre.py
```


[ici]: <https://docs.continuum.io/anaconda/install-macos>
[Anaconda-navigator]: <https://docs.continuum.io/>
[Mac osX Sierra 10.12.1]:<https://www.apple.com/fr/macos/sierra/>
[python 2.7]:<https://www.python.org/>
[pygame]:<https://www.pygame.org/news>
[pymunk]:<http://www.pymunk.org/en/latest/>
[numpy]:<http://www.numpy.org/>
[tensorflow]:<https://www.tensorflow.org/>
