import sqlalchemy 
import psycopg2
from sqlalchemy import create_engine
from Config2 import user,password
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask import Flask,  jsonify, render_template
import numpy as np
app = Flask(__name__)

    #replace the user, password, hostname and database according to your configuration according to your information
  
    
rds_connection_string = f"{user}:{password}@localhost:5432/mobility_db"
engine = create_engine(f'postgresql://{rds_connection_string}')
# def __init__(self):
#     self.connection = self.engine.connect()
#     print("DB Instance created")
    
# def fetchByQyery(self, query):
#     fetchQuery = self.connection.execute(f"SELECT * FROM mobility")
        
#     for data in fetchQuery.fetchall():
#         print(data)

Base = automap_base()

Base.prepare(engine, reflect=True)
Base.classes.keys()
Mob=Base.classes.mobility

# Base = automap_base()
# rds_connection_string = f"{user}:{password}@localhost:5432/mobility_db"
# engine = db.create_engine(f'postgresql://{rds_connection_string}')

# Base.prepare(engine, reflect=True)            
# Meas = Base.classes.mobility

# session = Session(engine)
# max_date=session.query(Meas.date)
# print(max_date)
mob_result=engine.execute('select * from mobility')
# for row in mob_result:
#     print(row)
    
@app.route("/")
def welcome():
    qu= "select * from mobility"
    transit = engine.execute(qu)
    
    for row in transit:
        transit= {"transit_type":row[0]}
    #whatever you get back from the database
    return render_template('index.html', data=transit)
    # """List all available api routes."""
    # return (
    #     f"Available Routes:<br/>"
    #     f"/api/v1.0/mobility<br/>"

# @app.route("/fetch")   
# def fetch():
#     data = #get something from the database
#     return jsonify(data)
    
@app.route("/api/v1.0/mobility")

def all_students():
    qu= "select distinct(geo_type) from mobility"
    transit = engine.execute(qu)
    
    for row in transit:
        transit= {"transit_type":row[0]}
        # transit_data.append(transit)

    # transit_data["transit"] = transit_data
    return transit



if __name__ == '__main__':
    app.run(debug=True)