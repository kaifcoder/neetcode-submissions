class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for n in nums:
            if mp.get(n, 0) == 1:
                return True
            mp[n] = 1 + mp.get(n, 0)
        return False