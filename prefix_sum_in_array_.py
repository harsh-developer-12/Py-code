def prefix_sum(number) : 
    prefix = []
    total = 0 
    for i in number :
        total= total +i 
        prefix.append(total)
    return prefix
number =[ 1, 2 , 4 , 5 ,4] 
result = prefix_sum(number) 
print(result )


