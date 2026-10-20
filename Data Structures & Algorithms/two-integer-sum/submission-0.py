class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = {}
        for i, num in enumerate(nums):
            complem = target - num
            if complem in val:
                return [val[complem], i]
            val[num] = i


        