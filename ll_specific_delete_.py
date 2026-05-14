class node:
    def __init__(self,data):
        self .data = data 
        self.next = None 
def create () : 
    f = node (10) 
    s = node (20) 
    th = node(30) 

    f.next = s 
    s.next = th  

    return f 


def delete (head , key):
    prev = None 
    temp = head

    while temp :
        if temp.data == key :
            if temp == head :
               return head.next 

            else :
                prev.next = temp.next 

                return head
            
        prev = temp 
        temp = temp.next  

    return head       
 


def traves(param) :
    head = param  
    while head :
        print(head.data , end="-->")
        head = head.next 
    print("null") 

head = create () 
new_head = delete( head , 20)  
traves(new_head)



