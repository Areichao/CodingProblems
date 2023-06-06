class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x_diff = coordinates[1][0] - coordinates[0][0]
        y_diff = coordinates[1][1] - coordinates[0][1]

        for i in range(2, len(coordinates)):
            currentx_diff = coordinates[i][0] - coordinates[i-1][0]
            currenty_diff = coordinates[i][1] - coordinates[i-1][1]
            if y_diff*currentx_diff != x_diff*currenty_diff:
                return False
            
        return True