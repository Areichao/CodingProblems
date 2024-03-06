import collections as c, heapq as h, math as m
class Solution:
    def reorganizeString(self, s: str) -> str:
        # first create the empty string for answer, and the max heap
        answer = "" 
        # -count because python library implements min heaps. 
        # .items() returns a list of (char, count) so we flip it to (count, char)
        maxHeap = [(-count, char) for char, count in c.Counter(s).items()]
        h.heapify(maxHeap) # convert to a priority queue
        print(maxHeap)

        # check if question is possible. if s is empty or too many repeats of one letter
        print(h.nsmallest(1, maxHeap)[0][0])
        if len(s) == 0 or h.nsmallest(1, maxHeap)[0][0] < -m.ceil(len(s)/2):
            print("This is impossible!")
            return ""

        while maxHeap: # while priority queue exists
            firstCount, firstChar = h.heappop(maxHeap) # put in negative count and char
            print("Current firstChar: ", firstChar)
            print("Current heapMax: ", maxHeap)
            if answer == "" or (answer[-1] != firstChar): # if empty or no previous repeat
                answer += firstChar # append
                print("This is the current answer: ", answer)
                firstCount += 1 # reduce count by 1 (remember we are negative)
                if firstCount < 0: # if its not 0, add back into heap
                    h.heappush(maxHeap,(firstCount, firstChar))
            else: # if we have repeat letters
                secondCount, secondChar = h.heappop(maxHeap)
                answer += secondChar + firstChar
                print("Answer with two appended: ", answer)
                secondCount += 1
                firstCount += 1
                # if there is still letters left, push back into priority queue
                if secondCount < 0: h.heappush(maxHeap, (secondCount, secondChar))
                if firstCount < 0: h.heappush(maxHeap, (firstCount, firstChar))
        return answer 

object = Solution()
print(object.reorganizeString("aaab"))
        