from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, session
import requests
import os


import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="lepoxa",
    password="lepoxa",
    database="gestn"
)
# Flask constructor
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/test')
def test():
    # Check if user is loggedin
    return render_template('index.html', msg="tested")


@app.route('/home')
def home():
    # Check if user is loggedin
    if session['typeAcc'] == "Etudiant":
        return redirect('/etudiant')

    if session['typeAcc'] == "Professeur":
        return redirect('/prof')
    if session['typeAcc'] == "Administration":
        return redirect('/admin')

    # if 'loggedin' in session:
    #     return render_template('index.html', msg='')

    # else:
    #     return redirect('https://localhost:5050/home')


@app.route('/etudiant')
def etudiant():
  cursor = mydb.cursor(buffered=True)
  # select etd.username, nt.note from accountsEtd as etd, notes as nt where etd.username = nt.username;
  cursor.execute('select etd.username, nt.note, nt.matiere from accountsEtd as etd, notes as nt where etd.username = nt.username and etd.username = %s;', (session['username'],))
  # Fetch one record and return result
  #select etd.username, nt.note, nt.matiere from accountsEtd as etd, notes as nt where etd.username = nt.username and etd.username =xroman@example.com;
  #8@Vi6PBo#H /  xroman@example.com
  data = cursor.fetchall()
  if data:
    return render_template('etd.html', data=data)
  else:
    return render_template('index.html', msg='Erreur, veuillez consulter votre administration')



@app.route('/prof')
def prof():
  cursor = mydb.cursor(buffered=True)
  # select etd.username, nt.note from accountsEtd as etd, notes as nt where etd.username = nt.username;
  cursor.execute('select etd.username, nt.note, nt.matiere from accountsEtd as etd, notes as nt where etd.username = nt.username and nt.matiere = %s;', (session['matiere'],))
  # Fetch one record and return result
  # select etd.username, nt.note, nt.matiere from accountsEtd as etd, notes as nt where nt.matiere = 'Reseau' group by etd.username;
  #8@Vi6PBo#H /  xroman@example.com
  data = cursor.fetchall()
  if data:
    return render_template('prf.html', data=data)
  else:
    return render_template('index.html', msg='Erreur, veuillez consulter votre administration')

@app.route('/profModifier')
def profModifier():
  pass


if __name__ == '__main__':
    app.run(debug=True, port=5051, host="0.0.0.0", use_reloader=True)
