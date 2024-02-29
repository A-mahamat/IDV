import datetime as dt 
import requests as rq
import json 
from pandas import json_normalize
import time
import pandas as pd 
import numpy as np
from server.adap import Adapter



class Mediator:
  def __init__(self):
    self.ada="test"
    

  def data(self,rqt):
    api_key="99cd4f9e9090da6790eea9baf6d75704"
    url=f'https://api.openweathermap.org/data/2.5/weather?q={rqt}&appid={api_key}'
    
    weather_data=Adapter().get_data(url)
    if weather_data:
      # Traitement des données météorologiques
      temp_kelvin = weather_data['main']['temp']
      temp_celsius = temp_kelvin - 273.15
      # Préparation des données pour affichage
      latitude = weather_data['coord']['lat']
      longitude = weather_data['coord']['lon']
      # Préparation des données pour affichage
      processed_data = {
          'Ville': weather_data['name'],
          'Description': weather_data['weather'][0]['description'],
          'Température': round(temp_celsius, 2),
          'Humidité': weather_data['main']['humidity'],
          'Pression': weather_data['main']['pressure'],
          'Vitesse_du_vent': weather_data['wind']['speed'],
          'Direction_du_vent': weather_data['wind']['deg'],
          'latitude':latitude,
          'longitude':longitude
          }
      return processed_data
    else:
      return None


