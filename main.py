height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(height / weight ** 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are under weight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese")
else: 
    print(f"Your bmi is {bmi}, you are clinically obese.")