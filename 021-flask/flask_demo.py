from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS, cross_origin
from Model import *

app = FlaskAPI(__name__)
cors = CORS(app)

teilnehmer_old = {
    'Mark'      : {'yob': 1977, 'fav_col': 'gruen', 'edu': ['vs', 'gym', 'uni']},
    'Herbert'   : {'yob': 1973, 'edu': [ 'vs', 'gym', 'htl', 'uni']},
    'Stefan'    : {'yob':1976},
    'Johann'    : {'yob':1987},
    'Marian'    : {'yob':1980},
    'Magdalena' : {'yob':1982},
    'Stefan'    : {'yob':1983},
    'Kurt'      : {'yob':1995},
    'Karl'      : {'yob':1960},
    'Latchezar' : {'yob':1972},
    }

@app.route("/", methods=["GET"])
def welcome():
    return {'data': 'Hello World'}
    

@app.route("/add/<int:number1>/<int:number2>", methods=["GET"])
def add(number1, number2):
    return {'number': number1 + number2}

# add "search" route die die Daten für einn TN retourniert
# search/Stefan => 'Stefan'    : {'yob':1976}  => wie einpacken?
@app.route("/search/<string:name>", methods=["GET"])
def search(name):
    try:
        return {'data': {name: teilnehmer_old[name]}}
    except KeyError:
        return {'error': 'user not found'}, 404 

@app.route("/searchdb/<string:name>", methods=["GET"])
def searchdb(name):
    session = get_session()
    student_query = session.query(Student).filter(Student.name.contains(name))    
    result = {'data': []}
    for student in student_query.all():
        result['data'].append(student.name)    
    
    if not result['data']:
        return {'error': 'nothing found'}, 404
    
    return result
    
    
        
    
if __name__ == '__main__':
    app.run(debug=True)