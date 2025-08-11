userDigit = int(input("Enter Your Number: "))

if userDigit > 1 and all(userDigit % i != 0 for i in range(2, userDigit)):
    print(userDigit, "is a Prime Number")
else:
    print(userDigit, "is not prime")