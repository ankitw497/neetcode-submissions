class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_nums = sorted((num,i) for i, num in enumerate(nums))
        i, j = 0, len(nums) - 1
        while (i < j) and (i != j):
            current_sum = index_nums[i][0] + index_nums[j][0]
            if current_sum > target:
                j -= 1
            elif current_sum < target:
                i += 1
            else:
                return sorted([index_nums[i][1],index_nums[j][1]])
        