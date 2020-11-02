
'''

+ 
+ komma (,) mit . Ersetzen => float

+ Durchschnittpreis je Brennstoff
+ Preisverlaufsgraph

(+ Maximalpreis pro Brennstoff und in welchem Jahr) => am Ende

Preise in EUR;;;;;;;;;;;;;
Nettopreis;2003;2004;2005;2006;2007;2008;2009;2010;2011;2012;2013;2014;2015
 Heizoel schwer (Industrie)/t ;162,38;154;224,92;267,54;278,98;392,05;283,68;386,12;504,2;573,75;511,77;472,79;332,34
 Heizoel schwer (Kraftwerke)/t ;121,88;115,74;138,96;165,27;153,14;226,44;144,04;271,95;320,06;493,1;473,35;340,29;331,06
''' 

import csv
from pprint import pprint
import numpy as np
from matplotlib import pyplot as plt

with open('daten.csv') as datafile:
    rows = csv.reader(datafile, delimiter=';')
    rows = list(rows)
    data = {}
    for row in rows[2:]:
        # print(row[0])
        val = row.pop(0).strip()
        '''
        data[val] = []        
        for n in row:
            data[val].append( float(n.replace(',', '.')) )
        '''
        data[val] = [ float(n.replace(',', '.')) for n in row]
        print("{:<40s}  {:.3f}".format(val, np.mean(data[val])))
        plt.plot(rows[1][1:], data[val], label = val)

plt.legend()
plt.xlabel('Jahr')
plt.ylabel('Brennstoff')
plt.savefig('brennstoffpreise.png')
# plt.show()        
# pprint(data)            
