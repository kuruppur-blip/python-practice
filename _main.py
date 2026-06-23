# print("hello")
# print()
# print("hello")
# print('hello')
# print("I'm coding")
# print("I'm coding")


# print( 5 + 5)
# print("5" + "5")
# print(5.0 + 5.0)
# print("5" + 5)
# print(5 + 5.0)

# name = "Rasini Kuruppu"
# age = "15"
# print(name + " is " + age )
# name = input("What's your name?")


# name = "Helen"
# age = 15 
# print(name + " is " + age)

# name = "Helen"
# age = 15 
# print(name, "is", age)


# print('hello' .upper())
# print('HELLO' .lower())

# if 'HELLO' == 'hello':
#     print('The same!')
# if 'HELLO'.lower() == 'hello':
#     print('The same!')



# guess = input("What's the password")
# print('Checking password is a match...')
# while guess != 'secret':
#     guess = input('Try again')
#     print('Checking password is a match...')
# input('Welcome')




# print(random.random())
# import random 
# print(random())
# import random 
# print(random.random())
# print(random.randint(0,10))




# user_input = 'idk'
# try: 
#     num = int(user_input)
#     print(f'You picked {num}')
# except: 
#     print(f'{user_input} is not a number!')
    



# shopping_list = ['apples','plums','pizza']
# print('aplles' in shopping_list)
# print('a' in 'definitely')
# user_input = input()
# if user_input.lower() in['a','b','c','d']:
#     print('Checking answer...')
# else:
#     print("That's not a valid answer!")


# print(len('apples'))

# shopping_list = ['apples','plums','pizza']
# print(len(shopping_list))

# shopping_list = ['apples','plums','pizza']
# print(len(shopping_list[1]))

# if len(input()) == 0:
#     print("You didn't type anything")





# for food in ['apples','carrots','muesli']:
#     print(food)

# for i in range(10):
#     print('Hello')

# foods = ['apples','carrots','muesli']
# for i in range(len(foods)):
#     print(f'{i+1}.{foods[i]}')






def calculate_area(x,y): 
    print (f"Area : {x,y}")

calculate_area()

def repeat_message(message,times):
    for i in range(times): 
        print (message)


repeat_message(5, "Hello")




def get_number(): 
    while True: 
        num = input("Give me a number.")
        try: 
            num = int(num)

        except: 
            print("That's not a number")


num = get_number() 

