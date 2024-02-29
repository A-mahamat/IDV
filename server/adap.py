import datetime as dt 
import requests as rq
import json 
from pandas import json_normalize
import time
import pandas as pd 
import numpy as np


# Adapters

class Adapter:
    def __init__(self):
        """ The adapater for  Logement API """
        self.ak="test"
        
                              

    def get_data(self,url):
        response = rq.get(url)
        # Vérifiez si la requête a réussi (code de statut HTTP 200)
        if response.status_code == 200:
          # Analysez la réponse JSON
          data = response.json()
          return data
        else:
          return "une erreur s'est produite"