def add(a, b):
    sum = a + b    
    return sum
    
def add_list(l: list) -> int:
    sum = 0    
    for i in l:
        sum += i
    l.append('a')
    return sum

fib = [
        1,
        1,
        2,
        3,
        5,
        8,
        13,
       ]
    
sum = add_list(fib)
print(sum)    
print(fib)    
    


