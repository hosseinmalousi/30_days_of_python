# #python calc

# operation = input("which operation u wanna use /,*,-,+ :")
# num1 = float(input("add the first number : "))
# num2 = float(input("add the second number : "))
# result = 0
# if operation == "+" :
#     result = num1 + num2 
#     print(round(result,3))
# elif operation == "-":
#     result = num1 - num2
#     print(round(result,3))
# elif operation == "*" :
#     result = num1*num2
#     print(round(result,3))
# elif operation == "/":
#     result = num1 + num2
#     print(round(result,3))
# else :
#     print("please insert the right operation")

    
## weight converter 

weight = float(input("how much do u weight ?"))
unit = input("is it in kilogram (K) or pounds (L)").lower()

if unit == "k" :
    unit = "Lb"
    print(f"{round(weight * 2,20462)} {unit}")
elif unit == "l" :
    unit = "KG"
    print(f"{round(weight / 2,20462)} {unit}")
else :
    print(f"the unit {unit} is not correct")
    
## temp converter 

temp = float(input("what is the temperture ?"))
unit = input("is it in celsius (C) or fahrenheit (F)").lower()

if unit == "c" :
    unit = "F"
    print(f"{round((temp * 9) /5 + 32 ,1)} {unit}")
elif unit == "f" :
    unit = "C"
    print(f"{round((temp - 32) * 5 /9 , 1)} {unit}")
else :
    print(f"the unit {unit} is not correct")