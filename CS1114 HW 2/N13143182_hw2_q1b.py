weight_pound = float(input("Please enter weight in pounds: "))

height_inch = float(input("Please enter height in inches: "))

weight_kilogram = weight_pound*0.453592
height_meter = height_inch*0.0254

bmi = weight_kilogram/(height_meter**2)

print("BMI is: ", bmi)
