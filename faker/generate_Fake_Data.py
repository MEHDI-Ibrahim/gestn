#!/usr/bin/env python

import random

import mysql.connector             
from mysql.connector import Error  
from faker import Faker

fake = Faker()

conn = mysql.connector.connect(host='db-service', database='gestn',
                               user='lepoxa', password='lepoxa')
cursor = conn.cursor()

matieres = ["Cloud Computing", "Reseau", "Statistiques","Communication","Machine Learning","Analyse Numérique"]
matieresProf = {}
for i in range(6):
    Faker.seed(i+100)
    matieresProf[i]=[fake.email(),fake.password(), fake.last_name(), fake.first_name(), 'prf', matieres[i]]


for i in range(100):
    Faker.seed(i)
    row = []
    row = [fake.email(),fake.password(), fake.last_name(), fake.first_name(), 'etd']

    cursor.execute('INSERT INTO `accountsEtd` (username ,password, nom, prenom, typeAcc) VALUES ("%s", "%s", "%s", "%s", "%s");' % (row[0], row[1], row[2], row[3], row[4]))

for key in matieresProf.keys():
    cursor.execute('INSERT INTO `accountsProf` (username ,password, nom, prenom, typeAcc, matiere) VALUES ("%s", "%s", "%s", "%s", "%s", "%s");' % (matieresProf[key][0], matieresProf[key][1], 
    matieresProf[key][2], matieresProf[key][3], matieresProf[key][4],matieresProf[key][5]))

conn.commit()

# create table accountsEtd(
#      username VARCHAR(50) NOT NULL,
#      password VARCHAR(50) NOT NULL,
     
#      nom VARCHAR(50) NOT NULL,
#      prenom VARCHAR(50) NOT NULL,

#      typeAcc VARCHAR(50) NOT NULL,
#      PRIMARY KEY ( username )
#      );
# insert into accounts values ('poxa','poxa','poxaNom','poxaPrenom','IDSCC','etd')

# create table accountsProf(
#      username VARCHAR(50) NOT NULL,
#      password VARCHAR(50) NOT NULL,
     
#      nom VARCHAR(50) NOT NULL,
#      prenom VARCHAR(50) NOT NULL,

#      typeAcc VARCHAR(50) NOT NULL,
#      matiere VARCHAR(50) NOT NULL,
#      PRIMARY KEY ( username )
#      );