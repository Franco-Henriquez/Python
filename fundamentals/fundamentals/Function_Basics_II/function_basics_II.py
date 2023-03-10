# Countdown - Create a function that accepts a number as an input.
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

# print("Please enter a countdown number")
# # to ensure that the list is accesible outside the function and
# # if the loop is placed inside a for loop, then every loop will
# # see the array/list as empty
# list_count = [] 

# def countdown(count):
#     count = int(count)
#     for integer in range(0,count+1):
#         list_count.append(count)
#         count -= 1
#         # print(count)
#     return list_count
# user_input = input()
# x = countdown(user_input)
# print(x)

# def countdown(count):
#     while count >= 0:
#         list_count.append(count)
#         count -= 1
#     return list_count

# user_input = int(input())
# x = countdown(user_input)
# print(x)


# # Print and Return - Create a function that will receive a list with two numbers.
# # Print the first value and return the second.
# # Example: print_and_return([1,2]) should print 1 and return 2
# def print_and_return(num_list):
#     print(num_list[0])
#     return num_list[1]
# print_and_return([5,9])
# #reason we don't see the return value is because we aren't printing it
# #but it is there, so will store the return in a var to neatly print it
# # x = print_and_return([5,9])
# # print(x)


# # First Plus Length - Create a function that accepts a list and returns the sum of the first value
# # in the list plus the list's length.
# # Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
# def first_plus_length(num_list):
#     # print("Lenght:",len(num_list))
#     x = num_list[0] + len(num_list)
#     return x
# print(first_plus_length([1,2,3,4,5]))

# # Values Greater than Second - Write a function that accepts a list and creates a new list containing 
# # only the values from the original list that are greater than its 2nd value.
# # Print how many values this is and then return the new list. 
# # If the list has less than 2 elements, have the function return False
#     # Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#     # Example: values_greater_than_second([3]) should return False
# def values_greater_than_second(num_list):
#     #always keep the initial array/list creation outside of the loop,
#     #otherwise the list gets reset every loop
#     new_list = []
#     for value in num_list:
#         if len(num_list) > 1 and value > num_list[1]:
#             new_list.append(value)
#         elif len(num_list) < 2:
#             return False
#         else:
#             continue
        
#     return new_list

# my_list = [3]
# print(values_greater_than_second(my_list))

# # This Length, That Value - 
# # Write a function that accepts two integers as parameters: size and value.
# # The function should create and return a list whose length is equal to the given size,
# # and whose values are all the given value.
# #     Example: length_and_value(4,7) should return [7,7,7,7]
# #     Example: length_and_value(6,2) should return [2,2,2,2,2,2]
# def length_and_value(size,value):
#     num_list = []
#     for integer in range(0,size):
#         num_list.append(value)
#     return num_list

# print(length_and_value(6,2))