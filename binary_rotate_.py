def binary (arr , num) :
    for _ in range (num) :
        last = arr[-1]  

        for j in range (len(arr)-1 , 0 , -1):
            arr[j] = arr[j-1] 

        arr[0] =last 

    return arr 

arr = [1,2,3,4,5,6] 
num = 3                   # num = kitne time rotate krna h 

print(binary(arr , num ))



# kisi specific value ko rorate krke aage le jana 

# def rotate (arr ):

#     inde = arr.index(4) 
#     val = arr[inde] 

#     for i in range (inde , 0 ,-1):
#         arr [i] = arr[i-1] 

#     arr[0] = val 
#     return arr 

# arr = [ 1,2,3,4,5] 
# print(rotate(arr))     


