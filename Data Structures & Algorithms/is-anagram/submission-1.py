class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ch = [0] * 26
        for c in s:
            ch[ord(c) - ord('a')] += 1
        for c in t:
            ch[ord(c) - ord('a')] -= 1
        
        for i in ch:
            if i > 0:
                return False
        return True