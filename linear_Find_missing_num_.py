def miss_num (arr):
    for i in range(1 , len(arr)+1):
        if i not in arr :
            return i 
        
arr = [1,3,4,5] 

print(miss_num(arr))
  

