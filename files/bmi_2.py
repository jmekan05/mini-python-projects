height = float(input("What is your height in m? "))
weight = float(input("What is weight in kg? "))

bmi = round(weight // height ** 2)

if bmi < 18.5:
    under = f"Your BMI is {bmi}, you are underweight."
    print(under)
elif bmi < 25:
    normal = f"Your BMI is {bmi}, you have a normal weight."
    print(normal)
elif bmi < 30:
    overweight = f"Your BMI is {bmi}, you are overweight."
    print(overweight)
elif bmi < 35:
    obese = f"Your BMI is {bmi}, you are obese."
    print(obese)
else:
    obese_severe = f"Your BMI is {bmi}, you are clinically obese."
    print(obese_severe)