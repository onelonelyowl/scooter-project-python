import itertools

class Scooter():
    serialNumber = 0
    serial_number_iter = itertools.count()
    def __init__(self, station):
        self.serial = next(Scooter.serial_number_iter)
        self.user = None
        self.charge = 100
        self.isBroken = False
        self.station = station
    def __str__(self):
        return f"serial: {self.serial}, user: {self.user}, charge: {self.charge}, isBroken: {self.isBroken}, station: {self.station}"
    def __repr__(self):
        return f"serial: {self.serial}, user: {self.user}, charge: {self.charge}, isBroken: {self.isBroken}, station: {self.station}"
    def __eq__(self, other):
        assert isinstance(other, Scooter)
        return self.serial == other.serial
    def rent(self, user):
        self.user = user
        self.station = None
    def dock(self, station):
        self.station = station
        self.user = None