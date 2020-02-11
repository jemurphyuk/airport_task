from aircraft import Aircraft


class Plane(Aircraft):
    def __init__(self, capacity, mass, flying_speed, nose_to_tail_length, manufacturer, model, wingspan, jet_engine_num, fuel_capacity):
        super().__init__(self, capacity, mass, flying_speed, nose_to_tail_length, manufacturer, model)
        self.wingspan = wingspan
        self.engines = jet_engine_num
        self.fuel = fuel_capacity

