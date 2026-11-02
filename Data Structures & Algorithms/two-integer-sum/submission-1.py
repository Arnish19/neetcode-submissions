class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in mp:
                return [mp[complement], index]
            else:
                mp[value] = index