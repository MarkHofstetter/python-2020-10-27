print("Hallo Welt")

a = 2
b = 3

print(a + b)

'''
a = input("Zahl 1: ")
b = input("Zahl 2: ")

print(int(a) + int(b))
'''

y = 2
z = "2"

print(y, z)

# print(y + z) # funktioniert nicht, da verschiedene Typen

print(type(y), type(z))

print(hex(id(a)), hex(id(y)))

y += 1
print(hex(id(a)), hex(id(y)))