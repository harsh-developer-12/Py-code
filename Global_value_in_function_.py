x = 10 
def function_name () :
    x = 20 
    print ("local  x = " , x )
function_name()    

print ( "Global x = ",x)


def global_change() :
    global x 
    x = 300 
global_change() 
