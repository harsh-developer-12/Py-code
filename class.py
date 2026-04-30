# def history ():
#     with open ("account.txt" , "r") as f :
#         f.read()

# def clar_history():
#             with open ("account.txt" , "w") as f :
#                 f.write (" clear history \n")

# def save_history(equation , result):
#         with open ("account.txt", "a") as file:
#          file.write (equation + " = " + str(result) + "\n")      

# while True:
#     print("1. Account Transaction")
#     print("2. View History")
#     print("3. Clear History")
#     print("4. Exit")
#     print("5. check balance")
#     choice = input(" choice an option: ")

#     if choice == '1':
#         ammount=int(input(" enter amount"))
#         passw=int(input("enter password"))
#         balance=6000
#         withdra_pass=1234
#         check_balance_password=12345
#         minimum_balance=0
#         if ammount > balance:
#             print("check your balance")
#         elif ammount <= balance :
#             print (" transaction success")

#     elif choice == '2':
#         history()

#     elif choice == '3':
#         clar_history()

#     elif choice == '5':
#         balance = 6000
#         passw=int(input(" enter password"))
#         check_balance_password=12345
#         if passw==check_balance_password:
#             print("your balance is : " , balance-ammount)

#         else:
#             print("wrong password pls enter correct password")    

#     elif choice == '4':
#         break

#     else:
#         print("Invalid choice. Please try again.")





# amount = int(input("Enter amount: "))

# notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

# total_notes = 0
# for note in notes:
#     if amount >= note:
#         count = amount // note
#         amount = amount % note
#         total_notes += count
#         print(note, ":", count , amount)
# print("Total number of notes:", total_notes)



# a = 7654 
# note = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
# for i in note :
#     if a >= i :  
#         count = a // i
#         a = a % i
#         print (i , " :" , count)    



import sys 
from PyQt5.QtWidgets import QApplication , QWidget 
ab = QApplication (sys.argv)
window= QWidget()
window.setWindowTitle(" form validation ")            
window.setGeometry(100,100,350,300)
window.show()
sys.exit(ab.exec_())

a=input("enter num")
for i in range (a):
    print(a-i)