#  Create function for hotel_cost
def hotel_cost(num_nights):
    nightly_fee = 125
    return num_nights * nightly_fee

#  Create function for plane_cost
#  Return 0 if required inputs are not entered
def plane_cost(city_flight):
    if city_flight == "Budapest":
        return 340
    if city_flight == "Istanbul":
        return 460
    if city_flight == "Lisbon":
        return 400
    if city_flight == "Rome":
        return 280
    if city_flight == "Athens":
        return 380
    else:
        return 0

#  Create function for car_rental
def car_rental(rental_days):
    daily_fee = 42
    return rental_days * daily_fee

#  Create function for total holiday_cost
#  Create a sum to add the three variables together
def holiday_cost(num_nights, city_flight, rental_days):
    hotel = hotel_cost(num_nights)
    flight = plane_cost(city_flight)
    car = car_rental(rental_days)
    total = hotel + flight + car
    
    #  Output according to user inputs
    print("\nYour holiday!\n")
    print("*************\n")
    print(f"You will fly to: {city_flight}")
    print(f"The cost of this hotel is: £{hotel}")
    print(f"The cost of your flight will be: £{flight}")
    print(f"The cost of the car rental will be: £{car}")
    print(f"The overall holiday will cost: £{total}")
    
    return total

#  Request inputs once all is defined
print("Your holiday choices are: Budapest, Istanbul, Lisbon, Rome, Athens")
city_flight = input("Which city will you be flying to? ")
num_nights = int(input("How many nights will you be staying? "))
rental_days = int(input("How long will you rent the car for? "))

#  Call on the functions to be printed
holiday_cost(num_nights, city_flight, rental_days)