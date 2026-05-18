def linear(arr , target): 
    count = 0 
    for i in range (len(arr)):
        if arr[i] == target : 

            count += 1

    return count


arr = [10,30,20 ,22 , 50 , 40 , 30 , 40 ,30] 

print(linear(arr , 30)) 
   