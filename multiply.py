def multiply():
    result = 1
    while True:
        num = input("Enter a number or type 'done' to finish: ")
        if num.lower() == "done":
            break
        result *= int(num)
    print("The product is:", result)

multiply()
