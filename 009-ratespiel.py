'''
Zahlenratespiel

eine Zufallszahl zwischen 1 u X (Usereingabe) wird gezogen

der Spieler darf 5 Mal raten oder "q" eingeben zum Aufhören

nach jeder Raterunde wird dem Spieler die Info gegeben ob er/sie
richtig/zu hoch/niedrig war

Ausgabe wieviele Fehler/nach wievielen Runden das richtige Ergebnis 
geraten wurde

1. Fehler sollen gefangen werden
2. Code duplizierung soll vermieden werden (Funktionen)
'''
import random
import os

DEBUG = os.environ.get('MY_DEBUG')

'''
try:
    user_input = int(user_input)   
except ValueError:
    print("keine Zahl")
    exit()
'''

def get_user_input_int(prompt: str, lower_imit = None, upper_limit = None):    
    while True:
        user_input = input(prompt + "(oder q zum abbrechen)")
        try:
            user_input = int(user_input)            
            break
        except ValueError:        
            if user_input.lower() == 'q':
                user_input = None                
            else:
                print('bitte eine Zahl eingeben')                                  
    return user_input



random_range = get_user_input_int(prompt = "Zahlenbereich: ")

if random_range is None:
    exit()

secret = random.randint(1, random_range)
if DEBUG:
    print('Secret: ', secret)

for i in range(6):    
    guess = get_user_input_int(str(i) + ". Rate: ")
    if guess == secret:        
        print("Richtig")
        break
    elif guess > secret:
        print("Zu hoch")
    else:
        print("Zu niedrig")
else:
    print("Falsch nach", i+1, "Versuchen")
        
