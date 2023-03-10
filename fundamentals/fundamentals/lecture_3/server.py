# this is an example of pulling data from an unknown container
# by debugging using print and other forms of logging vars
from models.weather import Weather
import time


Weather.save({
    "city":"Dallas",
    "state":"TX",
    "temp":"68",
    "precip":"40%"
})

Weather.save({
    "city":"Cortland",
    "state":"NY",
    "temp":"27",
    "precip":"96%"
})
Weather.save({
    "city":"Union",
    "state":"NJ",
    "temp":"41",
    "precip":"1%"
})

def weatherBot(q):
    print(f"Would you like to know the weather from a specific city{q}? y/n")
    user_input = input()
    if user_input == "y":
        print("What city's weather would you like to know?")
        print("here is a list of all available cities:")
        for x in Weather.get_all():
            # print(x)
            print(x.city)
        city = input()
        if city:
            citys_temperature = Weather.get_one_by_city(city).temp
            citys_precip_chance = Weather.get_one_by_city(city).precip
            citys_state = Weather.get_one_by_city(city).state
            city_parsed_info = citys_temperature +" "+ citys_precip_chance +" "+ citys_state
            print(f"The weather in {city}, {citys_state} is {citys_temperature}°")
            print(f"Chance of precipitation is {citys_precip_chance}")
            weatherBot(" again")
        elif not city or city == "none":
            print("closing the weather app")
    else:
        print("Closing the weather app")






    # print(Weather.get_all())
    

weatherBot("")
# city = "Union"
# citys_temperature = Weather.get_one_by_city(city).temp
# citys_precip_chance = Weather.get_one_by_city(city).precip
# citys_state = Weather.get_one_by_city(city).state
# city_parsed_info = citys_temperature +" "+ citys_precip_chance +" "+ citys_state
# print(city_parsed_info)


