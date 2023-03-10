# #Basic - Print all integers from 0 to 150.
# for integer in range(0,151):
#     print(integer)

# #Multiples of Five - Print all the multiples of 5 from 5 to 1,000
# for integer in range(0,1001,5):
#     print(integer)

# # Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
# for integer in range(1,101):
#     if integer % 10 == 0:
#         print("Coding Dojo")
#     elif integer % 5 == 0:
#         print("Coding")
#     else:
#         print(integer)

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
#for loop version
# for integer in range(0,500000):
#     if integer % 2 == 1:
#         # print(integer)
#         integer += integer

# print("Result:",integer)

#TO DO
#while loop version

# Countdown by Fours - Print positive nsdumbers starting at 2018, counting down by fours.
# integer = 2018
# while integer > 0:
#     if integer % 2 == 0:
#         print(integer)
#         integer -= 4
# else:
#     print("Final else statement")

#Flexible Counter - Set three variables: lowNum, highNum, mult.
#Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
#For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
# lowNum=1
# highNum=16
# mult=3
# for integer in range(lowNum,highNum):
#     if integer % mult == 0:
#         print(integer)
#         integer += 1

#TO DO make the while loop version work
# while lowNum <= highNum:
#     if lowNum % mult == 0:
#         print(lowNum)
#         lowNum += 1

