def write() :
    with open ("doc.txt" , "w") as file :
        user = str(input("enter your content"))
        file.write (user)
def show() :
    with open ("doc.txt" , "r") as file :
        content = file.read()
        print(content)

def add_new() :
    with open ("doc.txt" , "a") as file :
      file.write (" \n")
      user2 = str(input("enter your content to add"))
      file.write (user2)

while True :
    print ("1. view doc")
    print ("2. write doc")
    print ("3. add new content to doc")
    print ("4. exit")
    choice = int(input("enter your choice"))
    if choice == 1  : 
      show()
    elif choice == 2 :
        write()
    elif choice == 3 : 
     add_new()
    elif choice == exit :
       break
    else :
        print ("invalid choice")
        
