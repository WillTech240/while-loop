def bmi_calculator():
    userName = input("Enter Your Name: ")
    print(f"{userName}, welcome to the BMI Calculator App!")

    # Get user inputs
    weight = float(input("Enter your weight in Kilograms (Kg): "))
    height = float(input("Enter your height in meters (m): "))

    # Calculate BMI
    bmi = weight / (height ** 2)
    print(f"Your BMI is {bmi:.2f} kg/m²")

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"{userName}, you are {category}.")

bmi_calculator()
