class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # return value counter
        # while num1 != 0 and num2 != 0 
        # if num1 >= num2, num1 -= num2
        # otherwise, other way around
        # increase counter
        # while loop dies once one of them hits 
        # return counter
        # Time O(max(num1, num2)) space O(1)
        num_operations = 0
        while num1 and num2:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            num_operations += 1 
        return num_operations
    
        # euclidean approach
        num_operations = 0
        while num1 and num2:
            num_operations += num1 // num2
            num1 %= num2
            num1, num2 = num2, num1
        return num_operations

    
