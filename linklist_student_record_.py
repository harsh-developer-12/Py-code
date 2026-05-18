class record :
    def __init__(self , name , roll , mark ):
        self.name = name 
        self.roll = roll 
        self.mark = mark 
        self.next = None 

Name1 = record("Rani" , 7 , 87) 
Name2 = record ("annu" , 3 , 79)
Name3 = record("radha" , 4 , 82)

Name1.next = Name2 
Name2.next = Name3 

head = Name1 

while head :
    print(head.name , end= "-->")
    print(head.roll) 
    print(head.mark)
    head = head.next 
