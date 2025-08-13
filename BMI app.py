#Declaring function and variables
def bmi_calculator():
    userName = input("Enter Your Name: ")
    print(f"{userName} You're Welcome to the BMI Calculator App")
    weight = float(input("Enter your weight in Kilograms(Kg): "))
    height = float(input("Enter your height in meters(m): "))

    #BMI formula
    bmi = weight / (height**2)
    print(f"Your BMI is {bmi:.2f}")

    #Determining BMI cartegory
    if bmi < 18.5:
        print(f"{userName}, You're Underweight")
    elif 18.5 <= bmi < 24.9:
        print(f"{userName}, You're Normal")
    elif 25 <= bmi < 29.9:
        print(f"{userName}, You're Overweight")
    else:
        print(f"{userName}, you're obese!")
bmi_calculator()