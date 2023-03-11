# the 'from' command? only works when its python files you want to import are
# inside a folder called __pycache__
# I don't know why yet
# from assets.jokes import jokes_list
# from assets.quotes import quotes_list

# will use a combined quotes and jokes file with separate lists
from assets.jokes_and_quotes import jokes_list 
from assets.jokes_and_quotes import quotes_list
import time
import random


# def jokeBot():
#     print("Do you want to hear a joke? y/n")
#     user_input = input()
#     if user_input == "y":
#         pass
#     else:
#         pass

def jokeBot(x):
    this_joke = random.choice(jokes_list)
    random_int = random.randrange(2,6)
    print(f"Just to confirm, you want to hear a joke{x}, correct? y/n")
    user_input = input()
    if user_input == "y":
        # print("user said yes")
        print("okay let me find something...")
        time.sleep(2)
        print(this_joke["setup"])
        time.sleep(random_int)
        print(this_joke["punchline"])
        time.sleep(2)
        quoteBot(" again")
    elif user_input == "n":
        print("user said no")
    else:
        print("I couldn't understand what you said")

def quoteBot(x):
    this_quote = random.choice(quotes_list)
    random_int = random.randrange(2,6)
    print(f"Just to confirm, you want to hear a quote{x}, correct? y/n")
    user_input = input()
    if user_input == "y":
        # print("user said yes")
        print("okay let me find a quote for you...")
        time.sleep(2)
        print(this_quote["text"])
        time.sleep(random_int)
        print("by",this_quote["author"])
        time.sleep(2)
        quoteBot(" again")
    elif user_input == "n":
        print("user said no")
    else:
        print("I couldn't understand what you said")

def jokesNquotes():
    print("Would you like to hear a joke or a quote? joke/quote")
    user_input = input()
    if user_input == "joke":
        jokeBot("")
    elif user_input == "quote":
        quoteBot("")
    else:
        print("I did not understand.")

# jokesNquotes()

# to do:
# fix the quote and joke functions so that the bot sounds less bot-like
# may need to add additional if statements


# Notes:
# so quotes and jokes file have 2 lists
# one is called jokes_list
# the other is called quotes_list
# a list is an array and we access them with:
print(quotes_list[0])
# within each index of quotes_list, is a dictionary (object sort of)
# an object that contains two keys: text and author
# so to access a specific author from a specific array/list index # for example:
print(quotes_list[0]["author"])