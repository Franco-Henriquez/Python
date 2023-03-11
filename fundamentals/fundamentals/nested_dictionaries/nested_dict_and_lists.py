#UPDATE VALUES IN DICTIONARIES AND LISTS
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]


#     # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x[1][0] = 15
# print(x)
#     # Change the last_name of the first student from 'Jordan' to 'Bryant'
# students[0]["last_name"] = "Bryant"
# print(students[0])
#     # In the sports_directory, change 'Messi' to 'Andres'
# sports_directory["soccer"][0] = "Andres"
# print(sports_directory["soccer"])
#     # Change the value 20 in z to 30
# z[0]["y"] = 30
# print(z)


#ITERATE THROUGH A LIST OF DICTIONARIES
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# # first_name - Michael, last_name - Jordan
# # first_name - John, last_name - Rosales
# # first_name - Mark, last_name - Guillen
# # first_name - KB, last_name - Tonel

# def iterateDictionary(students_list):
#     for i in range(len(students_list)):
#         first_and_last_name = ""
#         for key, value in students_list[i].items():
#             first_and_last_name += f"{key} - {value}, "
#         print(first_and_last_name[:-2])

# iterateDictionary(students)

#GET VALUES IN A LIST
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# # Create a function iterateDictionary2(key_name, some_list) that, 
# # given a list of dictionaries and a key name, 
# # the function prints the value stored in that key for each dictionary. 
# # For example, iterateDictionary2('first_name', students) should output:

# def iterateDictionary2(key,list_of_dicts):
#     for integer in range(len(list_of_dicts)):
#         keys = list_of_dicts[integer][key]
#         print(keys)

# iterateDictionary2("last_name", students)

#ITERATE THROUGH A DICTIONARY WITH LIST VALUES
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for key, value in dojo.items():
        # print key lenght and name
        length_of_key = len(value)
        key = key.upper()
        length_plus_key_name = f"{length_of_key} {key}"
        print("")
        print(length_plus_key_name)
        for i in range(len(value)):
            value_listed = value[i]
            print(value_listed)
    
printInfo(dojo)
# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
