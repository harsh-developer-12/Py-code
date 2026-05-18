def linear(arr , target):
    for i in range (len(arr)):
        if arr[i] == target :
            return i 
        
    return -1 


arr = [10,30,20 ,22 , 50 , 40 ] 

print(linear(arr , 30)) 
