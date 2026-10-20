class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        value_dict = defaultdict(int)
        for num in nums:
            value_dict[num] += 1
            if value_dict[num] > 1:
                return True
        return False 
            

        