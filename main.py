height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = float(height) / int(weight) ** 2
end_result = int(bmi)

if end_result < 18.5:
    print("You are underweight.")
elif end_result < 25:
    print("You are normal weight.")
elif end_result < 30:
    print("You are overweight.")
elif end_result <= 35:
    print("You are obese")
else: 
    print("You are clinically obese.")