# facturial of a num

# a=int(input("entr a num"))
# fact = 1
# for i in range (1, a+1):
#      fact*=i
# print(  " facturial of num" , fact) 



# reverse num

# a =int(input("enter num"))
# for i in range (a):
#     print(a-i)


# prime num

# num=int(input("entr num"))
# if num>1:
#  for b in range (2,num):    
#      if (num%b)==0:
#           print(num,"not prime")
#           break
#      else: 
#           print( num ,"prime")




# name = "John"
# age = 30
# print (f" my name is {name} and i am {age} years old")     # f string ka kaam h ki hum variable ko string me asani  se use kar skte h 



# user=int(input(" enter amount"))
# user2=int(input("enter password"))
# balance=6000
# withdra_pass=1234
# check_balance_password=12345
# user3 =0
# if user > balance:
#     print("pese nhi h mc aokat me raho  \n pls check balance")
#     user3=int(input(" enter password"))
#     print(balance)

# elif  user<=balance and user2==withdra_pass:
#     print(" transaction succsee \n if u check your balance than enter password ")
#     user3=int(input(" enter password"))

#     if user3==check_balance_password:
#         print("your balance is : " , balance-user)
#     else:
#         print("wrong password")

# elif user2!=withdra_pass:
#     print(" wrong password pls check password and try again ")

# else :
#     print (" account not availeble ")



# randam password generator

# import string,random
# user= string.ascii_letters + string.digits + string.punctuation
# password= ''.join(random.choice(user) for i in range (8))
# print(" your randam password is : " ,password)

# string.ascii_letters = a to z A to Z auto print krta h 
# string.digits  =  0 - 9 print 
# string.punctuation =  !@#$%^&*  ye sb print krta  h 
# '' .join = character ko jod ke print krta h ....




# list=["get up morning 6 : 00 am" , "one hour study" , "go to school" , "in aftnoon mast aram se sone ka" , "fir uthne ka or ghumne ka" ,]
# print(list)
# list.append(input("add item in list"))
# print (list)
# list.pop(input(""))
# print(list)


# import math
# num=int(input("entr num"))
# square = math.log(num)
# print(" your square :",square)


# user=int(input("entr num"))
# print(1+(user-1)%9)
 

# how many chocolate u buy a fix amount of money 

# price=[9,8,7,5,4,5,4,1,2,1]
# money=3
# num=sorted(price)   
# print(num)                     
# if num[0]+num[1]<=money:
#     print(money-(num[0]+num[1]))
#     print(money)
# else:
#     print("money not enough")  



# n = 5
# for i in range(1, n+1):
#     print(" "*(n-i) + "*"*(2*i-1))               
# for i in range(n-1, 0, -1):                 
#     print(" "*(n-i) + "*"*(2*i-1))
 




# import numpy as harsh 
# pandey= harsh.eye(4, k=1)   #  k = left side marge krne ke liye h 
# print(pandey)



# import getpass
# password = getpass.getpass("Enter password: ")
# print(password)





# import pandas as pd
# data = {
#     "name" : ["harsh" , "loki" , "shailu"],
#     "age" : ['20', '23','24']
#     }
# df=pd.DataFrame(data)  # ye data ko ak table ke form me display krata h 
# print(df)


# import numpy as np

# a=np.random.rand(1, 10, (3, 3))
# print(a)




# from kivy.app import App
# from kivy.uix.label import Label

# class MyApp(App):
#     def build(self):            # ye function h jo app ko build krta h
#         return Label(text="Hello Kivy")

# MyApp().run()




                  #  some important code  # 

# from py_compile import main


# def show_history():
#     file  = open("history.txt", "r")
#     line = file.readlines()
#     if len (line) == 0:
#         print("No history found.")
#     else:
#         for line in reversed(line):
#             print(line.strip())
#     file.close()

#     def clear_history():
#         open("history.txt", "w").close()
#         print("History cleared.") 

#         def save_history(equation , result):
#             file = open ("history.txt", "a")
#             file.write (equation + " = " + str(result) + "\n")
#             file.close()

#             def calculator(user_input):
#                 try:
#                     result = eval(user_input)
#                     print("Result:", result)
#                     save_history(user_input, result)
#                 except Exception as e:
#                     print("Error:", e)


#             while True:
#                 user_input = input("Enter equation (or 'history', 'clear', 'exit'): ")
#                 if user_input.lower() == "history":
#                     show_history()
#                 elif user_input.lower() == "clear":
#                     clear_history()
#                 elif user_input.lower() == "exit":
#                     print("Exiting calculator.")
                    
#                     break
#                 else:
#                     calculator(user_input)
    
# main()


  


# # a= [3]
# # b= a
# # b.append(4)
# # print(a)

# # a = 3
# # b= a
# # c= 5
# # print (a is b )
# # print ( a is c )




# def ab():
#     with open ("hist" , "w") as f:      # file create and data store 
#         f.write ("hello world \n")      
#     with open ("hist" , "r") as f:       # file read mode 
#         print(f.read())
#     with open ("hist" , "a") as f:           # content add 
#         f.write ("pande ji \n")
#         with open ("hist" , "r") as f:
#                 print (f.read())

# ab()


      # <- classes and objects ->

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student("Ram", 16)
# s2 = Student("Amit", 17)

# print(s1.name, s1.age)
# print(s2.name, s2.age)


#       <- inheritance  ->
# class a :
#     def display(self):
#         print ("hello")
        
# class b(a):
#     def show(self):
#         print ("world")

# obj = b()
# obj.display()
# obj.show()



# class a:                                     # multilevel inheritance
#     def A (self):          
#         print("hello")
# class b(a):
#     def B(self):
#         print("world")
# class c(b):
#     def C(self):
#         print("htyu")
# obj = c()                   # class c ka object bna h
# obj.A()
# obj.B()                         # ye def function call kr rha h
# obj.C()




# class A:
#     def __init__(self):
#         print("Class A constructor")            # super ka use krke parent class ka constructor call kr skte h

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("Class B constructor")

# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("Class C constructor")

# obj = C()



# class student :
#     def __init__(self , name , age ):
#         self.name = name 
#         self.age = age 

# a = student (input("enter name: ") , int (input ("enter age: ")))
# print (a.name , a.age)





# import sys
# from PyQt5.QtWidgets import QApplication , QWidget 
# ab = QApplication (sys.argv)
# window= QWidget()
# window.setWindowTitle(" tittle of window ")

# a = 




