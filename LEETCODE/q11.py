class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) - 1
        answer = 0
        for left, hei in enumerate(height):
            area = (right - left) * min(hei, height[right])
            answer = max(area, answer)
            while right > left and height[right] < hei:
                right -= 1
                area = (right - left) * min(hei, height[right])
                answer = max(area, answer)
            if left >= right:
                return answer
        return answer
