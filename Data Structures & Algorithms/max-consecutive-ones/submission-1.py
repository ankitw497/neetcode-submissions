class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        i, count, max_count = 0, 0 , 0
        while i < len(nums):
            if nums[i] == 1:
                count  += 1
                if count >= max_count:
                    max_count = count
            else:
                count = 0
            i += 1
        return max_count    






        