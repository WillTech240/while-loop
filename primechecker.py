firstNumber = int(input("Enter Your first number: "))
LastNumber= int(input("Enter Your Last number: "))

for num in range(firstNumber, LastNumber + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
