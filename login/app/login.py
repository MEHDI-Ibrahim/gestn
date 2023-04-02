# importing Flask and other modules
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, session
import requests
import os
from datetime import timedelta

import mysql.connector

mydb = mysql.connector.connect(
    host="db-service",
    user="lepoxa",
    password="lepoxa",
    database="gestn"
)


# Flask constructor
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods=["GET"])
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return redirect('localhost:5051/home')
    # User is not loggedin redirect to login page

    else:
        return render_template('index.html', msg='')



# @app.route('/clearSession')
# def clrs():
# 	session.clear()
# 	return redirect('localhost:5050/')



@app.route('/register', methods=['POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST':

        # Create variables for easy access
        username = request.form.get("uname", False)
        password = request.form.get("psw", False)
        # Check if account exists using MySQL
        cursor = mydb.cursor(buffered=True)
        cursor.execute('SELECT * FROM accountsEtd WHERE username = %s AND password = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
        if account:
            # session.permanent = True
            # app.permanent_session_lifetime = timedelta(seconds=60)
            session['loggedin'] = True
            session['username'] = account[0]
            session['nom'] = account[2]
            session['prenom'] = account[3]
            session['typeAcc'] = "Etudiant"
            return redirect('http://localhost:5051/home')
            # return render_template('index.html', msg=account)
        cursor.execute('SELECT * FROM accountsProf WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        if account:
            # session.permanent = True
            # app.permanent_session_lifetime = timedelta(seconds=60)
            session['loggedin'] = True
            session['username'] = account[0]
            session['nom'] = account[2]
            session['prenom'] = account[3]
            session['typeAcc'] = "Professeur"
            session['matiere'] = account[5]
            return redirect('http://localhost:5051/home')
        else:
            msg = 'User ou mot de passe incorrect!'
            return render_template('index.html', msg='User ou mot de passe incorrect!')
    

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5050 ,use_reloader=True)


# example 'wolfemallory@example.org'  'U(58_QBXei'


# create table accounts(
#     -> username VARCHAR(50) NOT NULL,
#     -> password VARCHAR(50) NOT NULL,
#     -> 
#     -> nom VARCHAR(50) NOT NULL,
#     -> prenom VARCHAR(50) NOT NULL,
#     -> filiere VARCHAR(50) NOT NULL,
#     -> 
#     -> typeAcc VARCHAR(50) NOT NULL,
#     -> PRIMARY KEY ( username )
#     -> );