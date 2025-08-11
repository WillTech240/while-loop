#Variables for the options and user choice
option1 = "addition"
option2 = "subtraction"
option3 = "multiplication"
option4 = "Division"
user_choice = input(f"Choose your option, {option1} or {option2} or {option3} or {option4}: ").strip()

#Addition
if user_choice == option1:
    def add():
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        print(num1 + num2)
    add()
        
        
#Subtraction
elif user_choice == option2:
    def subtract():
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        print(num1 - num2)
    subtract()

#Multiplication
elif user_choice == option3:
      def multiply():
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        print(num1 * num2)
      multiply()

#Division
elif user_choice == option4:
      def Divide():
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        print(num1 / num2)
      Divide()
        
else:
    print("Invalid option")
        

  

    
    








