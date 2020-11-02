'''

der user gibt zahlen ein zb 2,3,4,2,3,3,2,4,3

bei eingabe von 'q' soll das Programm beendet
und es soll die Häufigkeit der Zahlen ausgegeben werden

2: 3
3: 4
4: 2

die Ermittlung/Berechnung der Statistik soll in einer separaten
Funktion und somit testbar sein 

[2,3,4,2,3,3,2,4,3] => {2: 3, 3: 4, 4: 2} 

'''

from pprint import pprint
from pathlib import Path
# here we add the parent dir (..) to the import 
# search path
import sys
sys.path.append(str(Path('.').absolute().parent))
from wifi_util import get_user_input_int

def count_occurences(data_list):
    statistic = {}
    for v in data_list:
        try:
            statistic[v] += 1
        except KeyError:
            statistic[v] = 1
    return statistic
        
if __name__ == '__main__':
    
    input_list = []
    while True:
        try:
            user_input = get_user_input_int('Bitte Wert eingeben ')
        execept AttributeError:
            break
        input_list.append(user_input)

    statistic = count_occurences(input_list)            
    pprint(statistic)