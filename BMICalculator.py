print("Welcome to BMI Calculator. Please enter your Height and Weight and see what is your health condition!!!!")
def height_converter(feet,inch):
    meter=round((0.3048*feet)+(0.0254)*inch,2)
    return meter
height_feet=int(input("Enter your feet: "))
height_inch=int(input("Enter your inch: "))
weight=float(input("Enter your weight: "))
height=height_converter(height_feet,height_inch)
bmi_value=round((weight/height**2),2)
if bmi_value>=18 and bmi_value<=24.9:
    print(f'Your BMI value is {bmi_value} and you have Healthy Weight!!')
elif bmi_value>=25 and bmi_value<=29.9:
    print(f'Your BMI value is {bmi_value} and you are Overweight!!')
elif bmi_value>=30 and bmi_value<=34.9:
    print(f'Your BMI value is {bmi_value} and you have Class 1 obesity!!')
elif bmi_value>=35 and bmi_value<=40:
    print(f'Your BMI value is {bmi_value} and you have Class 2 obesity!!')
elif bmi_value>40:
    print(f'Your BMI value is {bmi_value} and you have Class 3 obesity (severe obesity)!!')
else:
    print(f'Your BMI value is {bmi_value} and you are underweight!!')
