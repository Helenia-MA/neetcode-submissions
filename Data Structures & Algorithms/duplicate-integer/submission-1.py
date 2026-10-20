class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = set(nums)
        if len(new_nums) != len(nums):
            return True
        return False
    
        """
        # alternative - better since O(n) is worst case not average 
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.append(num)
        return False
        """

        