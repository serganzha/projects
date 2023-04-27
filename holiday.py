# user inputs and error handling for incorect input
try:
    city_flight = input("Please choose a destination: Berlin, Paris or Barcelona: ").lower()
    if city_flight not in ["berlin", "paris", "barcelona"]:
        raise ValueError("Invalid city selected. Please choose from Berlin, Paris, or Barcelona.")
    num_nights = int(input("Please enter the number of nights you wish to stay: "))
    rental_days = int(input("How many days will you be hiring a car for: "))
except ValueError as e:
    print(str(e))
    exit()


# functions following task specs
# calculating cost of the stay based on city and lengh of stay
def hotel_cost(city, num_nights):
    nightly_cost = 0
    if city_flight == "berlin":
        nightly_cost = 100
    elif city_flight == "paris":
        nightly_cost = 75
    elif city_flight == "barcelona":
        nightly_cost = 50
    return num_nights * nightly_cost


# flight cost function
def plane_cost(city_flight):
    if city_flight == "berlin":
        return 50
    elif city_flight == "paris":
        return 100
    elif city_flight == "barcelona":
        return 70


# instead of if/elif maybe a dictionary would suit better?
# potentially dictionary could store flight, hotel and rental costs
"""
city_costs = {"berlin": {"flight": 50, "hotel": 100, "car": 20},
            "paris": {"flight": 100, "hotel": 75, "car": 30},
            "barcelona": {"flight": 70, "hotel": 50, "car": 25}}
"""


# car rental assuming it's same across all cities
def car_rental(rental_days):
    return rental_days * 30


# function to calculate total cost of the trip
def holiday_cost(city, num_nights, rental_days):
    total_cost = hotel_cost(city, num_nights) + plane_cost(city) + car_rental(rental_days)
    return total_cost


hotel_total_cost = hotel_cost(city_flight, num_nights)
plane_total_cost = plane_cost(city_flight)
car_total_cost = car_rental(rental_days)
total_cost = holiday_cost(city_flight, num_nights, rental_days)
# print statments
print(f"The total hotel cost will be: £{hotel_total_cost}")
print(f"The total flight cost will be: £{plane_total_cost}")
print(f"The total car rental cost will be: £{car_total_cost}")
print(f"Total cost of your holiday will be: £{total_cost}, enjoy {city_flight.capitalize()}!")
