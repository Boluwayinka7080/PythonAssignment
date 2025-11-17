weight = float(input("What is your weight in kg: "))
height = float(input("What is your height in kg: "))
bmi = weight / (height * height)
if(bmi < 18.5):
    print("You are underweight")
if(bmi >= 18.5 and bmi <= 24.9):
    print("Your bmi is normal")
if(bmi >= 25 and bmi <= 29.9):
    print("You are overweight")
if(bmi >= 30):
    print("You are obese")
