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

    
# ## weight converter 

# weight = float(input("how much do u weight ?"))
# unit = input("is it in kilogram (K) or pounds (L)").lower()

# if unit == "k" :
#     unit = "Lb"
#     print(f"{round(weight * 2,20462)} {unit}")
# elif unit == "l" :
#     unit = "KG"
#     print(f"{round(weight / 2,20462)} {unit}")
# else :
#     print(f"the unit {unit} is not correct")
    
# ## temp converter 

# temp = float(input("what is the temperture ?"))
# unit = input("is it in celsius (C) or fahrenheit (F)").lower()

# if unit == "c" :
#     unit = "F"
#     print(f"{round((temp * 9) /5 + 32 ,1)} {unit}")
# elif unit == "f" :
#     unit = "C"
#     print(f"{round((temp - 32) * 5 /9 , 1)} {unit}")
# else :
#     print(f"the unit {unit} is not correct")

### validate user input 

# username = input("please enter ur username :\n")
# print(bool(username.find(" ")))

# if len(username) <= 12 and  username.find(" ") == -1 and username.isalpha() :
#     print("the username is Valid")
# else :
#     print("please enter a user name that :\n 'under 12 characters' \n 'no spaces' \n 'contain no digits'")

### intrest rate calculator

principle = 0
rate = 0
time = 0

while principle <= 0 and rate <= 0 and time <= 0 :
    principle = float(input("Enter the principle amount :"))
    if principle < 0 :
        print("principle can't be under 0")
    rate = float(input("Enter the rate :"))
    if rate < 0 :
        print("rate can't be under 0")
    time = int(input("Enter the time in years :"))
    if time < 0 :
        print("time can't be under 0")

result = principle* pow(1+(rate/100),time)

print(f"with principle of {principle:,.2f} and {rate:.2f} rate in {time} years, u will have {result:,.001f}$")