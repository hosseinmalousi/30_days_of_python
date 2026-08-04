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

# principle = 0
# rate = 0
# time = 0

# while principle <= 0 and rate <= 0 and time <= 0 :
#     principle = float(input("Enter the principle amount :"))
#     if principle < 0 :
#         print("principle can't be under 0")
#     rate = float(input("Enter the rate :"))
#     if rate < 0 :
#         print("rate can't be under 0")
#     time = int(input("Enter the time in years :"))
#     if time < 0 :
#         print("time can't be under 0")

# result = principle* pow(1+(rate/100),time)

# print(f"with principle of {principle:,.2f} and {rate:.2f} rate in {time} years, u will have {result:,.001f}$")

### countdown timer 

# import time

# seconds = int(input("Enter time in seconds :"))

# for x in range(seconds,0,-1) :
#     sec = x % 60
#     mins = (x // 60) % 60
#     hours = x // 3600
#     print(f"{hours:02}:{mins:02}:{sec:02}")
#     time.sleep(1)

    

# print("times up")

### Shopping cart program 

# foods=[]
# prices=[]
# total = 0

# while True:
#     order = input("Enter the food u order: (q for exit) \n")
#     if order.lower() == "q" :
#         break
#     else :
#         price = int(input(f"Enter the price for {order.capitalize()}: $"))
#         foods.append(order)
#         prices.append(price)

# for food in foods :
#     print(food, end=" ")

# for price in prices :
#     total += price

# print(f"your total is {total}$")
        
### phone tastatur 

# keyboards = [(7,8,9),(4,5,6),(1,2,3),("*",0,"#")]

# for key in keyboards:
#     for row in key:
#         print(row,end=" ")
#     print()


### quizz 

# questions = (
#     "What gas do humans need to breathe to survive?",
#     "What is the closest planet to the Sun?",
#     "What force pulls objects toward the Earth?",
#     "What organ pumps blood through the human body?"
# )

# answers = (
#     ("A) Nitrogen", "B) Oxygen", "C) Helium", "D) Carbon"),
#     ("A) Venus", "B) Mars", "C) Mercury", "D) Earth"),
#     ("A) Friction", "B) Inertia", "C) Magnetism", "D) Gravity"),
#     ("A) Liver", "B) Heart", "C) Kidney", "D) Lung")
# )

# correct_answers = ("B", "C", "D", "B")
# guesses =[]
# score = 0
# row =0

# for qeustion in questions:
#     print("+++++++++++++++++++++++++++++++++++")
#     print(qeustion)
#     for answer in answers[row]:
#         print(answer)    
    
#     guess = input("Please Answer with A,B,C,D: ")
#     guesses.append(guess)
#     if guess.upper() == correct_answers[row]:
#         print("correct answer")
#         score +=1
#     else :
#         print(f"the correct answer is {correct_answers[row]}")
        
#     row += 1
 
# print("/////// SCORES \\\\\\\\\\")

# print(f"YOU'VE SCORED {score / len(questions) *100} ")

### late night Shop

# menu = {"pizza":3,"bretzel" :1.5,"curry wurst":3,"burger":3,"soda":1,"ayran":1}

# cart=[]
# total=0

# for key ,value in menu.items():
#     print(f"{key.capitalize()} : {value} euro")

# print("-----------------------------")

# while True:
#     order = input("What do you order ? (q for exit)\n").lower()
    
#     if order == "q":
#         break
#     elif menu.get(order) :
#         cart.append(order)
#     else :
#         print(f"order {order} not available")
    
# for key ,value in menu.items():
#     if key in cart :
#         total += value

# print(f"your total is {total}")
        
        
### Python number guessing 

# import random 

# highest_num = 100
# lowest_num = 0 

# answer = random.randint(lowest_num,highest_num)

# difficulty = {"easy":7,"medium":4,"hard":3}
# chances = 0
# score = 0

# for key ,value in difficulty.items():
#     print(f"{key} : {value} chances")
# user_diff = input(f"please pick a difficulty level from above :").lower()

# if difficulty.get(user_diff) :
#     chances = difficulty.get(user_diff)

# while difficulty.get(user_diff) >= 1 :
#     guess = input(f"please guess the number between {lowest_num} and {highest_num} :")
    
#     if guess.isdigit() :
#         guess = int(guess)
#         if guess > highest_num or guess < lowest_num :
#             print("your guess is out of range")
#         elif guess > answer :
#             print("try lower ;)")
#             chances -= 1
#         elif guess < answer :
#             print("try higher ;) ")
#             chances -= 1
#         elif guess == answer :
#             print(f"your guess {guess} is right ")
#             print(f"your score is {chances}")
#             break
#         else :
#             print("invalid input")
#     else :
#         print("please enter a number")
        
### Rock , Paper , Scissors
# import random

# options = ("rock" , "paper", "scissors")



# playing = True

# while playing :
#     Player = None
#     computer = random.choice(options)
#     while Player not in options :
#         Player = input("Rock , Paper ,Scissors : ").lower()
    
#     print(f"your choice {Player}")
#     print(f"computer choice {computer}")
    
#     if Player == "paper" and computer == "rock" :
#         print("you win :)")
#     elif Player == "rock" and computer == "scissors":
#         print("you win :)")
#     elif Player == "scissors" and computer == "paper":
#         print("you win :)")
#     elif Player == computer:
#         print("it's a tie")
#     else :
#         print("you lose :( )")
    
#     if input("wanna play again ? (yes/no) ") != "yes" :
#         playing = False 