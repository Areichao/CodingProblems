class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # store initial score array indicies assuming there are no ties
        initial = {}
        result = [0 for x in range(len(score))]
        for i in range(len(score)):
            initial[score[i]] = i
        
        # now sort the original list
        sortedList = self.mergeSort(score)

        # get result
        for rank, s in enumerate(sortedList):
            index = initial[s] # get initial index
            if rank == 0:
                result[index] = "Gold Medal"
            elif rank == 1:
                result[index] = "Silver Medal"
            elif rank == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank + 1)

        return result


    def mergeSort(self, array):
        # base case the array has 1 or 0 elements which means it is already sorted
        if len(array) == 0 or len(array) == 1:
            return array
        
        # divide the array into two halves
        middle = len(array) // 2
        leftHalf = self.mergeSort(array[:middle])
        rightHalf = self.mergeSort(array[middle:])

        # merge the sorted halves
        return self.merge(leftHalf, rightHalf)

    def merge(self, left, right):
        # create empty result array
        result = []
        i = j = 0

        # compare elements from both halves and pick the largest element
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])

        return result