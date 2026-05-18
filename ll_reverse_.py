class node :
    def __init__(self , data ):
        self.data = data 
        self.next = None 

def create () :
    f = node (10) 
    s = node (20) 
    th = node (30) 
    ft = node (40) 

    f.next = s 
    s.next = th 
    th.next = ft 

    return f 

def rev (head):
    prev = None 
    curr = head 

    while curr : 

       next = curr.next 
       curr.next = prev 

       prev = curr 
       curr = next 
    return prev  

def trav(param) :  
    temp = param 
    while temp :
        print(temp.data , end="-->")
        temp = temp.next 
    print("null")

var = create () 
second = rev(var) 
trav(second) 


  