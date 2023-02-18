# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

# Dependencies for SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Flask Dependecy
from flask import Flask, jsonify

# Setting up Database
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

# Reflect database
Base.prepare(engine, reflect=True)
# References for each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Session Link
session = Session(engine)

# #Setting up Flask
app = Flask(__name__)

# Creating Welcome Routes
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

import app

print("example __name__ = %s", __name__)

if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")