# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
import random
import jeopardy

import requests #To access our API
# -- Initialization section --
app = Flask(__name__)

## secret key for session (In production, you would set this key via an environment variable)
app.secret_key = b'HO\xf8\xff+\n\x1e\\~/;}'

# -- Routes section --
@app.route('/')
@app.route('/index')

def index():
    session["score"] = 0
    return render_template('index.html')
@app.route('/jeopardy/random')
def jeopardy_random():
    #Use jservice API/random to get 1 jeopardy clue
    clue = jeopardy.random_clue()
    session["clue"] = clue
    return render_template('clue.html')

@app.route('/results', methods = ['GET', 'POST'])
def get_results():
    if request.method == 'GET':
        return redirect('/jeopardy/random')
    else:
        form = request.form
        answer = form['input_answer'] 
        if answer == session['clue']['answer']:
            session['score'] += session['clue']['value']
        else:
            session['score'] -= session['clue']['value']    
    
        return render_template('results.html')

    #adding answer
# @app.route('/get_results',methods = ['GET', 'POST'])

# def get_results():
#     if request.method == 'GET':
#         return render_template('clue.html')
#     else: 
#         form = request.form
#         data = jeopardy.find_data(['clue_answer'])
#         return render_template('app.py',data=data)


    # answer = clue.input
    # session["answer"] = answer
    # if  user_input == session['clue']['answer']:
    #     session['score'] += session['clue']['value']
    #     print("Qustion correct!")
    # else:
    #     session['score'] += 0
    #     print("Qustion incorrect!")
    # return render_template('clue.html')

