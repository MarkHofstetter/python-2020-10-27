j = 0
while j < 10:
    j += 2
    print(j)
else:
    print("else")


# repeat until loop    
while True:
    j -= 1
    print(j)
    if j <= 0:
        break

for i in range(-20,20,5):    
    if i == 0:
        continue
    print(i, end = ' * ')
else:
    print("i ende ", i)        
