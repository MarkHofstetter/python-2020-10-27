fib = [
        1,
        1,
        2,
        3,
        5,
        8,
        13,
       ]

# print(fib)       
'''
for no, v in enumerate(fib):
    print(no, v)
'''

print(fib[2:4])
print(fib[2:])
print(fib[-2])

fib.append(fib[-2] + fib[-1])

print(fib)

fib_copy = fib # kopiert nur die referenz!!
# fib_copy = list(fib)
fib_copy = fib.copy()
print(fib.reverse())

print(fib)
print(fib_copy)
