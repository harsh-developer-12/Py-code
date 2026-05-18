def insert (arr , value) :
     low = 0 
     high = len(arr) -1 

     while low < high :
         mid = (low +high) //2 

         if arr[mid] < value:
              low = mid +1 
         else :
              high = mid 

     arr.insert(low , value)
     return arr
 
arr = [ 1,3,4,5,8,9] 
print(insert(arr , 2))
