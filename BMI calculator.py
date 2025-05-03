def calculate_bmi():
    print("\nBMI Calculator")
    print("--------------")
    
    try:
        weight = float(input("Enter weight in kg: "))
        if weight <= 0:
            print("Weight must be a positive number")
            return
            
        print("",weight)  
        height = float(input("\nEnter height in cm: "))
        if height <= 0:
            print("Height must be a positive number")
            return
            
        print("",height)
        height_in_metres = height / 100
        bmi = round(weight / (height_in_metres ** 2), 2)

        print("\nYour BMI is:", bmi)
        
        if bmi < 16:
            print("Category: Severe thinness")
        elif 16 <= bmi < 17:
            print("Category: Moderate thinness")
        elif 17 <= bmi < 18.5:
            print("Category: Mild thinness")
        elif 18.5 <= bmi < 25:
            print("Category: Normal range")
        elif 25 <= bmi < 30:
            print("Category: Overweight (pre-obese)")
        elif 30 <= bmi < 35:
            print("Category: Obese class I")
        elif 35 <= bmi < 40:
            print("Category: Obese class II")
        else:
            print("Category: Obese class III")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

calculate_bmi()