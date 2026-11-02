class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        result = []

        # Merge while both have characters
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        # Add remaining characters
        while i < len(word1):
            result.append(word1[i])
            i += 1

        while j < len(word2):
            result.append(word2[j])
            j += 1

        return "".join(result)
