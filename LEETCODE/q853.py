class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_sort = sorted(zip(position, speed), key=lambda car: car[0], reverse=True)
        time_target = [((target - pos) / spd) for pos, spd in car_sort]
        fleets = 1 # minimum one fleet bc n >= 1
        curr_time = time_target[0] # atleast one target, no div by 0 bc speed > 0
        for time in time_target:
            if time > curr_time:
                curr_time = time
                fleets += 1
        return fleets