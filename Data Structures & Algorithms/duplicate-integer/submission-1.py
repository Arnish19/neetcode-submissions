class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = {}

        for n in nums:
            if n in dupe:
                return True
            else:
                dupe[n] = 1
            
        return False