def prime_between():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    for i in range(num1, num2 + 1):
        if i > 1:
            for i in range(2, int(i ** 0.5) + 1):
                if i % i == 0:
                    break
            else:
                print(i, end=" ")
prime_between()
