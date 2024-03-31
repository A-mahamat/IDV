





# Système  d’Intégration de Données




![GitHub dev_language](https://img.shields.io/badge/Python-green?style=flat&logo=python&logoColor=white)

![GitHub dev_language](https://img.shields.io/badge/Pandas-6aa84f?style=flat&logo=pandas&logoColor=white)
![GitHub dev_language](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![GitHub dev_language](https://img.shields.io/badge/API-blue?style=flat&logo=fastapi&logoColor=white)





<img src="./Assets/SOIVD-logo-gif.gif">





## le Projet
L'objectif de ce projet est de développer un Système d'Intégration Virtuelle de Données (SIVD) optimisé, qui tirera parti de diverses sources de données liées à l'énergie et aux conditions météorologique 
##### Contexte
● Intégration virtuelle de données provenant de diverses  origines.  

● Multiples  sources d’informations.   



● Exploration de l'architecture médiateur/adaptateur.

● Optimisation des requêtes et selection  de la méthode la plus performante.




##### solution apportée  
Une Application de fusion De Données virtuelle exploitant l'architecture médiateur-adaptateur.
##### Objectif
Consulter de manière cohérente des données multiples.

#### Outils
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

Source de données: Nous utiliserons deux API fournissant des données sur l'utilisation du gaz et de l'électricité dans diverses régions, une autre pour les données démographiques en France, et une dernière pour les informations sur le logement en France.




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
- [1] https://depinfo.u-cergy.fr/~vodislav/Master/IED/fichiers/integration.pdf
- [2] Api logements: https://opendata.caissedesdepots.fr/pages/pagehomerefonte/ 
- [3] Api energie 1 : https://opendata.agenceore.fr/explore/dataset/conso-elec-gaz-annuelle-par-secteur-dactivite-agregee-epci/information/ 
- [4] Api energie 2 : https://odre.opendatasoft.com/explore/dataset/conso-epci-annuelle/ 
- [5] Api population : https://public.opendatasoft.com/explore/dataset/population-francaise-communes/ 
- [6] Flask framework : https://flask.palletsprojects.com/en/2.2.x/ 
- [7] Anaconda distribution : https://docs.anaconda.com/anaconda/ 



