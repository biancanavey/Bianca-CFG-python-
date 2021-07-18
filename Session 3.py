#today = input('what day is it?')

#'is_monday = today == 'monday'

#Print(f'Today is Monday : {is_monday}')

# temperature = input ('what is the temperature?')
#
# is_freezing = float(temperature) <= 0
#
# print(f'The temperature is freezing: {is_freezing} ')

# Exercise 3.1: You have a budget of £10 and want to write a program to decide which burger
# restaurant to go to.
# 1. Input the price of a burger using input()
# 2. Check whether the price is less than or equal (<=) 10.00
# 3. Print the result in the format below
# Burger is within budget: True
# Hint: remember to convert the input from a string to a decimal with float()

# price = input('How much is a burger')
#
# price_10 = float(price) <= 10
#
# print(f'The burger is affordable: {price_10}')


# mars_choice = input('Would you like to visit mars? y/n')
#
# is_willing = mars_choice == 'y'
#
# affordable = input('can you afford to visit mars? y/n')
# can_afford = affordable =='y'
#
# shoud_visit_mars = is_willing and can_afford
#
# print(f'You should visit Mars:{should_visit_mars}')

# mars_choice = input('Would you like to visit mars? y/n ')
# is_willing = mars_choice == 'y'
#
# affordable = input('Can you afford to visit mars? y/n ')
# can_afford = affordable == 'y'
#
# should_visit_mars = is_willing and can_afford
#
# print(f'You should visit Mars: {should_visit_mars}')

# name = input('What is your name? ')
# is_admin = name == 'admin'
#
# password = input('What is your password? ')
# is_correct_password = password == 'kittens'
#
# if is_admin and is_correct_password:
#     print('Welcome!!!')
#
# if is_admin != True or is_correct_password != True:
#     print('Go away!!!')

# weather = input('What is the weather like?')
#
# if weather =='raining':
#     print('Make sure to bring a brolly')
# else:
#     print('All good! No brolly needed')
#
# name= input('What is your name?')
# is_admin = name =='admin'
#
# password = input('what is your password?')
# is_correct_passward = password == 'kittens'
#
# if is_admin and is_correct_passward:
#     print('Welcome!! You are who you say you are')
# else:
#     print('Go away Intruder!')

# Meal_price = float(input('How much did the meal cost?'))
# discount_choice = input('Do you have a discount? y/n)')
# discount_applicable = discount_choice == 'y'

# if discount_applicable:
#     meal_price = meal_price *0.9
#     print('Discount applied!!')
# else:
#     print('No discount')

# Meal_price = float(input('How much did the meal cost?'))
# if meal_price > 20:
#     meal_price = meal_price * 0.9
#     print (f'Discount applied! Your new total is £ {meal_price}')
# else:
#     print('No Discount')
# import random
#
# sides =int(input('How many sides does the die have?'))
# random_integer = random.randint(1,sides)
#
#print(f'you rolled a {random_integer}')
# random_integer =random.randint(1,100)
# print(randome_integer)

# import random
#
# def flip_coin():
#     random_number = random.randint(1,2)
#     if random_number == 1:
#         side = 'heads'
#     else:
#         side = 'tails'
#     return side
#
# choice = input('heads or tails: ')
# result = flip_coin()
#
# print(f'Your coin landed on {result}')

# def random_choice ():
#     choice_number = random.randint(1,3)
#     if choice_number == 1:
#         choice = 'rock'
#     elif choice_number ==2:
#         choice = 'scissors'
#     else:
#         choice = 'paper'
#         return choice
#
#     my_choice =input('choose rock,paper,or scissors:')
#     opponent_choice = random_choice()
#     print (f'Your oppinent chose {opponent_choice}')
#
#     if my_choice =='rock' and opponent_choice =='scissors':
#         print('you win!')