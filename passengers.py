from people import People


class Passenger(People):
    __booking_variable = 10000
    passenger_list = []

    def __init__(self, name, postcode, gender, passport):
        super().__init__(name, postcode, gender)
        self.__passport = passport
        self.board_id = Passenger.__booking_variable
        Passenger.__booking_variable += 1
        Passenger.__append_passenger_to_list(self)

    def get_passport(self):
        return self.__passport

    @classmethod
    def __append_passenger_to_list(cls, passenger):
        cls.passenger_list.append(passenger)

    # def print_flight_list():
        # return Passenger.passenger_list
    # __passport
