class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}

        for _ in s:
            if _ in freq_s:
                freq_s[_] += 1
            else:
                freq_s[_] = 1
        
        for _ in t:
            if _ in freq_t:
                freq_t[_] += 1
            else:
                freq_t[_] = 1
        
        if freq_s == freq_t:
            return True
        
        else:
            return False