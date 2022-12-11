#!/usr/bin/env python

import random

import mysql.connector             
from mysql.connector import Error  
from faker import Faker

fake = Faker()

conn = mysql.connector.connect(host='db-service', database='gestn',
                               user='lepoxa', password='lepoxa')
matieres = ["Cloud Computing", "Reseau", "Statistiques","Communication","Machine Learning","Analyse Numérique"]

cursor = conn.cursor()
for i in range(100):
    Faker.seed(i)
    row = [fake.email(),'',0]
    for j in range(len(matieres)):
        Faker.seed(i)
        row[1] = matieres[j]
        row[2] = random.randint(10,20)
        cursor.execute('INSERT INTO `notes` (username ,matiere, note) VALUES ("%s", "%s", "%d");' % (row[0], row[1], row[2]))
conn.commit()


# create table notes(
#      username VARCHAR(50) NOT NULL,
#      matiere VARCHAR(50) NOT NULL,
#      note integer(10) NOT NULL
#      );
# insert into accounts values ('poxa','poxa','poxaNom','poxaPrenom','IDSCC','etd')