class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = []
        suffixProduct = [] # Space O(2n)
        for i in range(len(nums)): # Time O(n)
            if not prefixProduct: # if this is the first element
                prefixProduct.append(nums[i])
                suffixProduct.append(nums[-(i+1)])
            else:
                prefixProduct.append(nums[i] * prefixProduct[i-1])
                suffixProduct.append(nums[-(i+1)] * suffixProduct[i-1])

        # actual solution
        answer = []
        for i in range(len(nums)): # Time O(n)
            if not answer:
                answer.append(suffixProduct[-(i + 2)])
            elif i == len(nums) - 1:
                answer.append(prefixProduct[i-1])
            else:
                answer.append(prefixProduct[i-1] * suffixProduct[-(i + 2)])
        return answer

