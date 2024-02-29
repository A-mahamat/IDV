# SOIVD – Système Optimisé d’Intégration Virtuelle de Données


# **Projet Chef d'œuvre** 







## About The Project
Le but de ce projet est de créé un Système Optimisé d’Intégration Virtuelle De
Données – SOIVD qui exploitera une bases de données en relation avec
 la météo. 

##### Contexte
● Intégration virtuelle de données provenant de OpenWeather.  

● Évolution vers de grosses quantités de données (Big Data).    

● Des données de plus en plus hétérogènes et interfaces d’accès variées (langages d’interrogation, modèle de données, interface de l'application pour l'utilisateur)

● Exploration de l'architecture médiateur/adaptateur.

● Optimisation des requêtes et le choix de la méthode performante.




##### Solution proposée  
Un Système Optimisé d’Intégration Virtuelle De Données - SOIVD avec une
architecture médiateur-adaptateur et une capacité d’intégration de
de données en temps rèel.

##### Objectif
Mettre en place un système d'intégration de données en temps réel pour la météo, permettant à l'utilisateur de sélectionner une ville de son choix, puis de récupérer et afficher les données météorologiques actuelles de cette ville à l'aide de l'API OpenWeather.

#### Built With
- Python
- Pandas (pandasql)
- APIs
- Flask
- HTML/CSS

## Installation

Use the package manager `pip` to install     
```bash
pip install -r requirements.txt
```
OR      

Use the package manager `pip` to install 

```bash
pip install flask
pip install pandasql
pip install contextlib
pip install bs4
pip install dateutil
```

## Packages

- json : https://docs.python.org/2/library/json.html

- requests : https://fr.python-requests.org/en/latest/

- dateutil : https://dateutil.readthedocs.io/en/stable/

- pandas : https://pandas.pydata.org/docs/

- pandasql : https://pypi.org/project/pandasql/

- termcolor : https://pypi.org/project/termcolor/

- urllib : https://docs.python.org/fr/3/library/urllib.html

- BeautifulSoup : https://www.crummy.com/software/BeautifulSoup/bs4/doc/

- contextlib : https://docs.python.org/3/library/contextlib.html

- flask : https://flask.palletsprojects.com/en/2.2.x/






## Datasets

Choix des Bases de données : Notre sélection des bases de données est guidée par la pertinence par rapport au contexte du réchauffement climatique. Dans cette optique, nous avons décidé d'exploiter une API fournissant des données météorologiques provenant de différentes régions. Pour l'instant, notre focus se porte principalement sur quelques villes en France. Cependant, nos plans incluent une expansion future vers d'autres régions du monde, afin d'explorer les perspectives globales du changement climatique.

### Description de l'API

| API                                                                                                                                 | Description                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| [API ](<https://openweathermap.org/current>) | Le jeu de données météorologiques disponible sur le site **OpenWeather** offre des renseignements sur le climat de toute localité à travers le monde. Ces données sont recueillies à partir de diverses sources telles que des satellites, des radars et un large réseau de stations météorologiques, entre autres. |





## Mise en place de l'environnement Flask
 - Création d'un environnement virtuel soit avec anaconda soit avec la commande -m venv <environment name> sous python
 - Dans le cas où l'env virtuel est crée par Anaconda, il faut spécifier dans le anaconda prompt : conda activate <environment name>
 - Pointer sur le dossier api_flask  (./api_flask)
 - Installer les bibliothèques nécessaires dans le fichier requirements.txt (Flask, requests, json, ...)

#### Exécution de l'app Flask
 - Dans la commande prompt d'anaconda : 
     1) set FLASK_APP=app.py
     2) set FLASK_ENV=development
     3) flask run
 - Taper dans l'url :  http://127.0.0.1:5000/
 - Obtenir les résultats affichés dans la page web
 

## Références:
-
- [1] A. R. J. O. Alon Halevy, «Data Integration: The Teenage Years,» VLDB Endowment, p. 8, 2006.
- [2] A. H. G. M. W.-C. T. Behzad Golshan, «Data Integration: After the Teenage Years,» PODS’17, p. 6, 2017.
-[3] Tutoriel API météo en R: https://www.youtube.com/watch?v=IkJ8Sx3yBwg
- [4] Flask framework : https://flask.palletsprojects.com/en/2.2.x/ 
- [5] Anaconda distribution : https://docs.anaconda.com/anaconda/ 



