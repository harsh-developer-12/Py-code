def binary (arr) : 
    low = 0 
    high = len(arr) -1 

    while low < high : 

        mid = (low + high) // 2 
        if arr [ mid ] < arr [mid+1] :
           low = mid +1 

        else : 
           high = mid 

    return arr[low] 

arr = [10,32,38, 4 , 83 ] 
print(binary(arr)) 


