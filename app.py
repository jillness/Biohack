import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import sqlite3

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


#################################################
# Database Setup
#################################################
# engine = create_engine("mysql://root:@localhost/Project_Three") <-- tried with mySQL file, did not work so switched to sqlite file
engine = create_engine("sqlite:///NIH_data.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
NIH_Data = Base.classes.nih_data

# Create our session (link) from Python to the DB
session = Session(engine)

#flask setup
app = Flask(__name__)
db = SQLAlchemy(app) 

#querying PI names to test connection, looks like this is working
@app.route("/")
def database():
    results = session.query(NIH_Data.pi).all()

    all_names = list(np.ravel(results))

    return jsonify(all_names)

#testing to see if table is displayed to web. not successful
#get error with db. apparently db not defined but I defined it earlier in the code..?
@app.route("/NIH_Data")
def NIH_Table():
    cursor = db.execute('SELECT column1,column2,column3,column4 FROM NIH_data')
    return render_template('NIH_Data_Web.html', items=cursor.fetchall())


if __name__ == "__main__":
    app.run()