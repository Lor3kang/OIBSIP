def calculate_bmi(weight, height):
    """
    Calculate BMI using weight (in kilograms) and height (in meters).
    Formula: BMI = weight / (height * height)
    """
    bmi = weight / (height ** 2)
    return bmi

def categorize_bmi(bmi):
    """
    Categorize BMI into different health categories.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return

        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are categorized as: {category}")

    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()
