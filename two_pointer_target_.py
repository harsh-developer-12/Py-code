array = [ 2 , 5 , 4 , 9]
target = 9 
for i in range(len(array)) :
    for j in range (i+1 , len(array)):
        if array[i]+array[j] == target :
         print("target : " , array[i] ,"+" , array [j] , "=" ,  target )
