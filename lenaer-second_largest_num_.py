# def second_largest(arr):
#     first = max(arr)

#     second = float('-inf')
#     for num in arr:
#         if num != first and num > second:
#             second = num

#     return second 


# arr = [2 , 6 , 7 , 8 , 9]
# print(second_largest(arr)) 


#  one more method  

def large(arr) :
     largest = max(arr) 
     smallest= min(arr) 

     for i in arr : 
         if smallest < i < largest :
             smallest = i 

     return smallest 


arr = [5 , 8 , 180 , 2 ] 

print(large(arr))  