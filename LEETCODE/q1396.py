class UndergroundSystem:
    def __init__(self):
        """ Constructor """
        # all functions are O(1) for time, O(C + R) for space
        self.customers = {}
        self.routes = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        """ A customer with a card ID equal to id, checks in at the station stationName at time t.
            A customer can only be checked into one place at a time.
        """
        if not isinstance(id, int) or not isinstance(t, int):
            raise TypeError("ID and time should be an integer")
        if not isinstance(stationName, str):
            raise TypeError("Station name should be a string")
        if t < 0:
            raise ValueError("Time should be a non-negative integer")
        
        if id not in self.customers:
            self.customers[id] = (stationName, t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        """ A customer with a card ID equal to id, checks out from the station stationName at time t. """
        if id in self.customers:
            # unpacking and deleting from hash table
            startStation, time = self.customers.pop(id)
            # if route exists, append onto the current values
            if (startStation, stationName) in self.routes: # (total, count)
                total, count = self.routes[(startStation, stationName)]
                self.routes[(startStation, stationName)] = [total + (t - time), count + 1]
            # if route doesnt exist, add it into the hash table
            else:
                self.routes[(startStation, stationName)] = [t - time, 1]
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        """ Returns the average time it takes to travel from startStation to endStation. """
        total, count = self.routes[(startStation, endStation)]
        return total / count