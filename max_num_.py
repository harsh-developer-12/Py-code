def max(arr) :
    value = arr[0] 
    for i in arr :
        if i > value :
            value =i 
    return value     

arr = [1,3,7,9,4,5] 
print(max(arr))


