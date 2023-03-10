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
# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print(f"My name is {first_name} {last_name} and I am {age} years old.")
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


# num_list = [1, 5, 8, 4] 
# my_list = [1, 'Zen', 'hi']
# my_list.pop()

# print(len(my_list))
# output

#TypeError: '>' not supported between instances of 'str' and 'int'
# for example it wont work with my_list because Zen and hi are strings
# print(max(num_list)) #returns the highest value in a sequence.
# print(min(num_list)) #returns the lowest value in a sequence.
# print(sorted(num_list))

# other cool builtin functions for lists (arrays)
    # list.append(value) appends a value to the end of the list.
    # list.pop(index) remove a value at given position. if no parameter is passed, it will remove the last value in the list.
    # Very very cool, index works with strings too. Possibly all value types.
    # list.index(value) returns the index (position) of the given value if it exists in the list and raises an error if it does not exist.
    # list.reverse() reverses the order of the elements, in place.*
    # list.sort() sorts the items in order of least to greatest, or alphabetically for strings, in place.*
# print(num_list.pop()) # cool thing here, it prints/logs the number removed while also removing it :D
# print(num_list)
# print(my_list.index('Zen'))

#important thing to remember is that the last number (16) in a range will not print.
# also by default if no start (2) is set
# for i in range(2, 16, 3):
#     print(i)

# range doesn't seem to work alone, only works along with for loops and
# when stored in something but can't directly log/print a range
# print(list(range(2,6)))

# count = 0
# while count <= 5:
#     print("looping - ", count)
#     count += 1

#again important to remember, the 5 is not counted, but because we start at 0, we are still counting up to 5 times.
# for x in range(0,5):
#     print("looping =", x)

# y = 3
# while y > 0:
#     print(y)
#     y = y - 1
# else:
#     print("Final else statement")


# TO DO
#fix this so that it returns the changed result of num_list
# num_list = ["oranges", "apples", "grapes", "bananas","celery"] 

# def replace(a,b):
#     indexOfA = num_list.index(a) 
#     num_list[indexOfA] = b
#     return "Complete"

# replace("celery","Pineapple")

#LOOPS OVER LISTS
# my_list = ["abc",123,"xyz"]
# for integer in range(0, len(my_list)):
#     #reason we tell the range to start at 0 is because lists indexes always start with 0
#     #this line provides the index number followed by whats in content inside that position.
#     print(integer, my_list[integer])
#     # output:
#     # 0 abc
#     # 1 123
#     # 2 xyz

# # this is an easy way to loop through a list, the for loop basically again even though we dont' tell it to start anywhere,
# # it knows that a list starts at index 0, so it just loops until the end of the index.
# # our index has 3 indexes
# #    0    1    2
# # ["abc",123,"xyz"]
# for i in my_list:
#     print(i)
#     #output:
#     # abc
#     # 123
#     # xyz


# another example like the one above
# countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]
# # Challenge 1: Fix the range!
# for integer in range(0, len(countries)):
#     print("Index:",integer)
#     # Challenge 2: print the index here
#     print("Country:",countries[integer])
#     # Challenge 3: print the country here

# # Looping over values only...
# for country in countries:
#     print("Country: ", country)
#     # Challenge 4: print the country here

# y = 3
# while y > 0:
#     print(y)
#     y -= 1
# else:
#     print("Final else statement")

# x = 0
# while x < 6:
#     print(x)
#     x += 1
# else:
#     print("Final else statement")



#EXAMPLE OF BREAKS
y = 3
while y > 0:
    print(y)
    y = y - 1
    #so you would think that while y is above 0, it will keep looping, except the loop is broken while it's running y = 1
    # reason for this is because after it print(y) it also does y = y - 1
    # so before it gets a chance to loop again, the if statement stops it because now y is equal to 0
    # so it never gets a chance to loop one last time just to trigger the else statement from while
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")
# output: 3, 2, 1

#EXAMPLE OF CONTINUES
for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i