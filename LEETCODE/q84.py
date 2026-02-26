class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_area = 0
        rectangle = [] # stack to store index an d height
        # go through each histogram rectangle from left to right, keep in mind index
        for i, height in enumerate(heights):
            if not rectangle or height >= rectangle[-1][1]: # if this is the first rectangle, or next rectangle is taller than what we have
                rectangle.append((i, height))
            else: # otherwise (if histogram is shorter)
                indx = 0
                # while the histogram is shorter than the top of stack & stack isnt empty, keep popping and calculating the max area and update.
                while rectangle and height <= rectangle[-1][1]:
                    indx, hei = rectangle.pop()
                    largest_area = max(hei * (i - indx), largest_area) # area is height * current index - position of rectangle start
                if not rectangle: # if stack is now empty, make starting point the leftmost side
                    rectangle.append((0, height))
                else: # otherwise, take the index of the last rectangle of same height
                    rectangle.append((indx, height))
        # after for loop, go through the things which remain in the stack and calculate the area for those
        for rec in rectangle:
            area = rec[1] * (len(heights) - rec[0]) # area is height * full length of histogram to position of rectangle
            largest_area = max(area, largest_area)
        return largest_area