class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
        # we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True

    def about_this_shoe(self):
        if self.in_stock == True:
            print(f"{self.brand} are {self.type} shoes priced at ${self.price} currently in stock.")
        elif self.in_stock == False:
            print(f"{self.brand} are {self.type} shoes priced at ${self.price} but not in stock.")
        else:
            pass


skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
print(skater_shoe.type)	# output: Low-top Trainers
print(dress_shoe.type)	# output: Ballet Flats
print(f"Skaer Shoe In stock: {skater_shoe.in_stock}")
print(f"Dress Show In stock: {dress_shoe.in_stock}")
skater_shoe.in_stock = False
print(skater_shoe.about_this_shoe())
print(dress_shoe.about_this_shoe())


class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
    # adding the greeting method
    def greeting(self):
        print(f"Hello, my name is {self.name}")

adrien = User("Adrien", "adion@codingdojo.com")
cool_person = User("Sadie", "sflick@codingdojo.com")
    
adrien.greeting()
# prints Hello, my name is Adrien
    
cool_person.greeting()
# prints Hello, my name is Sadie

