#Variables for the options and user choice
while True:
    print("Choose your option:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    user_choice = input("Enter your choice (1-4): ").strip()

#Addition
    if user_choice == "1":
        def add():
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(num1 + num2)
        add()
        
        
#Subtraction
    elif user_choice == "2":
        def subtract():
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(num1 - num2)
        subtract()

#Multiplication
    elif user_choice == "3":
        def multiply():
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(num1 * num2)
        multiply()

#Division
    elif user_choice == "4":
        def Divide():
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print("Result:", num1 / num2)
        Divide()
        
    else:
        print("Invalid option, Please try again")
    # Ask if user wants to continue
    try_again = input("\n Do you want to calculate again? (yes/no): ").strip().lower()
    if try_again != "yes":
        print("Goodbye!")
        break
        

    

  

    
    








