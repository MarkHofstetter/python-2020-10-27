import re
from pprint import pprint

test_plz = 'A-1324'
# A - - 1234

matches = re.search(r'^A[ -]{0,1}(\d{4})$', test_plz)
pprint(matches)
print(test_plz)
if matches:
    print("ist PLZ", matches[0], matches[1])
else:
    print("ist keine PLZ")
    
    
test_plz = 'Mein Strasse 18, A-1324 Bladorf'
# A - - 1234

matches = re.search(r'A[ -]{0,1}(\d{4})', test_plz)
pprint(matches)
print(test_plz)
if matches:
    print("ist PLZ", matches[0], matches[1])
else:
    print("ist keine PLZ")    
    
    
print("Normalisieren")
test_plz = '  Mein Str.    18 ,      A-1324   Bladorf, Blistr. 34 '
test_plz = test_plz.strip()
test_plz = re.sub(r'\s+', ' ', test_plz)
test_plz = re.sub(r'\s+,', ',', test_plz)
test_plz = re.sub(r'(str)\.', r'\1asse', test_plz, flags=re.IGNORECASE)
print(test_plz)

    