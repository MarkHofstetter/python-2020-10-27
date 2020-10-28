
#    key        value
teilnehmer = {
    'Mark':     1975,
    'Barabara': 1997,
    'Michael':  1961,
    'Eugene':   1992,
    'Robert':   1978,
    'Klaus':    1974,
    'Andreas':  1987,
    'Andreas':  1986,
    }
    
print(teilnehmer['Andreas'])

teilnehmer['Eva'] = 1980

'''
for name in teilnehmer:
# zu jedem Namen das Geburtsjahr, Ausgabe mit einem Formatstring
    print("Name: {:20s} {:d}".format(name, teilnehmer[name]))
'''

for name, geburtsjahr in teilnehmer.items():
# zu jedem Namen das Geburtsjahr, Ausgabe mit einem Formatstring
    print("Name: {:>20s} {:d}".format(name, geburtsjahr))
