# Thenea_Sun
# Sept. 19th
# assignment_two
# This is my second project, which I created a chat bot with codes, in order to get all the information that is
# required in the rubric

print("Hello! I am the artificial intelligence you are going to talk to in the next five minutes!")

print("My name is San!")

name_of_user = input("What is your name?")

print(name_of_user, "sounds cute! I like this name!")

location_of_user = input("Where are you from then? By the way I am set to be from Maryland :P")

print("From the knowledge I have,", location_of_user, "is a very enjoyable place.", "Umm... Let's do some fun "
                                                                                    "calculation", name_of_user, ".")

favorite_number_of_user = input("What is your favorite number?")

difference_between_numbers = int(favorite_number_of_user) / 7

print("I like all numbers, but I still got a favorite one. Now it it your turn to guess--my favorite number is",
      difference_between_numbers, "times bigger than yours.")

print("Yeah", name_of_user, ", My favorite number is 7. Good job :P!")

print("Now I showed your my calculating skills, what about let me help you do something?")

favorite_car_of_user = input("So what is your favorite car?")

print("To be honest, I also want one of those. Imagine......", favorite_car_of_user, "WOW...")

price_of_the_car = float(input("How much is it?"))

print("God!", price_of_the_car, "! That is a fair price for those kinds of cars but still expensive!")

years_to_buy = float(input("So what is your plan? How many years would you like to take a loan out to pay for it?"))

# I want to add as much humanity to the robot as I can

annual_interest_rate = float(input("Could you tell me your annual interest rate then?"))

print("Let me help you on this,", name_of_user, "!")

monthly_interest_rate = annual_interest_rate / 100 / 12

number_of_month = years_to_buy * 12

monthly_payment = (monthly_interest_rate * price_of_the_car) / (1 - (1 + int(monthly_interest_rate)) ^
                                                                          (- int(number_of_month))

total_car_cost = monthly_payment * int(number_of_month)

print("Here you are! I got it! Your monthly payment for", favorite_car_of_user, "is going to be", monthly_payment,
      ", and add on together you will pay", total_car_cost, "to get your car! Let's go", name_of_user, "!")

