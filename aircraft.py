class Aircraft:
    aircraft_inventory = []

    def __init__(self, capacity, mass, flying_speed, nose_to_tail_length, manufacturer, model):
        self.capacity = capacity
        self.mass = mass
        self.speed = flying_speed
        self.length = nose_to_tail_length
        self.make = manufacturer
        self.model = model

    def add_to_aircraft_list(self):
        return Aircraft.aircraft_inventory.append(self)
    #
