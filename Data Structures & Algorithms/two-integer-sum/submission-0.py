class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, val in enumerate(nums):
            comp = target - val
            if comp in mp:
                return [mp.get(comp),i]
            mp[val] = i
        return []
        