# def lenear (arr , target) :
#     last = -1 

#     for i in range (len(arr)): 
#         if arr [i] == target :
#             last = i 

#     return last         

# arr = [10 , 30 , 22 , 33 , 30 , 56 , 39]            
# print(lenear(arr , 30)) 


#  one more 


def lenear (arr , target):
    for i in range (len(arr)-1,-1,-1) :
        if arr[i] == target :
            return i 
    
arr = [10 , 20 , 30 , 20 , 20 ,30 ,44]  

print(lenear(arr , 20))  