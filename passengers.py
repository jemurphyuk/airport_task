from people import People

class Passenger(People):
    __booking_variable = 10000
    passenger_list = []
    def __init__(self, name, postcode, gender, passport):
        super().__init__(name, postcode, gender)
        self.__passport = passport
        self.flight_id = Passenger.__booking_variable
        Passenger.__booking_variable += 1

    def get_passport(self):
        return self.__passport

    def add_passenger(self, passenger):
        return self.passenger_list.append(passenger)

    def print_flight_list(self):
        return self.passenger_list
    # __passport