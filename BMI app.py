def bmi_calculator():
    while True:
        userName = input("Enter Your Name: ")
        
        print(f"Hello {userName}, Welcome to the BMI Calculator App!")
        print("This app calculates your Body Mass Index (BMI)\n"
          "and tells you your weight category.\n")

    # Get user inputs
        weight = float(input("Enter your weight in Kilograms (Kg): "))
        height = float(input("Enter your height in meters (m): "))

    # Calculate BMI
        bmi = weight / (height ** 2)
        print(f"Your BMI is {bmi:.2f} kg/m²")

    # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
            tips = "You may need to eat more nutritious foods and consult a doctor."
        elif 18.5 <= bmi <= 24.9:
            category = "Normal"
            tips = "Great job! Maintain your healthy habits."
        elif 25 <= bmi <= 29.9:
            category = "Overweight"
            tips = "Consider regular exercise and a balanced diet."
        else:
            category = "Obese"
            tips = "Seek medical advice and adopt a healthier lifestyle."

        print(f"{userName}, you are {category}.")
        print(f" Health Tip: {tips}\n")
    # Ask if user wants to calculate again
        again = input("Do you want to check again? (yes/no): ").strip().lower()
        if again != "yes":
            print("\n Thank you for using the BMI Calculator App. Stay healthy! ")
        break
            
bmi_calculator()


