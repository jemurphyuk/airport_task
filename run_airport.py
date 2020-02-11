# import all classes
#from people import *
from passengers import Passenger
#from buildings import *
#from aircraft import *
from plane import Plane
from flight import Flight
# identify dependencies

# start empty list of what I want to track
    # airplanes
    # passengers - select one and add to flight
    # flights - must have, and list all

# initialise 6 passengers
passenger1 = Passenger('Kenny', 'SO', 'M', 8348)
passenger2 = Passenger('Stan', 'B', 'M', 6354)
passenger3 = Passenger('Kyle', 'CV', 'M', 2457)
passenger4 = Passenger('Eric', 'CM', 'M', 9452)
passenger5 = Passenger('Clyde', 'NO', 'M', 1845)
passenger6 = Passenger('Butters', 'NW', 'M', 4572)

# initialise 3 planes
# plane1 = Plane(200, 300, 700, 132, 'Boeing', '747', 111, 4, 600)
# plane2 = Plane(150, 300, 750, 111, 'Boeing', '737', 92, 2, 400)
# plane3 = Plane(400, 300, 650, 160, 'Airbus', 'A380', 130, 6, 800)
# initialise 3 flights
flight1 = Flight('Emirates', 'Dubai', 'LHR', '20/01/2020')
flight2 = Flight('British Airways', 'LGW', 'JFK', '22/01/2020')
flight3 = Flight('EasyJet', 'LTN', 'CDG', '24/01/2020')

#flight_atlanta =
# add 2 passengers to each flight
flight1.add_passenger_boarder(passenger1)
flight1.add_passenger_boarder(passenger2)
flight2.add_passenger_boarder(passenger3)
flight2.add_passenger_boarder(passenger4)
flight3.add_passenger_boarder(passenger5)
flight3.add_passenger_boarder(passenger6)

flight_list = [flight1, flight2, flight3]

for flight in flight_list:
    print(vars(flight)['flight_id'])
    for passenger in Flight.show_boarding_list(flight):
        print(passenger.flight_id, passenger.name, passenger.get_passport())


# print(vars(passenger1))
# #flight_atlanta.add_passenger(passenger1)
# # list passengers in one flight
# print(vars(flight1))
# print(vars(flight2))
# print(vars(flight3))