text = "Python ist toll" 

text = ( text + " " ) * 4 
print(text)
print('=' * len(text) )

print( text.upper() )
print( text.lower() )

print( text.count("o") )
print( text.replace("Python", "perl").count("o") )