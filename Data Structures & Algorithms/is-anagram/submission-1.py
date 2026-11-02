class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_1 = {}
        freq_2 = {}

        for ch in s:
            if ch in freq_1:
                freq_1[ch] += 1
            else:
                freq_1[ch] = 1
        
        for ch in t:
            if ch in freq_2:
                freq_2[ch] += 1
            else:
                freq_2[ch] = 1
        
        if freq_1 == freq_2:
            return True
        else:
            return False