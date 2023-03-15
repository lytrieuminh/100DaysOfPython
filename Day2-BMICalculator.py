# Day 2: BMI Calculator

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = float(weight) / float(height) ** 2
result_bmi = int(bmi)
print(f"Your Body Mazz Index result: ", result_bmi)
