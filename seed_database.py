"""Seeding my database"""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb therapist')
os.system('createdb therapist')

model.connect_to_db(server.app)
model.db.create_all()

# Load therapist data from JSON file
with open('therapists.json') as f:
    therapist_data = json.loads(f.read())

# Create therapists, store them in list 
therapist_in_db = []
for therapist in therapist_data:
    name, pic, description, phonenum, fp, latitude, longitude, sliding_scale = (therapist['name'],
                                    therapist['pic'],
                                    therapist['description'],
                                    therapist['phonenum'],
                                    therapist['fp'],
                                    therapist['latitude'],
                                    therapist['longitude'],
                                    therapist['sliding_scale'],)

    db_therapist = crud.create_therapist(name,
                                 pic,
                                 description,
                                 phonenum,
                                 fp,
                                 latitude,
                                 longitude,
                                 sliding_scale)
    therapist_in_db.append(db_therapist)