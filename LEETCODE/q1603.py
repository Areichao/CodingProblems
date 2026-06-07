class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        """ initialize number of parking spaces of each size """
        self.spots = [big, medium, small]
        
    def addCar(self, carType: int) -> bool:
        """ return true if there is a parkinng spot left for this car size """
        if self.spots[carType - 1] > 0:
            self.spots[carType - 1] -= 1
            return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)