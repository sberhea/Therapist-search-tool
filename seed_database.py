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
    name, pic, description, phonenum, fp, latitude, longitude, sliding_scale = (therapsts['name'],
                                    therapists['pic'],
                                    therapists['description'],
                                    therapists['phonenum'],
                                    therapists['fp'],
                                    therapists['latitude'],
                                    therapists['longitude'],
                                    therapists['sliding_scale'],)

    db_therapists = crud.create_therapist(name,
                                 pic,
                                 description,
                                 phonenum,
                                 fp,
                                 latitude,
                                 longitude,
                                 sliding_scale)
    therapists_in_db.append(db_therapists)