"""Seeding my database"""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb therapists')
os.system('createdb therapists')

model.connect_to_db(server.app)
model.db.create_all()

# Load therapist data from JSON file
with open('data/therapists.json') as f:
    therapist_data = json.loads(f.read())

# Create therapists, store them in list 
therapists_in_db = []
for therapist in therapist_data:
    name, phonenum, insurance, location = (therapsts['name'],
                                    therapists['phonenum']
                                    therapists['insurance']
                                    therapists['location'])

    db_therapists = crud.create_therapist(name,
                                 phonenum,
                                 insurance,
                                 location)
    movies_in_db.append(db_movie)