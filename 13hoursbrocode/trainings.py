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

### Dice roller program

# import random

# dies= []
# dices = {1: (" _______ ",
#              "|       |",
#              "|   *   |",
#              "|       |",
#              "|_______|"),
#          2: (" _______ ",
#              "| *     |",
#              "|       |",
#              "|     * |",
#              "|_______|"),
#          3: (" _______ ",
#              "| *     |",
#              "|   *   |",
#              "|     * |",
#              "|_______|"),
#          4: (" _______ ",
#              "| *   * |",
#              "|       |",
#              "| *   * |",
#              "|_______|"),
#          5: (" _______ ",
#              "| *   * |",
#              "|   *   |",
#              "| *   * |",
#              "|_______|"),
#          6: (" _______ ",
#              "| *   * |",
#              "| *   * |",
#              "| *   * |",
#              "|_______|")}

# num_dice = int(input("how many dices do u want ?"))

# for x in range(num_dice):
#     dies.append(random.randint(1,6))

# print(dies)
# # for item in dies :
# #     for dice in dices.get(item):
# #         print(dice)

# for row in range(5):
#     for dice in dies :
#         print(dices.get(dice)[row],end=" ")
#     print()
        
# grades = {"hoss" : "A" , "mamad" : "b","nima":"C"}

# print(grades.get("hoss"),grades["mamad"])

# def sayhello(name,*args,**kwargs):
#     print(f"hi {name} {args[1]}")
#     if kwargs["girl"] :
#         print(f"bonjur madame {kwargs["girl"]}")
# sayhello("mamad","ali","hossein",girl = "fatemeh")
    
# print(help("copy"))


# def main():
#     print("im main")

# if __name__ == "__main__":
#     main()

### banking program 

# def showBalance(balance):
#     print(f"Your balance is {balance:.02f}$")

# def deposit(balance):
#     amount = float(input("How much do you want to deposit ? "))
    
#     if amount > 0 :
#         return amount
#     else :
#         print("please insert a valid number and graeter than zero")
#         return 0

# def withdraw(balance):
#     amount = float(input("How much do you want to withdraw ? "))
    
#     if amount > 0 and amount < balance :
#         return amount
#     else :
#         print("please insert a valid number and graeter than zero")
#         return 0

# def main():
#     balance = 0
#     is_running = True
    
#     while is_running:
#         print("Welcome to our seld-made Bank")
#         print("1.Show Balance")
#         print("2.Deposit")
#         print("3.Withdraw")
#         print("4.quit")
        
#         option = int(input("please choose from 1-4 :"))
        
#         match option:
#             case 1:
#                 print("*******************")
#                 showBalance(balance)
#                 print("*******************")
#             case 2:
#                 balance += deposit(balance)
#             case 3:
#                 balance -= withdraw(balance)
#             case 4:
#                 is_running = False
        

# if __name__ == "__main__":
#     main()

### Slot Machine Game
# import random
# import time
# def roll():
#     slots = ["💣" , "🔮" , "🛎" , "🍑"]
    
#     return [random.choice(slots) for _ in range(3)]

# def print_row(row):
#     print("is spinning ...")
#     time.sleep(1)
            
#     print("|".join(row))

# def payout(row,bet):
#     if row[0] == row[1] == row[2]:
#         if row[0] == "💣":
#             return bet * 3
#         elif row[0] == "🔮":
#             return bet * 6
#         elif row[0] == "🛎":
#             return bet * 9
#         else :
#             return bet * 5
#     return 0

# def main():
    
#     balance = input("please enter the amount you wnat as the balance : $")
#     if not balance.isdigit():
#         print("please enter a valid number")
        
#     balance = int(balance)
    
#     while balance > 0:
#         print("$$$$$$$$$$$$$$$$$$$$$$$")
#         print("Wellcome to the slot machine game")
#         print("$$$$$$$$$$$$$$$$$$$$$$$\n")
        
        
#         print(f"balance : ${balance}")
        
#         bet = input("how much are u willing to bet: $")
        
#         if not bet.isdigit() :
#             print("enter a valid number")
            
#         bet = int(bet)
        
#         if bet < 0 :
#             print("please set a bet more than zero")
#             continue
#         elif bet > balance :
#             print("insufficent funds ")
#             continue
#         else :
#             balance -= bet    
        
#         row =roll()
#         print_row(row)
        
#         balance += payout(row,bet)
        
#         playAgain = input("do you want to play agian (Y/N) :").lower()
#         if not playAgain == "y" :
#             break
#     print(f"your current balance is ${balance}")
    

# if __name__ == "__main__":
#     main() 

### Eyncrypt and Decrypt program

# import string
# import random

# def encrypt(text,chars,keys):
#     encrypted = ""
#     for char in text:
#         index = chars.index(char)
#         encrypted += keys[index]
#     return encrypted

# def decrypt(text,chars,keys):
#     decrypted = ""
#     for char in text:
#         index = keys.index(char)
#         decrypted += chars[index]
#     return decrypted

# def main():
#     chars = list(" " + string.digits + string.ascii_lowercase+ string.ascii_uppercase + string.punctuation)
#     keys = chars.copy()
#     random.shuffle(keys)
#     while True:
#         print("Wellcome to the cipherus")
#         print("************************")        
#         text = input("please enter the text (q for exit):")
#         if text != "q" : 
#             if input("please insert E for eyncrypt and D for decrypt : ").lower() == "e" :
#                 encrypted = encrypt(text,chars,keys)
#                 print(f"The Encrypted text : {encrypted}")
#             else :
#                 decrypted = decrypt(text,chars,keys)
#                 print(f"The Decrypted text : {decrypted}")
#             print()
#         else :
#             break        

# if __name__ == "__main__":
#     main()

### Hangman game 

# import random
# import words

# hangman_art={0:("  ","  ","  "),
#              1:(" O ","  ","  "),
#              2:(" O "," | ","  "),
#              3:(" O ","/| ","  "),
#              4:(" O ","/|\\","  "),
#              5:(" O ","/|\\","/  "),
#              6:(" O ","/|\\","/ \\")}

# def display_art(counter):
#     for line in hangman_art[counter]:
#         print(line)
#     print("***************")


# def show_answer(answer):
#     print(f"The correct answer is {answer}")

# def fill_placeholder(placeholder):
#     print("***************")
#     print(" ".join(placeholder)+"\n")
#     print("***************")

# def main():
#     print("Wellcome to the hangman game")
    
#     answer = random.choice(words.words)
#     wrong_guesses = 0
#     placeholder = ["_"]* len(answer) 
#     already_guessed = set()
#     is_running = True
    
#     while is_running:
#         fill_placeholder(placeholder)
#         display_art(wrong_guesses)
        
        
#         guess =input("please type down your guess :")
#         if len(guess) != 1 or not guess.isalpha():
#             print("please add a valid input")
#             continue
#         elif guess in already_guessed:
#             print("you've already guessed this letter")
#             continue
        
#         if guess in answer :
#             for i in range(len(answer)):
#                 if answer[i] == guess :
#                     placeholder[i] = guess
#             already_guessed.add(guess)
#         else :
#             wrong_guesses += 1
            
#         if wrong_guesses >= len(hangman_art) - 1:
#             display_art(wrong_guesses)
#             show_answer(answer)
#             print("You've lose")
#             is_running = False
#         elif "_" not in placeholder :
#             display_art(wrong_guesses)
#             show_answer(answer)
#             print("You've won")
#             is_running = False
            
# if __name__ == "__main__":
#     main()

# class Athelte:
    
#     atheltes =[]
    
#     def __init__(self,first_name,last_name,age,club,sport):
#         self._first_name = first_name.capitalize()
#         self._last_name = last_name
#         self.age = age
#         self.club = club
#         self._sport = sport
#         self.atheltes.append((self._first_name,self._last_name))
    
#     @property
#     def first_name(self):
#         return self._first_name
    
#     @first_name.setter
#     def first_name(self,new_first_name):
#         self._first_name = new_first_name

#     @property
#     def sport(self):
#         return self._sport
    
#     @sport.deleter
#     def sport(self):
#         del self._sport
#         print("sport has been deleted")
#     def get_athelte(self):
#         return f"{self.first_name} {self.last_name} is {self.age} years old and is a {self.sport} player"
    
#     def get_player_goals(self):
#         pass
    
#     def Score():
#         pass   
    
#     @classmethod
#     def list_athletes(cls):
#         for athlete in cls.atheltes:
#             print(athlete)
    
#     @staticmethod
#     def is_club_valid(club):
#         clubs = ["Barcelona" , "Athletico madrid" ,"Real madrid" , "Malaga"]
#         return club.capitalize() in clubs
    
    
# class Footballer(Athelte):
#     def __init__(self, first_name, last_name, age, club,position):
#         super().__init__(first_name, last_name, age, club ,sport="football")
#         self.position = position
        



# athelte1 = Athelte("hossein","malousi" , 21,"barcelona","football")
# athelte2 = Athelte("Alex","b",21,"real","basketball")

# footballer1 = Footballer("hossein","malousi",21,"real" ,"winger",)
# footballer1.first_name = "stephan"
# footballer1.position = "midfielder"
# print(footballer1.position)
# del footballer1.sport
# print(footballer1.list_athletes())
# print(Athelte.is_club_valid("barcelona"))
    

# import os
# import json

# family_members = {"parents":("saeed" ,"maryam"),
#                   "childerens":("hossein","rozhan"),
#                   "pets":("steve")}
# file_path= "./text.text"

# with open(file_path,"r") as file:
#     print(file.read())
#     print(f"file {file_path} is created")
    
# with open("./13hoursbrocode/json_test.json","w") as file:
#     json.dump(family_members,file,indent=4)
#     print("json test has been created")


### alarm clock

# import datetime
# import time


# is_running = True
# target_time = input("when do u wanna wake up ?:(HH:MM:SS)\n")


# while is_running: 
#     current_time = datetime.datetime.now().strftime("%H:%M:%S")
#     # target_time = datetime.time(14,11,0)
#     print(current_time)
#     time.sleep(1)
#     if  current_time == target_time:
#         print("wake up sinshine")
#         is_running = False


### api testing 

# import requests

# base_url= "https://pokeapi.co/api/v2/pokemon/"

# def get_the_quote(name):
#     url =f"{base_url}{name}"
    
#     request =requests.get(url)
    
#     if request.status_code == 200 :
#         print("data recieved")
#         req_data = request.json()
#         return req_data
#     else :
#         print("no such name")
#         return 

# name = input("what anime qoute do u want :")

# qoute = get_the_quote(name)

# print(qoute["name"])

### coffee picture fetcher

import requests

def fetch_pic():
    url = "https://coffee.alexflipnote.dev/random"
    
    req = requests.get(url,stream=True)
    
    if req.status_code == 200 :
        with open("./coffee.jpg", "wb") as file:
            for chunk in req.iter_content(chunk_size=8192):
                file.write(chunk)
        return "file has been created"
            
pic = fetch_pic()
print(pic)
