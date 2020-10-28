import pprint

teilnehmer = {
    'Mark':     {'yob': 1975, 'fav_col': 'blau'},
    'Barabara': {'yob': 1997, 'fav_col': 'grün'},
    'Michael':  {'yob': 1961, 'fav_col': 'gelb', 'edu': [ 'vs', 'uni']},
    'Eugene':   1992,
    'Robert':   1978,
    'Klaus':    1974,
    'Andreas':  1987,
    'Andreas':  1986,
    }

# print(teilnehmer['Michael']['edu'][-1])
pprint.pprint(teilnehmer)
exit()

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

teilnehmer |= teilnehmer_old
    
'''
Benutzereingabe "Namen"
Ausgabe des Geburtsdatums (und optional der Lieblingfarbe)

1. mit try/except
und/oder 2. if
'''

search = input("Teilnehmername: ")
try:
    tn = teilnehmer[search]
except KeyError:
    print("Teilnehmer existiert nicht")
    exit()
    
'''    
try: 
    yob = tn['yob']
except TypeError:
    yob = tn
'''

if isinstance(tn, dict):
    yob = tn['yob']    
else:
    yob = tn
    
print("Name: {:20s} {:d}".format(search, yob))    

