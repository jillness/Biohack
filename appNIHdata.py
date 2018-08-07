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
#plug in final sqlite file
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

# #querying PI names to test connection, looks like this is working
# @app.route("/")
# def database():
#     results = session.query(NIH_Data.pi).all()

#     all_names = list(np.ravel(results))
#     print(all_names)

#     return jsonify(all_names)

#testing to see if table can be displayed to web (feed database to html)
@app.route("/NIH_Data")
def NIH_Table(db = db):
    #cur = con.cursor()
    #cur.execute("SELECT * FROM NIH_data")
    #data = cur.fetchall()
    #render_template('NIH_Data_Web.html', data=data)
    
    # cursor = session.query(NIH_Data).all()
    # print(cursor)
    #cursor = db.engine.execute(sqlalchemy.text("SELECT * FROM nih_data"))


    cursor = session.query(NIH_Data).all()   
    cursor = list(np.ravel(cursor))
    # print(cursor[0].pi)


    return render_template('NIH_Data_Web.html', items=cursor)



if __name__ == "__main__":
    app.run()