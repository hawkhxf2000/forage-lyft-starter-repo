from tire import Tires


class CarriganTire(Tires):

    def __init__(self, tires_wear):
        self.tires_wear = tires_wear

    def needs_service(self):
        for tire_wear in self.tires_wear:
            if tire_wear >= 0.9:
                return True

        return False
