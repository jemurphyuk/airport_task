
class Flight:
    __flight_integer = 100
    flight_list = []
    def __init__(self, airline, origin, destination, datetime):
        if airline.upper() == 'EMIRATES':
            self.flight_id = 'EK' + str(Flight.__flight_integer)
            Flight.__flight_integer += 1
        elif airline.upper() == 'BRITISH AIRWAYS':
            self.flight_id = 'BA' + str(Flight.__flight_integer)
            Flight.__flight_integer += 1
        else:
            self.flight_id = 'ZZ' + str(Flight.__flight_integer)
            Flight.__flight_integer += 1
        self.airline = airline
        self.origin = origin
        self.destination = destination
        self.datetime = datetime
        self.boarding_list = []

    def add_passenger_boarder(self, name):
        return self.boarding_list.append(name)

    def show_boarding_list(self):
        return self.boarding_list

    def add_flight_to_flight_list(self):
        return Flight.flight_list.append(self)
    # origin
    # destination
    # datetime
    # a list of passengers