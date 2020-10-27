user_input = input("Gib mir eine Zahl: ")

try:
    user_input = int(user_input)   
except ValueError:
    print("keine Zahl")
    exit()
    
print("Ergebnis: ", user_input * 5)