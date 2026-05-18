class student :
    def __init__(x , name , roll , mark ):   # x.name = xke andr sb cheezw h kyu functoin call krne pr use first parameter ko hi accesses  krte first me kitni bhi elements ho wo unhe sb ko accese kr lega 
        x.name = name 
        x.roll = roll 
        x.mark = mark
    def show(x) :
        print("name = " , x.name )         
        print("roll no = " , x.roll )   
        print(" mark = " , x.mark )

class_obj = student("ravi" , 21 , 78) 
class_obj.show()    

