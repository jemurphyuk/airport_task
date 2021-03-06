# import all classes
# from people import *
# from buildings import *
# from aircraft import *
from passengers import Passenger
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


# add_passenger(passenger1)

# print(vars(Passenger.print_flight_list))


# initialise 3 planes
plane1 = Plane(200, 300, 700, 132, 'Boeing', '747', 111, 4, 600)
plane2 = Plane(150, 300, 750, 111, 'Boeing', '737', 92, 2, 400)
plane3 = Plane(400, 300, 650, 160, 'Airbus', 'A380', 130, 6, 800)

# initialise 3 flights
flight1 = Flight('Emirates', 'Dubai', 'LHR', '20/01/2020')
flight2 = Flight('British Airways', 'LGW', 'JFK', '22/01/2020')
flight3 = Flight('EasyJet', 'LTN', 'CDG', '24/01/2020')

# add 2 passengers to each flight
flight1.add_passenger_boarder([passenger1, passenger2])
flight2.add_passenger_boarder([passenger3, passenger4])
flight3.add_passenger_boarder([passenger5, passenger6])

for flight in Flight.flight_list:
    print(f"Flight ID: {vars(flight)['flight_id']}")
    print(f"Airline: {vars(flight)['airline']}")
    for passenger in Flight.show_boarding_list(flight):
        print(passenger.board_id, passenger.name, passenger.get_passport())
    print('\n')


for i in range(0, len(Flight.flight_list)):
    obj = vars(Flight.flight_list[i])
    print(obj)
# obj2 = obj['boarding_list']
# # print(vars(obj2))
# print(obj)
print('\n')
# print(vars(passenger1))
# #flight_atlanta.add_passenger(passenger1)
# # list passengers in one flight
# print(vars(flight1))
# print(vars(flight2))
# print(vars(flight3))

for i in range(0, len(Passenger.passenger_list)):
    obj = vars(Passenger.passenger_list[i])
    print(obj)

obj = vars(Flight.flight_list[0])
passengerzzz = (obj['boarding_list'])
print(vars(passengerzzz[1]))