class node :
     def __init__(self , data):
          self.data = data 
          self.next = None 

def create () :
     f = node(10) 
     s = node (20) 
     th = node(30) 
     fi = node(40)

     f.next = s 
     s.next = th 
     th.next = fi 

     return f 


def travers(param) :
     head  = param
     while head :
          print(head.data , end="-->")
          head = head.next 

     print("null") 

def second_last (parem) :
     prev = None 
     temp = parem

     while temp.next :
          prev = temp 
          temp = temp.next 

     print(prev.data)      

var= create ()  
travers(var)
second_last(var)

  