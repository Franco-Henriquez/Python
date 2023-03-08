# import random

# print('Welcome to Python!')

# print('This is a loop printing 5 times')
# for x in range(1, 6):
#     print(f'x is: {x}')

# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# day = random.choice(weekdays)

# print(f'Today is: {day}')

# if day == 'Monday':
#     print('It will be a long week!')
# elif(day == 'Friday'):
#     print('Woohoo, time for the weekend!')
# else:
#     print('Not quite there yet.')


# class EmptyClass:
#     pass

# for val in my_string:
#     pass

#self project, make this count to 100 but only the odd numbers
# for x in range(1, 101):
#     print(f'x is: {x}')

#sample of type conversion how to to find out the type of data with type()
# int_to_float = float(35)
# float_to_int = int(44.2)
# int_to_complex = complex(35)
# print(int_to_float)
# print(float_to_int)
# print(int_to_complex)
# print(type(int_to_float))
# print(type(float_to_int))
# print(type(int_to_complex))

#example of importanting a library and using it. Random doesn't exist in python so a separate library needs to be imported.
# import random
# print(random.randint(2,5)) # provides a random number between 2 and 5

# name = "Zen"
# print("My name is"+ name)


#String Interpolation
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")
#the java equivalent is something like this:
# console.log(`My Name is ${MyName}`);


#before string interlopation was a thing in python, it was written using the format() builtin function
#very similar to C++ (Why doesn't C++ do something like the f interlopation??)
# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# # output: My name is Zen Coder and I am 27 years old.
# print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# # output: My name is 27 Zen and I am Coder years old.

#%-formatting, this is also used in C++ !!!
# hw = "Hello %s" % "world" 	# with literal values
# py = "I love Python %d" % 3 
# print(hw, py)
# # output: Hello world I love Python 3
# name = "Zen"
# age = 27
# print("My name is %s and I'm %d" % (name, age))		# or with variables
# # output: My name is Zen and I'm 27



