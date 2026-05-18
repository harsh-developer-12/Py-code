def binary (arr , target):
    low = 0 
    high = len(arr) -1  

    while low < high :

       mid  = (low+high) // 2 

       if arr[mid] == target :
        return mid 
    
       elif arr [mid] < target :
         return mid +1 
    
       else :
           high = mid-1 

    return -1 

arr = [1,2,3,4,5] 
print(binary(arr , 3))            