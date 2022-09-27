from tire import Tires


class TireFactory(Tires):

    def __init__(self, tires_wear):
        self.tires_wear = tires_wear

    def needs_service(self):
        tires_wear = 0
        for tire_wear in self.tires_wear:
            tires_wear += tire_wear
        if tires_wear >= 3:
            return True
        else:
            return False
