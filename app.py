from flask import Flask, render_template, request

import datetime as dt 
import requests as rq
import json 
from pandas import json_normalize
import time
import pandas as pd 
import numpy as np
import psutil
import os


# import de la classe mediateur 
from server.media import Mediator

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('for2.html')



@app.route('/post_submit_form',methods=['get','post'])
def post_submit_form():

    if request.method == 'POST':

        query = request.form["defined_query"]

    else:
        return 'Error'

    pid = os.getpid()
    py = psutil.Process(pid)
    
    res=Mediator().data(query)
    
    
    return render_template('rslt.html',res=res)






if __name__ == "__main__":
    app.run(debug=True)