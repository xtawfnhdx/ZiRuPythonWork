# Define a function that computes the BMI index
def bmi(height, weight):
    # 1. Convert the height in feet and inches to metres
    # The parameter height is a list that stores [feet, inches]
    height_m = 0.3048 * (height[0] + height[1]/12)
    
    # 2. Convert the weight in pounds to kg
    weight_kg = 0.453592 * weight
    
    # 3. Compute the BMI index using the formula
    bmi_index = weight_kg / height_m ** 2
    
    # Return the BMI index with a return statement
    return bmi_index


# Define a function that compute the average BMI index given an arbitrary number of BMI indexes as arguments
def average_bmi(*args):
    return sum(args) / len(args)


# Define a function that computes and display the BMI index
def show_bmi(height, weight):
    # Use bmi() to compute and store the BMI index
    bmi_index = bmi(height, weight)
    
    # Display a message
    print(f"The BMI index is {bmi_index}")
