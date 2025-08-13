#Variables for the options and user choice
while True:
    print("Choose your option:")
    print("1. Prime Numbers")
    print("2. Even Numbers")
    print("3. Odd Numbers")
    user_choice = input("Enter your choice (1-3): ").strip()

#Prime Numbers
    if user_choice == "1":
        def prime_number():
            start = int(input("Enter your first number "))
            end = int(input("Enter your last number "))
            print(f"Prime numbers between {start} and {end} ")
            for num in range(start, end + 1):
                if num > 1:
                    is_prime = True
                    for i in range(2, int(num **0.5) + 1):
                        if num % i == 0:
                            is_prime = False
                            break
                        if is_prime:
                            print(num)
        prime_number()
#Even Numbers
    elif user_choice == "2":
         def even_numbers():
            start = int(input("Enter your first number: "))
            end = int(input("Enter your last number"))
            print(f"Even numbers between {start} and {end} ")
            for num in range(start, end +1):
                if num %2 == 0:
                    print(num)
         even_numbers()    

#odd numbers
    elif user_choice == "3":
        def odd_number():
            start = int(input("Enter your first number: "))
            end = int(input("Enter your last number: "))
            print(f"Odd numbers between {start} and {end} ")
            for num in range(start, end +1):
                if num %2 != 0:
                    print(num)
        odd_number()

    else:
        # Ask if user wants to continue
        try_again = input("\n Do you want to calculate again? (yes/no): ").strip().lower()
        if try_again != "yes":
            print("Goodbye!")
            break
        
        

    

  

    
    








