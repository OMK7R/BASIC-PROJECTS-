print("**********CALCULATOR**********")
print("\n")


num1 = int(input("Enter First Number :"))
num2 = int(input("Enter Second Number :"))


print("\n iiEnter 1 for ADDITION \n Enter 2 for SUBTRACTION\n Enter 3 for MULTIPLICATION\n Enter 4 for DIVISION")
print("\n")
Entered_Number=int(input("Choice a Number From 1 to 4 :"))
print("\n")

if Entered_Number == 1 :
    print("The Addition of FIRST and SECOND is :",num1 + num2)
    
elif Entered_Number == 2:
    print("The Subtraction of {num1} and {num2} is :",num1-num2)
    
elif Entered_Number == 3:
    print("The Multiplication of {num1} and {num2} is :",num1*num2)
    
elif Entered_Number == 4:
    print("The Division of {num1} and {num2} is :",num1/um2)
    
else:
    print("This is WRONG format . Please Enter among the above Numbers")
    
    
    
    
    
