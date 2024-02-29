# SOIVD – Système Optimisé d’Intégration Virtuelle de Données






<img src="./Assets/SOIVD-logo-gif.gif">

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

## Conception
La figure ci-dessus représente l'architecture adoptée pour la réalisation du présent projet. Il s'agit d'une architecture Adaptateur-Médiateur dont nous allons utiliser l'approche GAV
<img src="./Assets/SOIVD_Global_architecture.png">

Diagramme de séquence
<img src="./Assets/SOIVD_Sequence_diagram.png">


## Datasets

"Choix des Bases de données : Notre sélection des bases de données est guidée par la pertinence par rapport au contexte du réchauffement climatique. Dans cette optique, nous avons décidé d'exploiter une API fournissant des données météorologiques provenant de différentes régions. Pour l'instant, notre focus se porte principalement sur quelques villes en France. Cependant, nos plans incluent une expansion future vers d'autres régions du monde, afin d'explorer les perspectives globales du changement climatique."

### Description de l'API

| API                                                                                                                                 | Description                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| [API ](<https://openweathermap.org/current>) | Le jeu de données météorologiques disponible sur le site **OpenWeather** offre des renseignements sur le climat de toute localité à travers le monde. Ces données sont recueillies à partir de diverses sources telles que des satellites, des radars et un large réseau de stations météorologiques, entre autres. |





## Mise en place de l'environnement Flask
 - Création d'un environnement virtuel soit avec anaconda soit avec la commande -m venv <environment name> sous python
 - Dans le cas où l'env virtuel est crée par Anaconda, il faut spécifier dans le anaconda prompt : conda activate <environment name>
 - Pointer sur le dossier api_flask  (./api_flask)
 - Installer les bibliothèques nécessaires dans le fichier requirements.txt (Flask, requests, json, ...)
#### Exploration de l'architecture du projet flask 
 - Dossier static : contient tous les fichiers de style et les images si vous aurez besoin
 - Dossier templates : contient tous les fichiers html pour la partie front-end du projet
#### Exécution de l'app Flask
 - Dans la commande prompt d'anaconda : 
     1) set FLASK_APP=app.py
     2) set FLASK_ENV=development
     3) flask run
 - Taper dans l'url :  http://127.0.0.1:5000/
 - Obtenir les résultats affichés dans la page web
 
#### Affichage:
![alt text](https://imagizer.imageshack.com/img922/8676/2o56BP.png)
![alt text](https://imagizer.imageshack.com/img923/2163/d1oSyG.png)
## Références:
- [1] S. A. Y. P. V. S. S. Adah, «Query Caching and Optimization in Distributed Mediator Systems,» SIGMOD, p. 12, 1996.
- [2] A. R. J. O. Alon Halevy, «Data Integration: The Teenage Years,» VLDB Endowment, p. 8, 2006.
- [3] A. H. G. M. W.-C. T. Behzad Golshan, «Data Integration: After the Teenage Years,» PODS’17, p. 6, 2017.
- [4] P. K. P. S. G. A. A. J. R. B. S. D. G. H. L. P. M. S. M. E. P. H. Z. AnHai Doan, «Toward a System Building Agenda for Data Integration (and Data Science),» IEEE, p. 12.
- [5] G. Wiederhold, «Mediators in the Architecture of Future Information Systems,» IEEE, p. 38, 1991.
- [6] Api de logements sociaux et bailleurs par région : https://opendata.caissedesdepots.fr/pages/pagehomerefonte/ 
- [7] Api energie 1 :consommation quotidienne brute r ́egional electricit ́e ou de gaz : https://opendata.agenceore.fr/explore/dataset/conso-elec-gaz-annuelle-par-secteur-dactivite-agregee-epci/information/ 
- [8] Api energie 2 : Production demi-horaire agrégée par région : https://odre.opendatasoft.com/explore/dataset/conso-epci-annuelle/ 
- [9] Api population : informations démographiques sur les communes en France : https://public.opendatasoft.com/explore/dataset/population-francaise-communes/ 
- [10] Flask framework : https://flask.palletsprojects.com/en/2.2.x/ 
- [11] Anaconda distribution : https://docs.anaconda.com/anaconda/ 



