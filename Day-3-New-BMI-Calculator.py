# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_height = float(height) ** 2
new_weight = float(weight)
total = round(new_weight / new_height ,2)
# when submitting this it wanted a round but not the decimals

if total <= 18.4:
    print(f"Your BMI is {total}, you are underweight.")
elif total < 25:
    print(f"Your BMI is {total}, you have a normal weight.")
elif total < 30:
    print(f"Your BMI is {total}, you are slightly overweight.")
elif total < 35:
    print(f"Your BMI is {total}, you are obese.")
else:
    print(f"Your BMI is {total}, you are clinically obese.")


 # Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# height = 1.75
# weight = 85