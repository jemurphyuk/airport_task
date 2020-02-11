from people import People


class Passenger(People):
    passenger_list = []
    __booking_variable = 10000

    def __init__(self, name, postcode, gender, passport):
        super().__init__(name, postcode, gender)
        self.__passport = passport
        self.flight_id = Passenger.__booking_variable
        Passenger.__booking_variable += 1

    def get_passport(self):
        return self.__passport

    def add_passenger(self):
        return Passenger.passenger_list.append(self)

    # def print_flight_list():
        # return Passenger.passenger_list
    # __passport
